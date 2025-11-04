s = "Cyber"
print(s.encode())

print(b"Cyber".hex())
print(bytes.fromhex('4379626572'))


# XOR Trick (CTF Style)

msg = b'flag'
key = 0x42
print(bytes([b ^ key for b in msg]))

print("\n")

'''
Exercise:
XOR the bytes of b'secret' with the key 0x10 and observe the result.
'''

msg = b'secret'
key = 0x10
print(bytes([b ^ key for b in msg]))
