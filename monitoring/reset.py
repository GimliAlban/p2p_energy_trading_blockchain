import sys
sys.path.insert(1, '../')

from contract.smart_contract_details.contractInfo import web3, contract

web3.eth.defaultAccount = web3.eth.accounts[0]

contract.functions.reset().transact()
