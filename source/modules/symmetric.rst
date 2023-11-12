SymmetricCipher Module
======================

.. automodule:: symmetric.symmetric
   :members:
   :undoc-members:
   :show-inheritance:

.. class:: SymmetricCipher

   A class for handling symmetric encryption.

   .. method:: generate_key()

      Generate a 256-bit symmetric key.

      :return: The generated symmetric key.
      :rtype: bytes

   .. method:: generate_iv()

      Generate a 128-bit initialization vector.

      :return: The generated initialization vector.
      :rtype: bytes

   .. method:: aes_encrypt(key, iv, plaintext)

      Encrypt a plaintext message using AES encryption.

      :param key: The symmetric key.
      :type key: bytes
      :param iv: The initialization vector.
      :type iv: bytes
      :param plaintext: The plaintext message to be encrypted.
      :type plaintext: str
      :return: The encrypted message.
      :rtype: bytes

   .. method:: aes_decrypt(key, iv, ciphertext)

      Decrypt a ciphertext message using AES decryption.

      :param key: The symmetric key.
      :type key: bytes
      :param iv: The initialization vector.
      :type iv: bytes
      :param ciphertext: The ciphertext message to be decrypted.
      :type ciphertext: bytes
      :return: The decrypted message.
      :rtype: str