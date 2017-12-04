import binascii

import mnemonic
import base58


ashex = lambda b: binascii.hexlify(seed).decode('ascii')

ENGLISH = set([w.strip() for w in open("wordlist.txt").readlines()])

recovery = input("Enter the first 23 words of your recovery phrase:\n")
words = [w.strip() for w in recovery.split(" ")]

if len(words) != 23:
    raise ValueError("It contains {} words instead of 23".format(len(words)))

unknowns = set(words) - ENGLISH
if len(unknowns) > 0:
    raise ValueError("{} not in wordlist".format(unknowns))

print()

passphrases = []
m = mnemonic.Mnemonic('english')
for word in ENGLISH:
    full = recovery + ' ' + word
    if m.check(full):
        print("\t{}: {}".format(len(passphrases), full))
        passphrases.append(full)

nstr = input("Which one is yours:\n")
n = int(nstr)
passphrase = passphrases[n]

seed = mnemonic.Mnemonic.to_seed(passphrase)
print("BIP39 seed: {}".format(ashex(seed)))
