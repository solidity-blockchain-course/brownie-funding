from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():

    # customAccount = accounts.load("new-account")
    # accountFromEnv = accounts.add(os.getenv("PRIVATE_KEY"))
    # accountFromEnvBetter = accounts.add(config["wallets"]["from_key"])
    # print(accountFromEnvBetter)
    account = get_account()
    ss = SimpleStorage.deploy({"from": account})
    stored_value = ss.retrieve()
    print(stored_value)
    transaction = ss.store(15, {"from": account})
    transaction.wait(1)  # wait 1 block confirmation
    updated_stored_value = ss.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
