import time
from contractInfo import contract, address
import pprint

from contractInfo import web3

def prosumerOrConsumer(energy):
    if (energy < 0):
        return 1;
    if (energy >= 0):
        return 2;

# functions:
# get the available energy from the contract:

def getConsumedEnergy():
    return contract.functions.getConsumedEnergy().call()

def getMaxBalanceForThisCycle():
    return contract.functions.getMaxBalanceForThisCycle().call()

def numberOfParticipant():
    print('| Number of consumer: ' + str(contract.functions.getNumberConsumer().call()))
    print('| Number of prosumer: ' + str(contract.functions.getNumberProsumer().call()))

def getNumberConsumer():
    return contract.functions.getNumberConsumer().call()

def getAvailableEnergy():
    return contract.functions.getAvailableEnergy().call()

# get the demand energy from the contract:


def getDemandEnergy():
    return contract.functions.getDemandEnergy().call()

# print smart contract balance:


def getContractBalance():
    return contract.functions.getBalance().call()

# TODO: function reset.


# get the value monitored by the emonPi:
import requests
# get value from emoncms api


def getValueFromEmonPi():
    # to connect to the API for getting emoncms values:
    APIKEY = '5a8fc3b42672113c669318f6a0356cc6'
    url = 'https://emoncms.org/feed/timevalue.json?id=370268&apikey=5a8fc3b42672113c669318f6a0356cc6'
    # request value
    inc_value = requests.get(
        url, headers={'Authorization': 'Bearer 5a8fc3b42672113c669318f6a0356cc6'})
    # return the value
    return inc_value.json()


def updateEnergy(newEnergy, pastEnergy):
    tx_hash = contract.functions.updateEnergy(newEnergy, pastEnergy).transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    case = int(receipt['logs'][0]['data'],16)
    return case

def transaction(userAddress, case, energy):
    time.sleep(5)
    if(case == 1):
        print('_________________________________________')
        print('Consumer Case')
        stop = 0;
        while stop == 0:
            tx_hash = contract.functions.consumer(userAddress, energy).transact()
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
            #print(receipt['logs'][0]['data'])
            energyReceive = int(receipt['logs'][0]['data'],16)
            print('Energy receive from the pull '+str(energyReceive))
            if(energyReceive == 0):
                stop = 1
                print('There is no available energy.')
                break
            if(energyReceive >= energy):
                contract.functions.deposit(1, abs(energyReceive)*1000000000000).transact({	'to': address,
                                                                                    'from': userAddress,
                                                                                    'value': abs(energyReceive)*1000000000000
                                                                                })
                stop = 1
            else:
                time.sleep(3)

    if(case == 2):
        print('_________________________________________')
        print('Prosumer Case')
        if(getNumberConsumer() != 0):
            time.sleep(5)
        if (getConsumedEnergy() > 0):
            if (getNumberConsumer() != 0):
                while (getNumberConsumer() != 0):
                    print('Wait till the end of energy allocation to consumer.');
            tx_hash = contract.functions.prosumer(userAddress, energy).transact()
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
            print(int(receipt['logs'][0]['data'],16))
        else:
            tx_hash = contract.functions.deductProsumer().transact()
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
