from hashstate import openssl_sha512

h1 = openssl_sha512()
h2 = openssl_sha512()
print(h1.serialize() == h2.serialize())

h1.update(b'abc')
print(h1.serialize() != h2.serialize())

h2.deserialize(h1.serialize())
print(h1.serialize() == h2.serialize())
print(h1.digest() == h2.digest())
