pragma solidity ^0.5.0;
// lvl 1: equal split

contract AssociateProfitSplitter {

    // Three payable addresses representing `employee_one`, `employee_two` and `employee_three`.
    address payable employee_one;
    address payable employee_two;
    address payable employee_three;
    
    constructor(address payable _one, address payable _two, address payable _three)
    public {
        employee_one = _one;
        employee_two = _two;
        employee_three = _three;
    }
    
    function balance() public view returns(uint) {
        return address(this).balance;
        }
    
    function deposit() public payable {
        // Split `msg.value` into three
        uint amount = msg.value / 3;
    
        // Transfer amount to each employee
        employee_one.transfer(amount);
        employee_two.transfer(amount);
        employee_three.transfer(amount);
    
        // Send back any remainder to HR (`msg.sender`)
        msg.sender.transfer(msg.value - (amount*3));
    }
    
    function() external payable {
        // Enforce that the `deposit` function is called in the fallback function!
        deposit();
    }
}