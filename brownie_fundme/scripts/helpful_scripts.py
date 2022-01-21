from brownie import network,config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]

def get_account():
    if (network.show_active()) in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0] 
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"the active n/w is {network.show_active()}")
    print("deploying mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000,"ether"), {"from":get_account()} )
        print("mock aggregatory deployed")