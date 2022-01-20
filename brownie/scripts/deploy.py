from brownie import accounts, config, SimpleStorage,network
import os

def deploy_simple_storage():
    #method 1 directly get account from ganache cli
    account1 = get_account()
    print(account1)
    #method 2 freecode camp account kovan acct from meta mask using cmd "brownie accounts new freecodecamp-account"
    #account2 = accounts.load("freecodecamp-account")
    #print (account2)
    #methhod 3 safely secure private key not stored in git. never put wallets with actual money as env variables
    # put private kay in .env and create brownie-config.yaml with its contents
    #account3= accounts.add(os.getenv("G_PRIV_KEY"))
    #methhod 4 using wallets in brownie-config
    #account = accounts.add(config["wallets"]["from_key"])
    #print(account)
    #var= os.getenv("OTHER_Variable")
    #print(account3)
    #print(var)
    simple_storage = SimpleStorage.deploy({"from": account1})
    #print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15,{"from": account1})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    if (network.show_active()) == "development":
        return accounts[0] 
    else:
        return accounts.add(config["wallets"]["from_key"])



def main():
    deploy_simple_storage()