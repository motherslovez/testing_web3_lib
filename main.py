from web3 import Web3
from eth_account import Account
from config import private_key


w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
burn_address = "0x0000000000000000000000000000000000000000"
private_key = private_key
acc = Account.from_key(private_key)


def burn_bnb(amount_to_burn, gwei):
    transaction = {
        'to': burn_address,
        'value': w3.to_wei(amount_to_burn, 'ether'),  # bnb token amount
        'gas': 2000000,  # Лимит газа для транзакции
        'gasPrice': w3.to_wei(str(gwei), 'gwei'),  # gas price in gwei
        'nonce': w3.eth.get_transaction_count(acc.address),
        'chainId': 56
    }

    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
