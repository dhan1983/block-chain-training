from solcx import compile_standard,install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv
load_dotenv()
with open("./SimpleStorage.sol", "r" ) as file:
    simple_storage_file = file.read()
#compile our solidity 
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language":"Solidity",
        "sources":{"SimpleStorage.sol":{"content":simple_storage_file}},
        "settings": {
            "outputSelection":{
                "*": {"*":["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        }
    },
    solc_version="0.6.0",

)   
with open ("compile_code.json", "w") as file:
    json.dump(compiled_sol,file)  

# get bytecode
bytecode = compiled_sol  ["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
#get abi
abi = compiled_sol  ["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
#connect to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x055587b1EE5C96DFFadDceaC517769E8De276D5f"
private_key="0xc8ecbd5a19c538ad705146428cad6e24a6fbd8fbc6a7672125b8b02c26bdbb47"
SimpleStorage = w3.eth.contract(abi=abi , bytecode=bytecode)
print(SimpleStorage) 
#build a transaction 3 steps 1) build 2) sign 3) send the transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
transaction = SimpleStorage.constructor().buildTransaction(
    {"gasPrice": w3.eth.gas_price,"chainId": chain_id,"from": my_address,"nonce":nonce}
)
#print(transaction)
private_key = os.getenv("G_PRIV_KEY")
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("deploying intital contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt= w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!!!")
# to work with a contract you need contract ABI and contract Address
simpe_storage= w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
# to interact with bc u ca do a call or transact but Transact will make a state change
# this is like blue button in remix
print(simpe_storage.functions.retrieve().call()) 

print("Updating contract ...")
store_transaction = simpe_storage.functions.store(15).buildTransaction(
    # we need to have a differnet nonce from what we used to deploy contract
    {"gasPrice": w3.eth.gas_price,"chainId": chain_id,"from": my_address,"nonce":nonce +1}
)
signed_store_txn= w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
#deploy contract
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
txn_receipt= w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")
print(simpe_storage.functions.retrieve().call()) 

 

