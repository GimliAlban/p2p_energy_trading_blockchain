import sys
sys.path.insert(1, '../../')

from contract.smart_contract_details.contractInfo import contract, web3, address


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


def updateEnergy(newEnergy, pastEnergy):
    tx_hash = contract.functions.updateEnergy(newEnergy, pastEnergy).transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    case = int(receipt['logs'][0]['data'], 16)
    return case


def consumer(userAddress, energy):
    tx_hash = contract.functions.consumer(userAddress, energy).transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    energyReceiveFormThePull = int(receipt['logs'][0]['data'], 16)
    return energyReceiveFormThePull


def deposit(userAddress, energyToPay):
    contract.functions.deposit(1, abs(energyToPay) * 10000000000000000).transact({	'to': address,
                                                                               'from': userAddress,
                                                                               'value': abs(energyToPay) * 10000000000000000
                                                                               })


def prosumer(userAddress, energy):
    tx_hash = contract.functions.prosumer(userAddress, energy).transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    ethReceived = int(receipt['logs'][0]['data'], 16)
    return ethReceived

def deductProsumer():
    tx_hash = contract.functions.deductProsumer().transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
