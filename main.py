import hashlib
import json
from time import time


class Blockchain():
  def __init__(self):
    self.chain = []
    self.pending_transactions = []
    self.new_block(previous_hash="Genesis block", proof=100)
  
  def new_block(self, proof, previous_hash = None):
    block_info = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.pending_transactions,
      'proof': proof,
    }
    index = len(self.chain) + 1
    previous_hash =  previous_hash or self.previous_hash(index)
    block = [block_info]
    self.pending_transactions = []
    self.chain.append(block)
    name = "block " + str(len(self.chain)-1) + ".txt"
    with open(str(name), 'w') as f:
      f.write(str(block) + "\n" + previous_hash)
    
    
    return block

  def previous_hash(self, block_number):
    try:
      name = "block " + str(block_number -1) + ".txt"
      with open(str(name), 'r') as f:
        previous_hash = f.readlines()
        previous_hash2 = previous_hash[1]
      return previous_hash2
      
    except:
     
      previous_hash = self.hash(self.chain[-1])
      return previous_hash
          


  def new_transaction(self, sender, recipient, amount):
    transaction = {
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    }
    self.pending_transactions.append(transaction)
    return len(self.chain)

  def hash(self, block):
    string_object = json.dumps(block, sort_keys=True)
    block_string = string_object.encode()

    raw_hash = hashlib.sha256(block_string)
    hex_hash = raw_hash.hexdigest()

    return hex_hash






blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
t7 = blockchain.new_transaction("Jaap", "Kirsten", '0 BTC')
blockchain.new_block(6789)

t8 = blockchain.new_transaction("Tom", "Bern", '2 BTC')
blockchain.new_block(125)

t9 = blockchain.new_transaction("Bern", "Tim", '2 BTC')
blockchain.new_block(420)