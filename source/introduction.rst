Introduction
============

Welcome to the Tanji project, a Python package for handling symmetric and asymmetric encryption. 

This package provides a simple and straightforward way to encrypt and decrypt messages using a combination of symmetric (AES) and asymmetric (RSA) encryption.

Example
-------

Here is a simple example of how to use the Tanji package:

.. code-block:: python

    from tanji.tanji import Tanji

    # Create a Tanji instance
    tanji = Tanji()

    # Generate a key pair
    tanji.generate_key_pair()

    # Encrypt a message
    encrypted_message, ciphertext = tanji.encrypt_message("Hello, Tanji!")

    # Decrypt the message
    decrypted_message = tanji.decrypt_message(encrypted_message, ciphertext)

    # The decrypted_message should now be "Hello, Tanji!"