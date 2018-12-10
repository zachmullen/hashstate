from distutils.core import setup, Extension

c_ext = Extension(
    'hashstate',
    sources=['hashstate.c'],
    include_dirs=['/usr/local/opt/openssl/include'],
    library_dirs=['/usr/local/opt/openssl/lib'],
    libraries=['ssl']
)

setup(
    name='hashstate',
    version='1.0',
    description='Serialize hash objects',
    ext_modules=[c_ext]
)
