import hashlib
import json

class Blockchain():
  def __init__(self):
    self.chain = []
    self.pending_transactions = []
    self.new_block(previous_hash="Genesis block", proof=100)
  
  def new_block(self, proof, previous_hash = None):
    block_info = {
      'index': len(self.chain) + 1,
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

      
      previous_hash3 = self.hash(self.chain[-1])
      if previous_hash2 == previous_hash3:
        print("block " + str(block_number - 2) + " is valid")
      else:
        print("blockchain is invalid")
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
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 Karstcoin')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 Karstcoin')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 Karstcoin')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 Karstcoin')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 Karstcoin')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 Karstcoin')
t7 = blockchain.new_transaction("Jaap", "Karsten", '0 Karstcoin')
blockchain.new_block(6789)

t8 = blockchain.new_transaction("Tim", "Bern", '2 Karstcoin')
blockchain.new_block(125)

t9 = blockchain.new_transaction("Bern", "Tim", '2 Karstcoin')
blockchain.new_block(420)

t10 = blockchain.new_transaction("Bern", "Tim", '3 Karstcoin')
blockchain.new_block(440)

t11 = blockchain.new_transaction("Bern", "Tim", '3 Karstcoin')
blockchain.new_block(442)

t12 = blockchain.new_transaction("Alice", "Mike", '1 Karstcoin')
t13 = blockchain.new_transaction("Bob", "Alice", '0.5 Karstcoin')
t14 = blockchain.new_transaction("Mike", "Bob", '0.5 Karstcoin')
t15 = blockchain.new_transaction("Joost", "Jaap", '0 Karstcoin')
blockchain.new_block(101112)

t11 = blockchain.new_transaction("Ester", "Rik", '5 Karstcoin')
blockchain.new_block(442)

t12 = blockchain.new_transaction("Satoshi", "Mike", '5 Karstcoin')
t13 = blockchain.new_transaction("Mike", "Satoshi", '1 Karstcoin')
t14 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 Karstcoin')
blockchain.new_block(131415)


#Je kan een nieuw block aanmaken door een variatie op deze regel toe te voegen
#t(n+1) = blockchain.new_transaction("NaamGever", "NaamOntvanger", 'X Karstcoin') | Je kan meerdere transactions toevoegen per block
#blockchain.new_block(x) | Waarbij x elk  getal mag zijn

#Als je in de oude transactie iets aanpast en de code runt dan geeft hij aan dat de blockchain op dat punt invalid is

#https://github.com/Bart1003/Blockchain-pws-2.0/settings/access?query=filter%3Apending_invitations 