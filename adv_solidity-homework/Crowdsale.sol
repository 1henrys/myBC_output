pragma solidity ^0.5.0;

import "./PupperCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";

contract PupperCoinCrowdsale is Crowdsale, MintedCrowdsale, TimedCrowdsale, RefundableCrowdsale {

    constructor(
        uint rate, // rate in TKNbits
        address payable wallet, // sale beneficiary
        PupperCoin token,
        uint goal,
        uint openingTime,
        uint closingTime
    )
        RefundableCrowdsale(goal)
        TimedCrowdsale(openingTime,closingTime)
        MintedCrowdsale()
        Crowdsale(rate,wallet,token) public {
        // constructor can stay empty
        }
}

contract PupperCoinSaleDeployer {
    address public token_sale_address;
    address public token_address;
//    uint256 constant goal = 30000000000000000000;
    uint256 constant goal = 100000000000000000;

    uint openingTime = now;
    uint closingTime = now + 24 weeks;

    function timeWarp() public {
        closingTime = now + 5 minutes;
    }

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    ) public {
        // create the PupperCoin and keep its address handy
        PupperCoin token = new PupperCoin(name, symbol, 0);
        token_address = address(token);
        // create PupperCoinSale, tell it about token, set goal, set open/close times to now / now + 24 weeks.
        PupperCoinCrowdsale pupper_sale = new PupperCoinCrowdsale(1,wallet,token,goal,openingTime,closingTime);
        token_sale_address = address(pupper_sale);

        // make PupperCoinSale contract a minter, then PupperCoinSaleDeployer renounce its minter role
        token.addMinter(token_sale_address);
        token.renounceMinter();
    }
}
