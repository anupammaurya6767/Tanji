# Tanji Encryption Library 👩‍💻🔐

Tanji is a Python encryption library that provides a secure and flexible solution for encrypting and decrypting messages. It leverages both symmetric and asymmetric encryption techniques to ensure the confidentiality and integrity of your data.

## Features 🚀

- **Symmetric Encryption:** Utilizes the Advanced Encryption Standard (AES) algorithm for symmetric key encryption.
- **Asymmetric Encryption:** Employs RSA algorithm for secure asymmetric key encryption.
- **Base64 Encoding:** Efficiently encodes encrypted data using Base64 for safe transmission.
- **Key Pair Generation:** Automatically generates RSA key pairs for secure communication.
- **Random Initialization Vectors (IV):** Uses random IVs to enhance security.
- **Ease of Use:** Simple and straightforward interface for encrypting and decrypting messages.

## How Tanji Differs 🤔

- **Robust Security:** Tanji prioritizes the security of your data by combining symmetric and asymmetric encryption methods.
- **Key Pair Generation:** Automatically generates and manages RSA key pairs, simplifying the encryption process.
- **Dynamic Initialization Vectors:** Randomly generated IVs for each encryption enhance the resistance against cryptographic attacks.
- **Base64 Encoding:** Encoded data ensures compatibility and safe transmission across different systems.
- **Developer-Friendly:** Designed to be user-friendly and easily integrated into various Python projects.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🚀 Proud to present Tanji, a Python encryption package!<a href="https://t.co/T4e4kTNM8n">https://t.co/T4e4kTNM8n</a><br><br> <a href="https://twitter.com/hashtag/Tanji?src=hash&amp;ref_src=twsrc%5Etfw">#Tanji</a> <a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> <a href="https://twitter.com/hashtag/Encryption?src=hash&amp;ref_src=twsrc%5Etfw">#Encryption</a> <a href="https://twitter.com/hashtag/Cybersecurity?src=hash&amp;ref_src=twsrc%5Etfw">#Cybersecurity</a> <a href="https://twitter.com/hashtag/OpenSource?src=hash&amp;ref_src=twsrc%5Etfw">#OpenSource</a> <a href="https://twitter.com/hashtag/DataSecurity?src=hash&amp;ref_src=twsrc%5Etfw">#DataSecurity</a> <a href="https://twitter.com/hashtag/InfoSec?src=hash&amp;ref_src=twsrc%5Etfw">#InfoSec</a> <a href="https://twitter.com/hashtag/Programming?src=hash&amp;ref_src=twsrc%5Etfw">#Programming</a> <a href="https://twitter.com/hashtag/PrivacyFirst?src=hash&amp;ref_src=twsrc%5Etfw">#PrivacyFirst</a> <a href="https://twitter.com/hashtag/DeveloperTools?src=hash&amp;ref_src=twsrc%5Etfw">#DeveloperTools</a> <a href="https://twitter.com/hashtag/TechInnovation?src=hash&amp;ref_src=twsrc%5Etfw">#TechInnovation</a> <a href="https://twitter.com/hashtag/CodeSecurity?src=hash&amp;ref_src=twsrc%5Etfw">#CodeSecurity</a> <a href="https://twitter.com/hashtag/DataIntegrity?src=hash&amp;ref_src=twsrc%5Etfw">#DataIntegrity</a> <a href="https://twitter.com/hashtag/SecureCoding?src=hash&amp;ref_src=twsrc%5Etfw">#SecureCoding</a> <a href="https://twitter.com/hashtag/PythonLibrary?src=hash&amp;ref_src=twsrc%5Etfw">#PythonLibrary</a></p>&mdash; Anupam Maurya (@anupammaurya981) <a href="https://twitter.com/anupammaurya981/status/1731865225308078434?ref_src=twsrc%5Etfw">December 5, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Getting Started 🏁

1. Install Tanji:

    ```bash
    pip install tanji
    ```

2. Use Tanji in your Python project:

    ```python
    from tanji.tanji import Tanji

    # Example Usage
    tanji = Tanji()
    encrypted_message, ciphertext = tanji.encrypt_message("Hello, Tanji!")
    decrypted_message = tanji.decrypt_message(encrypted_message, ciphertext)

    print("Original Message:", "Hello, Tanji!")
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)
    ```

## Contributing 🤝

Contributions are welcome! Feel free to submit issues or pull requests.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
