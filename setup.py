from setuptools import setup, Extension

with open('README.md') as f:
    readme = f.read()

c_ext = Extension(
    'hashstate._hashstate',
    sources=['hashstate/_hashstate.c'],
    libraries=['ssl']
)

setup(
    name='hashstate',
    version='0.2.1',
    description='Serializable hash objects',
    url='https://github.com/zachmullen/hashstate',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=['hashstate'],
    ext_modules=[c_ext],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
