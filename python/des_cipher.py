"""Transform path: weak cipher (DES) -> AES-GCM (deterministic head)."""
from Crypto.Cipher import DES


def encrypt(key: bytes, data: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)
