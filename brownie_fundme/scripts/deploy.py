from brownie import FundMe,network,config,MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import os

def deploy_fundme():
    
    account1 = get_account()
    #the publish_source flag is used to publish everything in the cotract to kovan etherium so you can
    # see the read and write(payable functions in the web)  . for this u need to import the api key from 
    # eth io and export itin .env . when u publish contract the import stmt expands code that is flatening.
    #if we are on a n/w like kovan then use the associated address else deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        #after setting ganache as ethereum local env it will be not be considered as dev env so make the above change
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account1},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    

def main():
    deploy_fundme()