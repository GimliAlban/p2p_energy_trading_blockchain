import sys
sys.path.insert(1, '../../')

from contract.smart_contract_details.contractInfo import web3
import contract.smart_contract_controllers.contractControllers as contractControllers
import users.usersControllers as usersControllers

#Select the account number for the Ganache blockchain:
web3.eth.defaultAccount = web3.eth.accounts[1]

pastEnergy=usersControllers.getValueFromEmonPi()
pastEnergy['value'] = contractControllers.getAvailableEnergy()

while True:
	newEnergy = usersControllers.getValueFromEmonPi()
	if(newEnergy['time'] !=  pastEnergy['time']):
		newEnergy['value'] = int(float(newEnergy['value'])*1000)
		case = usersControllers.updateEnergy(newEnergy['value'], pastEnergy['value'])
		usersControllers.transaction(web3.eth.defaultAccount, case, newEnergy['value'])
		pastEnergy = newEnergy
		## TODO: input enter to stop the loop
