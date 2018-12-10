import hashstate
import pytest

ALGS = {'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'}


@pytest.mark.parametrize('alg', ALGS)
def test_serialization(alg):
    ctor = getattr(hashstate, 'openssl_' + alg)
    h1 = ctor()
    h2 = ctor()
    assert h1.serialize() == h2.serialize()
    h1.update(b'abc')
    h2.update(b'abc')
    assert h1.serialize() == h2.serialize()

    h1.update(b'hello')
    assert h1.serialize() != h2.serialize()

    h2.deserialize(h1.serialize())
    assert h1.digest() == h2.digest()

    h1.update(b'foo')
    h2.update(b'foo')
    assert h1.digest() == h2.digest()
