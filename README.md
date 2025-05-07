````markdown
# Cryptolib: Python Cryptography Library

Welcome to **Cryptolib**, a lightweight and efficient Python cryptography library that implements several popular encryption and decryption algorithms. Whether you're a beginner or an expert in cryptography, **Cryptolib** is designed to make cryptography easy and accessible with minimal dependencies.

---

## 🛠️ Features

- **Caesar Cipher**: A simple substitution cipher where each letter of the plaintext is shifted by a fixed number of positions in the alphabet.
- **Vigenère Cipher**: A more advanced encryption method that uses a keyword to shift the letters of the plaintext.
- **Substitution Cipher**: Encrypts text by substituting each letter of the plaintext with another letter.

---

## 📦 Installation

You can install the library with the following pip command:

```bash
pip install git+https://github.com/ErfanNahidi/cryptography-algorithms-python.git
````

Alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/ErfanNahidi/cryptography-algorithms-python.git
cd cryptography-algorithms-python
pip install .
```

---

## 🧑‍💻 Usage

The library supports the following encryption and decryption algorithms:

### Caesar Cipher

**Encryption**:

```python
from cryptolib.encrypt import Caesar

plain_text = "Hello World"
key = 3
cipher_text = Caesar(plain_text, key)
print(f"Encrypted: {cipher_text}")
```

**Decryption**:

```python
from cryptolib.decrypt import Caesar

cipher_text = "Khoor Zruog"
key = 3
plain_text = Caesar(cipher_text, key)
print(f"Decrypted: {plain_text}")
```

### Vigenère Cipher

**Encryption**:

```python
from cryptolib.encrypt import Vigenere

plain_text = "Hello World"
key = "key"
cipher_text = Vigenere(plain_text, key)
print(f"Encrypted: {cipher_text}")
```

**Decryption**:

```python
from cryptolib.decrypt import Vigenere

cipher_text = "Ripxe Sjbiu"
key = "key"
plain_text = Vigenere(cipher_text, key)
print(f"Decrypted: {plain_text}")
```

---

## 🔧 Algorithms Implemented

* **Caesar Cipher**: One of the simplest and oldest ciphers, where each letter is shifted by a fixed amount.
* **Vigenère Cipher**: A more secure cipher using a repeating key for encryption, offering better security than Caesar.
* **Substitution Cipher**: Substitutes each letter of the plaintext with another letter or symbol based on a fixed system.

---

## 📂 Project Structure

```plaintext
cryptolib/
│
├── cryptolib/
│   ├── __init__.py
│   ├── core.py         # Helper functions
│   ├── encrypt.py      # Encryption algorithms
│   ├── decrypt.py      # Decryption algorithms
│
├── tests/
│   ├── __init__.py     # Tests for encryption and decryption
│   ├── test_algorithms.py
│
├── README.md           # Project documentation
├── setup.py            # Package setup for distribution
├── requirements.txt    # Dependency management (empty for now)
└── LICENSE             # MIT License
```

---

## 📋 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🚀 Contributing

We welcome contributions! If you have suggestions, improvements, or bug fixes, please open an issue or create a pull request. Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

---

## 🤝 Acknowledgements

* Thanks to the open-source community for providing great resources and learning materials.
* This project serves as a personal learning tool to better understand cryptographic principles and their implementation in Python.

---

## 📞 Contact

For any questions or suggestions, feel free to reach out:

* Email: [erfannahidi20@gmail.com]
* GitHub: [https://github.com/ErfanNahidi]

```