from solcx import compile_standard,install_solc
import json
from web3 import Web3
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
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
chain_id = 1337
my_address = ""
private_key=""
SimpleStorage = w3.eth.contract(abi=abi , bytecode=bytecode)
print(SimpleStorage) 
#build a transaction 3 steps 1) build 2) sign 3) send the transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id,"from": my_address,"nonce":nonce}
)
print(transaction)

 

