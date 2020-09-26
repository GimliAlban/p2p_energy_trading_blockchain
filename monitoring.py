import functions_file
import time
from contractInfo import web3

#Select the account number for the Ganache blockchain:
web3.eth.defaultAccount = web3.eth.accounts[0]

while True:
    # contract.functions.priceEnergy().transact()
    newEnergy = functions_file.getValueFromEmonPi()
    time.sleep(3)
    functions_file.numberOfParticipant()
    print('| Read value from emongcms website: ' + str(newEnergy['value']))
    print('| Available energy in the system: ' +
          str(functions_file.getAvailableEnergy()))
    print('| Demand energy in the system: ' +
          str(functions_file.getDemandEnergy()))
    print('| Consumed Energy: ' + str(functions_file.getConsumedEnergy()))
    print('| Max Balance Cycle: ' + str(functions_file.getMaxBalanceForThisCycle()))
    print('| Smart contract balance: ' + str(functions_file.getContractBalance()))
    print('|_________________________________________')
    pastEnergy = newEnergy
