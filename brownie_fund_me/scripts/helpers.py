from brownie import network, accounts, config, MockV3Aggregator

# creating custom mainnet-fork-dev
# brownie networks add development mainnet-fork-dev cmd=ganache-cli
# host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/{apiKey}
# accounts=10 mnemonic=brownie port=8545
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 2000 * 10 ** 8


def get_account():
    print(f"active: {network.show_active()}")
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"active network: {network.show_active()}")
    print("Deploying mocks ...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})

    print("Mocks deployed!")
