//SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

//just a comment

contract FundMe{
    mapping (address => uint256) public addressToAmountFunded;
    // get the owner immediately ths copntact gets ccalled using constructor
    address[] public funders;
    address public owner;
    //#globalise so  ganache can get price of ether
    AggregatorV3Interface public priceFeed;
    constructor(address _priceFeed) public{
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }
    function fund () public payable{
        //$50 converting it into gwei
        uint256 minimumUSD = 50 * 10 ** 18;
        //1gwei < $50
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }
    function getVersion() public view returns(uint256){
        return priceFeed.version();

    }
    function getPrice() public view returns(uint256){
        (uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    )=priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }   
    function getConversionRate(uint256 ethAmount) public view returns(uint256 ) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice *  ethAmount)/1000000000000000000;
        return ethAmountInUsd;
    }
    //modifier are used tochange the behaviour of the fun in a declarative way
    modifier onlyOwner {
    	//is the message sender owner of the contract?
        require(msg.sender == owner);
        
        _;
    }
    function withdraw()  payable onlyOwner public {
        
        payable(msg.sender).transfer(address (this).balance);
        for(uint256 funderIndex=0;funderIndex<funders.length;funderIndex++){
            address funder =funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}