import hashlib
import datetime as date

def getBlockHash(block):
	    sha = hashlib.sha256()
	    sha.update(str(block.index) + 
	               str(block.timestamp) + 
	               str(block.data) + 
	               str(block.previousHash))
	    return sha.hexdigest()
	    
class Block:

  def __init__(self, index, timestamp, data, previousHash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previousHash = previousHash
    self.hash = getBlockHash(self)
  

if __name__ == "__main__" :
	blockchain = BlockChain()
	firstBlock = blockchain.firstBlock()
	blockchain.addBlock(firstBlock)
	for i in range(0, 100):
		newBlock = blockchain.generateBlock()
		blockchain.addBlock(newBlock)
		print "Block #{} Added!".format(newBlock.index)
		print "Hash: {}\n".format(newBlock.hash) 

