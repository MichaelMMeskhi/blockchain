class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transaction = []

	def new_block(self):
		# Creates a new block and addes it to the chain
		pass

	def new_transaction(self):
		# Add a new transaction to the list of transactions
		pass

	@staticmethod
	def hash(block):
		# Hashes a block
		pass

	@property
	def last_block(self):
		# Return the last block in the chain
		pass