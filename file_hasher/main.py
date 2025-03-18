#importing sys for getting commandline args
#importing for getting sha256 hash function

import sys
import hashlib

print("<-------Welcome to your Ghaser: Your favorite Hashing Tool------->")

#prompts the user to provide file and also select hash type
file = input("Please provide a file: \n")
hash_type = input("Select hash type (type 'more' to learn about hash types): \n")

#provides more information to the user about all the various hash types
while hash_type == "more":
    print("""
Hashing Tool Quick Guide
🔹Tip: Use SHA - 256 or higher for cryptographic security.For passwords, use Argon2 instead of general hash functions.
    Supported Hash Types:
✅ MD5 (Message-Digest Algorithm 5)
🔹 Fast but Weak – 128-bit hash, widely used but highly vulnerable to collisions.
⚠️ Security Risk: Easily cracked with rainbow tables & brute-force attacks.

✅ SHA-1 (Secure Hash Algorithm 1)
🔹 Better than MD5, But Still Weak – 160-bit hash, used in legacy systems.
⚠️ Security Risk: Susceptible to collision attacks (e.g., SHAttered attack).

✅ SHA-256 (Secure Hash Algorithm 256)
🔹 Modern Standard – 256-bit hash, widely used in cryptography & blockchain.
⚠️ Security Risk: Strong but slower; quantum attacks could weaken it in the future.

✅ SHA-512 (Secure Hash Algorithm 512)
🔹 High Security & Performance – 512-bit hash, more secure than SHA-256.
⚠️ Security Risk: Larger hash means higher storage & computational costs.

✅ BLAKE2
🔹 Faster & Secure Alternative to SHA-2 – Efficient hashing with strong resistance to attacks.
⚠️ Security Risk: Newer algorithm; adoption is still growing.

✅ SHA-3 (Keccak-based)
🔹 Next-Gen Cryptographic Hash – Resistant to length extension & collision attacks.
⚠️ Security Risk: Slower adoption compared to SHA-2; less optimized in hardware.

✅ RIPEMD-160
🔹 Legacy Hash for Bitcoin & PGP – 160-bit hash, alternative to SHA-1.
⚠️ Security Risk: Not recommended for new projects due to security concerns.

✅ Argon2 (For Password Hashing)
🔹 Resistant to Brute-force Attacks – Memory-hard function, ideal for password security.
⚠️ Security Risk: Slower than general-purpose hashing, but great for security.
""")
    hash_type = input("Select hash type (type 'more' to learn about hash types): \n")

#function creates the hash

def createhash(file, hash_type):

    #initializing the hash method
    hash = hashlib.new(hash_type)

    #reading the file
    with open(file, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break

            #passing the file into the hash function
            hash.update(data)

    #returns hash in hexadecimal format
    return hash.hexdigest()

#prints the final hash
print(f"Hash:{createhash(file,hash_type)}")