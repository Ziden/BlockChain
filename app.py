from blockchain import BlockChain

if __name__ == "__main__" :
	blockchain = BlockChain()
	firstBlock = blockchain.firstBlock()
	blockchain.addBlock(firstBlock)
	for i in range(0, 100):
		newBlock = blockchain.generateBlock()
		blockchain.addBlock(newBlock)
		print "Block #{} Added!".format(newBlock.index)
		print "Hash: {}\n".format(newBlock.hash) 

