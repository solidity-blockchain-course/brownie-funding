from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpers import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    print(f"using account: {account.address}")
    print(f"with balance: {account.balance()}")
    # pass the aggregator feed address

    # if we are on persistent network, use the address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account, "gas_price": 10 ** 13},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    print(f"balance left {account.balance()}")
    return fund_me


def main():
    deploy_fund_me()
