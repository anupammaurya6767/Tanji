import pytest
from tanji.tanji import Tanji

SECRET_KEY = "supersecret"


@pytest.fixture
def tanji_instance():
    return Tanji(secret_key=SECRET_KEY)


def test_generate_key_pair(tanji_instance):
    tanji_instance.generate_key_pair()
    assert tanji_instance.private_key is not None
    assert tanji_instance.public_key is not None


def test_encrypt_decrypt_message(tanji_instance):
    tanji_instance.generate_key_pair()
    plaintext = "Hello, Tanji!"

    # Encrypt the message
    encrypted_message, ciphertext = tanji_instance.encrypt_message(plaintext)

    # Decrypt the message
    decrypted_message = tanji_instance.decrypt_message(encrypted_message, ciphertext)

    # Print values for debugging
    print("Original plaintext:", plaintext)
    print("Decrypted message:", decrypted_message)

    # Assert equality
    assert decrypted_message == plaintext
