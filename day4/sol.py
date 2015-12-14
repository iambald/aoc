import hashlib

num = 0
while (hashlib.md5("bgvyzdsv" + str(num)).hexdigest().startswith('00000') == False):
    num += 1

print num
