from tanji.tanji import Tanji

tanji = Tanji()
tanji.generate_key_pair()
encrypted_message, ciphertext = tanji.encrypt_message("Hello, Tanji!")
decrypted_message = tanji.decrypt_message(encrypted_message, ciphertext)
