import itertools
import hashlib as hasher
import datetime as date
import string


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """ Конструктор нового объекта """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        """ Функция для создания нового блока """
        sha = hasher.sha256()
        data = (str(self.index) + str(self.timestamp) + 
                   str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(data)
        return sha.hexdigest()
    
    
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", str(0))


def next_block(last_block, data):
    current_index = last_block.index + 1
    current_timestamp = date.datetime.now()
    current_hash = last_block.hash
    return Block(current_index, current_timestamp, data, current_hash)


def create_blockchain():
    blockchain = [create_genesis_block()]
    for index in itertools.count():
        data = yield
        block = next_block(blockchain[index], data)
        yield block
        blockchain.append(block)

blockchain = create_blockchain()
next(blockchain)
print(blockchain.send('LSD was ordered').data)
