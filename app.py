import  json
from web3 import Web3

infura_url = "https://ropsten.infura.io/v3/6cc62c163d4c4dc4bc3aa7ca866b8866"
web3 = Web3(Web3.HTTPProvider(infura_url))


abi = json.loads('give the abi of your contract')
address = "give the address of your contract"

contract = web3.eth.contract(address=address, abi=abi)
print(contract)
totalSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())
balance = contract.functions.balanceOf('give the address of the account whom you want check the balance').call()
print(web3.fromWei(balance, 'ether'))
