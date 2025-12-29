from passlib.hash import sha256_crypt
crypto = sha256_crypt

plainPasswd = "sunbeam"
encPasswd = crypto.hash(plainPasswd)
print("Encrypted Passwd:", encPasswd)

rawPasswd = input("Enter passwd: ")
matched = crypto.verify(rawPasswd, encPasswd)
print("Is Matched:", matched)