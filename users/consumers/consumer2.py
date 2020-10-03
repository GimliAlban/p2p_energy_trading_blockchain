import sys
sys.path.insert(1, '../../')

from contract.smart_contract_details.contractInfo import web3
import contract.smart_contract_controllers.contractControllers as contractControllers
import users.usersControllers as usersControllers
from time import gmtime, strftime, sleep

# Select the account number for the Ganache blockchain:
web3.eth.defaultAccount = web3.eth.accounts[4]

pastEnergy = 0

while True:
    newEnergy = -50  # read value from emonPi
    thisTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if(((thisTime[-1] == '0') and ((thisTime[-2] == ('0')))) or ((thisTime[-1] == '0') and ((thisTime[-2] == ('3'))))):
        print(thisTime)
        # newEnergy = -int(float(newEnergy) * 1000) used to convert the value read from th emonPi
        case = usersControllers.updateEnergy(newEnergy, pastEnergy)
        usersControllers.transaction(web3.eth.defaultAccount, case, newEnergy)
        pastEnergy = newEnergy
        sleep(1)
        # TODO: input enter to stop the loop
