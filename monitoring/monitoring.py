import sys
sys.path.insert(1, '../')

import time
from contract.smart_contract_details.contractInfo import web3
import contract.smart_contract_controllers.contractControllers as contractControllers
import users.usersControllers as usersControllers

# Select the account number for the Ganache blockchain:
web3.eth.defaultAccount = web3.eth.accounts[0]

while True:
    # contract.functions.priceEnergy().transact()
    time.sleep(3)
    print('| Number of Prosumer in the cycle: ' +
          str(contractControllers.getNumberProsumer()))
    print('| Number of Consumer in the cycle: ' +
          str(contractControllers.getNumberConsumer()))
    print('| Available energy in the system: ' +
          str(contractControllers.getAvailableEnergy()))
    print('| Demand energy in the system: ' +
          str(contractControllers.getDemandEnergy()))
    print('| Consumed Energy: ' + str(contractControllers.getConsumedEnergy()))
    print('| Max Balance Cycle: ' +
          str(contractControllers.getMaxBalanceForThisCycle()))
    print('| Smart contract balance: ' +
          str(contractControllers.getContractBalance()))
    print('|_________________________________________')
