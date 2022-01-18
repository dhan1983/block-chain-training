//SPDX-License_Identifier: MIT
pragma solidity ^0.6.0;
import "./SimpleStorage.sol";
// is keyword is used for contract inheritance 
contract StorageFactory is SimpleStorage {

    SimpleStorage[] public simpleStorageArray;
    function createSimpleStorageContract() public{
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    
    }
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        //Below two things needed to call another contract fn
        //Address
        //ABI
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
        
    }
    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256){
        //Below two things needed to call another contract fn
        //Address
        //ABI
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrieve();
        
    }
}