import sys
sys.path.insert(1, '../')

import time
import requests
from contract.smart_contract_details.contractInfo import contract, address, web3
import contract.smart_contract_controllers.contractControllers as contractControllers


def getValueFromEmonPi():
    # to connect to the API for getting emoncms values:
    APIKEY = '5a8fc3b42672113c669318f6a0356cc6'
    url = 'https://emoncms.org/feed/timevalue.json?id=369266&apikey=5a8fc3b42672113c669318f6a0356cc6'
    # request value
    inc_value = requests.get(
        url, headers={'Authorization': 'Bearer 5a8fc3b42672113c669318f6a0356cc6'})
    # return the value
    return inc_value.json()


def prosumerOrConsumer(energy):
    if (energy < 0):
        return 1
    if (energy >= 0):
        return 2


def updateEnergy(newEnergy, pastEnergy):
    tx_hash = contract.functions.updateEnergy(newEnergy, pastEnergy).transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    case = int(receipt['logs'][0]['data'], 16)
    return case


def transaction(userAddress, case, energy):
    time.sleep(5)
    if(case == 1):
        print('_________________________________________')
        print('Consumer Case')
        stop = 0
        while stop == 0:
            tx_hash = contract.functions.consumer(
                userAddress, energy).transact()
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
            # print(receipt['logs'][0]['data'])
            energyReceive = int(receipt['logs'][0]['data'], 16)
            print('Energy receive from the pull ' + str(energyReceive))
            if(energyReceive == 0):
                stop = 1
                print('There is no available energy.')
                break
            if(energyReceive >= energy):
                contract.functions.deposit(1, abs(energyReceive) * 1000000000000).transact({	'to': address,
                                                                                             'from': userAddress,
                                                                                             'value': abs(energyReceive) * 1000000000000
                                                                                             })
                stop = 1
            else:
                time.sleep(3)

    if(case == 2):
        print('_________________________________________')
        print('Prosumer Case')
        if(contractControllers.getNumberConsumer() != 0):
            time.sleep(5)
        if (contractControllers.getConsumedEnergy() > 0):
            if (contractControllers.getNumberConsumer() != 0):
                while (contractControllers.getNumberConsumer() != 0):
                    print('Wait till the end of energy allocation to consumer.')
            tx_hash = contract.functions.prosumer(
                userAddress, energy).transact()
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
            print(int(receipt['logs'][0]['data'], 16))
        else:
            tx_hash = contract.functions.deductProsumer().transact()
            receipt = web3.eth.waitForTransactionReceipt(tx_hash)
