import os
import random
import sys
from typing import Tuple

from . import cryptomath_module as cryptoMath
from . import rabin_miller as rabinMiller


def main():
    print("Making key files...")
    makeKeyFiles("rsa", 1024)
    print("Key files generation successful.")


def generateKey(keySize: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    print("Generating prime p...")
    p = rabinMiller.generateLargePrime(keySize)
    print("Generating prime q...")
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    print("Generating e that is relatively prime to (p - 1) * (q - 1)...")
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print("Calculating d that is mod inverse of e...")
    d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)


def makeKeyFiles(name: int, keySize: int) -> None:
    if os.path.exists("%s_pubkey.txt" % (name)) or os.path.exists(
        "%s_privkey.txt" % (name)
    ):
        print("\nWARNING:")
        print(
            '"%s_pubkey.txt" or "%s_privkey.txt" already exists. \n'
            "Use a different name or delete these files and re-run this program."
            % (name, name)
        )
        sys.exit()

    publicKey, privateKey = generateKey(keySize)
    print("\nWriting public key to file %s_pubkey.txt..." % name)
    with open("%s_pubkey.txt" % name, "w") as out_file:
        out_file.write("{},{},{}".format(keySize, publicKey[0], publicKey[1]))

    print("Writing private key to file %s_privkey.txt..." % name)
    with open("%s_privkey.txt" % name, "w") as out_file:
        out_file.write("{},{},{}".format(keySize, privateKey[0], privateKey[1]))


if __name__ == "__main__":
    main()
