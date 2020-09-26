from contractInfo import web3
from contractInfo import contract

from functions_file import getValueFromEmonPi, getAvailableEnergy, updateEnergy, transaction

#Select the account number for the Ganache blockchain:
web3.eth.defaultAccount = web3.eth.accounts[1]

pastEnergy=getValueFromEmonPi()
pastEnergy['value'] = getAvailableEnergy()

while True:
	newEnergy = getValueFromEmonPi()
	if(newEnergy['time'] !=  pastEnergy['time']):
		newEnergy['value'] = int(float(newEnergy['value'])*1000)
		case = updateEnergy(newEnergy['value'], pastEnergy['value'])
		transaction(web3.eth.defaultAccount, case, newEnergy['value'])
		pastEnergy = newEnergy
		## TODO: input enter to stop the loop
