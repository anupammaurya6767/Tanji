Tanji Module
=============

.. automodule:: tanji.tanji
   :members:
   :undoc-members:
   :show-inheritance:

.. class:: Tanji(secret_key=None)

   A class for handling symmetric and asymmetric encryption.

   .. attribute:: secret_key

      The secret key used for symmetric encryption.

   .. attribute:: private_key

      The private key used for asymmetric encryption.

   .. attribute:: public_key

      The public key used for asymmetric encryption.

   .. attribute:: iv

      The initialization vector used for symmetric encryption.

   .. method:: generate_key_pair()

      Generate a pair of private and public keys for asymmetric encryption.

   .. method:: encrypt_message(message)

      Encrypt a message using symmetric encryption, then encrypt the symmetric key using asymmetric encryption.

      :param message: The message to be encrypted.
      :type message: str
      :return: The encrypted symmetric key and the encrypted message, both base64 encoded.
      :rtype: tuple

   .. method:: decrypt_message(encrypted_sym_key, ciphertext)

      Decrypt a symmetric key using asymmetric encryption, then decrypt a message using the decrypted symmetric key.

      :param encrypted_sym_key: The encrypted symmetric key, base64 encoded.
      :type encrypted_sym_key: str
      :param ciphertext: The encrypted message, base64 encoded.
      :type ciphertext: str
      :return: The decrypted message.
      :rtype: str