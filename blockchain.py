import hashlib
import datetime as date
from block import Block

class BlockChain:

	def __init__(self):
		self.chain = []
		self.previousBlock = None

	def addBlock(self, block):
		self.chain.append(block)
		self.previousBlock = block

	def firstBlock(self):
  		return Block(0, date.datetime.now(), "Genesis Block", "0")

  	def generateBlock(self):
		index = self.previousBlock.index + 1
	  	timestamp = date.datetime.now()
	  	data = "Block data for index " + str(index)
	  	hashe = self.previousBlock.hash
	  	return Block(index, timestamp, data, hashe)
