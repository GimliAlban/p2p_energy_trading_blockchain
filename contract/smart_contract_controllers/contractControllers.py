import sys
sys.path.insert(1, '../../')

from contract.smart_contract_details.contractInfo import contract

def getAvailableEnergy():
    return contract.functions.getAvailableEnergy().call()

def getDemandEnergy():
    return contract.functions.getDemandEnergy().call()

def getConsumedEnergy():
    return contract.functions.getConsumedEnergy().call()

def getContractBalance():
    return contract.functions.getBalance().call()

def getMaxBalanceForThisCycle():
    return contract.functions.getMaxBalanceForThisCycle().call()

def getNumberConsumer():
    return contract.functions.getNumberConsumer().call()

def getNumberProsumer():
    return contract.functions.getNumberProsumer().call()
