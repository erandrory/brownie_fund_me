from brownie import network, accounts, config, MockV3Aggregator


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        print("fake accounts")
        return accounts[0]
    else:
        print("Real accounts")
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks Deployed")
