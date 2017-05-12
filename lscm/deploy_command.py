import web3
import json

public_provider = web3.HTTPProvider('http://localhost:8200')
public_web3 = web3.Web3(public_provider)
public_psn = web3.personal.Personal(public_web3)

contract_abi = json.load(open('/home/gethuser/last/lscm/build/EchequeSystem.abi'))
contract_bin = open('/home/gethuser/last/lscm/build/EchequeSystem.bin').readline()

contract = public_web3.eth.contract(abi=contract_abi, bytecode=contract_bin)

public_psn.unlockAccount(public_web3.eth.accounts[0],"123456",1000)

trans_hash = contract.deploy(args=(public_web3.eth.accounts[0],'HSBC','HKD'))
print trans_hash

#After the transaction is mined:
'''
contract_address = public_web3.eth.getTransactionReceipt(trans_hash)['contractAddress']
print contract_address
contract = public_web3.eth.contract(abi=contract_abi, address=contract_address)

'''
