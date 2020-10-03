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


def updateEnergy(newEnergy, pastEnergy):
    return contractControllers.updateEnergy(newEnergy, pastEnergy)


def transaction(userAddress, case, energy):
    # Wait for everyone to upload their respective values in the smart contract
    time.sleep(5)
    if(case == 1):
        print('Consumer Case')
        stop = 0
        while stop == 0:
            energyReceive = contractControllers.consumer(userAddress, energy)
            if(energyReceive == 0):
                stop = 1
                print('There is no Available energy in the system.')
                break
            if(energyReceive >= energy):
                print('Energy receive from the pull: ' + str(energyReceive) + 'kW')
                contractControllers.deposit(userAddress, energyReceive)
                stop = 1
            else:
                print('Energy receive from the pull ' + str(energyReceive) +
                      '.\nYou are know waiting to see if there is any available energy left in the pull.')
                contractControllers.deposit(userAddress, energyReceive)
                time.sleep(2)

    if(case == 2):
        print('Prosumer Case')
        if(contractControllers.getDemandEnergy() != 0):
            time.sleep(4)
            if (contractControllers.getConsumedEnergy() > 0):
                while (contractControllers.getNumberConsumer() != 0):
                    print('Wait till the end of energy allocation to consumer.')
                ethReceived = contractControllers.prosumer(userAddress, energy)
                print('You receive ' + str(ethReceived) + ' wei.')
            else:
                contractControllers.deductProsumer()
                print('There is no Consumed energy in the system.')
        else:
            contractControllers.deductProsumer()
            print('There is no Demand in the system.')

    print('_________________________________________')
