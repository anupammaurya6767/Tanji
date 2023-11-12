AsymmetricCipher Module
=======================

.. automodule:: asymmetric.asymmetric
   :members:
   :undoc-members:
   :show-inheritance:

.. class:: AsymmetricCipher

   A class for handling asymmetric encryption.

   .. method:: generate_key_pair()

      Generate a pair of private and public keys for RSA encryption.

      :return: The generated private and public keys.
      :rtype: tuple

   .. method:: rsa_encrypt(message, public_key)

      Encrypt a message using RSA encryption.

      :param message: The message to be encrypted.
      :type message: bytes
      :param public_key: The public key for RSA encryption.
      :type public_key: RSAPublicKey
      :return: The encrypted message.
      :rtype: bytes

   .. method:: rsa_decrypt(ciphertext, private_key)

      Decrypt a ciphertext message using RSA decryption.

      :param ciphertext: The ciphertext message to be decrypted.
      :type ciphertext: bytes
      :param private_key: The private key for RSA decryption.
      :type private_key: RSAPrivateKey
      :return: The decrypted message.
      :rtype: bytes