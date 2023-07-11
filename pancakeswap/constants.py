MODULES_ACCOUNT = "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa"
RESOURCES_ACCOUNT = "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa"

COIN_INFO = "0x1::coin::CoinInfo"
COIN_STORE = "0x1::coin::CoinStore"

NETWORKS_MODULES = {
    "Scripts": f"{MODULES_ACCOUNT}::router",
    "ResourceType": f"{MODULES_ACCOUNT}::swap"
}

FEE_PCT = 3
FEE_SCALE = 1000
