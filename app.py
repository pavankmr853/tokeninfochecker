from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x09566dEFBD91D9C218c40bD89Dd04eC5C20b6cab"
account_2 = "0x19081D4665879E49F408A1d386Df9215F3C337d2"

private_key = "af63980c120dcc88b316c39b5b572916a388eb844cf63834b14283e5b28c64cd"


nonce = web3.eth.getTransactionCount(account_1)

tx = {
'nonce': nonce,
'to': account_2,
'value': web3.toWei(1, 'ether'),
'gas': 2000000,
'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))
