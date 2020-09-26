from contractInfo import web3

from contractInfo import contract

#Select the account number for the Ganache blockchain:
web3.eth.defaultAccount = web3.eth.accounts[0]

contract.functions.reset().transact()
