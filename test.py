import string

temp  = list([(int(encrypt((ord(letter) - 96), e, n))) for letter in string.ascii_lowercase])
print(list([(ord(letter) - 96) for letter in string.ascii_lowercase]))
print(temp)
print(list([(int(decrypt(letter,privateKey,n))) for letter in temp]))