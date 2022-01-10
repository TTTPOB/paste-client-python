from nacl.public import PrivateKey, PublicKey
from nacl.encoding import HexEncoder


def generate_new_keypair():
    key_pair = PrivateKey.generate()
    return key_pair
