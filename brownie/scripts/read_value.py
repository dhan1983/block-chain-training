from brownie import SimpleStorage, accounts , config

def read_contracts():
    # most recent deploy is -1
    print(SimpleStorage[-1])
    # go take the index thats one less than the length
    #ABI
    #address
    

def main():
    read_contracts()