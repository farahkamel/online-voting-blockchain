#  the below library module is an interface for hashing messages easily
from hashlib import *
# adding the below module of cryptography will provides cryptographic recipes and primitives 
import cryptography
from time import time
import time

# setting the global value of mine_difficulty as 2
mine_difficulty = 2
# now defining the class Blocks which will handle the list of records (i.e. blocks) of movies
class Blocks:
    # setting the movie blocks as declaring with 0 to initialize
    block_number = 0
    # defining the init method to initialize the parameters 
    def __init__(self, timecreation,information, lasthash="2"):
        # the below lines will set the blocknumber depending on the number of movies in the database
        self.block_number = Blocks.block_number
        # the following line will keep on incrementing the movies number one by one to keep on displaying all
        Blocks.block_number +=1
        # the below snippet will keep on check on the time of creating threads each time for the record (timestamp)
        self.timecreation = timecreation
        # it will save the information and will update its value after each block extraction
        self.information = information
        # it will use Ethereum in which every block has a nonce. The nonce is the number of transactions sent from a given address.
		# In cryptography, a nonce is a one-time code selected in a random or pseudo-random manner that is used to secure transmition
        self.nonce_ethereum = 0
        self.lasthash = lasthash
        self.block_hash = self.proof_of_work()

    #the following function will perform the task of hashing to index the movies according to their respective IDs
    def hashing(self):
        # hashing the blocks
        # it will return the cryptographic indices using the algorithm of  Secure Hash Algorithms (sha256)
        return sha256(str(self.nonce_ethereum*3 - self.timecreation*5).encode('utf-8')).hexdigest()
        
    # this will create a block each time a new record is demanded by the main thread call
    def createblock(self):
        # creating a brand new block in the block_chain
        # it will print the complete block information
        print(("Block's index: ", self.block_number),("Block's time creation: ", self.timecreation),
         ("Block's information: ", self.information),("Nonce ethereum: ",self.nonce_ethereum),
         ("last hash: ", self.lasthash),("Block_hash: ", self.block_hash,'\n') )


    # the following function will create a decentralized consensus mechanism that will require members of a network to 
	# expend effort solving an arbitrary mathematical puzzle to prevent anybody from gaming the system
    # basic algorithm for the work proof
    def proof_of_work(self,proofwork=mine_difficulty):
        self.nonce_ethereum = 0
        while (self.hashing()[:proofwork] !="0"*proofwork):
            self.nonce_ethereum +=1
        return self.hashing()
# the below is the class declaration of the actual Block_chaining
class Block_chain:
    # it will create  the init function to handle the class parameter which in this case is only chains.
# Each block in the chain contains a number of transactions(voting transacction), and every time a new transaction occurs on the 
# blockchain, a record of that transaction is added to every participant's ledger.
    def __init__(self) :
        self.chains = []

    # creating the Genesis block (first block)
    def Genesis_first_block (self):
        # it will return the time when the first Genesis block is created
        return Blocks (time.time(), "Gensis block is first")

    # the following method of this class will create the Genesis block by calling the method  Genesis_first_block  and appending in the chains
	# which is the main parameter of our this class
    def create_Genesisblock(self):
        self.chains.append(self.Genesis_first_block())

    # the following method is very vital in the block chaining as it will create the blocks/ records for extracting the movies from the web page
    def creating_block(self,currentblock):
        # it will append the current blocks or records to the list of the chains each time a request will be made through the query 
        currentblock.lasthash = self.chains[len(self.chains)-1].block_hash
        currentblock.block_hash = currentblock.proof_of_work()
        self.chains.append(currentblock) 
    
    # the following function will validate each time a new block is created which is very important in the whole process of block chaining
    def validating_block(self):
        # it will loop over all the blocks and will keep on validating them based on their hashing and conditions and will return boolean value as True or False
        for k in range(1,len(self.chains)):
            if self.chains[k].block_hash != self.chains[k].hashing():
                return False
            if self.chains[k-1].block_hash !=self.chains[k].lasthash:
                return False

        return True
    # the method below will show the created blocks after validating them correctly
    def showing_chains(self):
        return [self.chains[k] for k in range (len(self.chains)) if self.chains[k].block_number!=0]
    



