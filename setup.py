from setuptools import setup, find_packages

setup(
    name='cryptolib',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    description='A simple cryptography library with encryption and decryption algorithms',
    author='Erfan Nahidi',
    author_email='Erfannahidi20@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
