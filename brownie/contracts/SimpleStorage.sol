pragma solidity =0.6.0;

contract SimpleStorage {
    uint256 public favouriteNumber = 5;
    struct People {
        uint256 favNumber;
        string name;
    }
    People[] public people;

    function store(uint256 _favouriteNumber) public {
        favouriteNumber = _favouriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favouriteNumber;
    }

    function addPerson(string memory _name, uint256 _favNumber) public {
        people.push(People({favNumber: _favNumber, name: _name}));
    }
}
