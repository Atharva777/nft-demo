from scripts.helpful_scripts import get_account, SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
opensea_url = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! you can now view your NFT at {opensea_url.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}"
    )
    return simple_collectible


def main():
    deploy_and_create()
