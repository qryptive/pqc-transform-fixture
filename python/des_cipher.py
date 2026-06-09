"""Transform path: weak cipher (DES) -> AES-GCM (deterministic head)."""
from pqc_des_compat import AESGCMCipher
from Crypto.Cipher import DES


def encrypt(key: bytes, data: bytes) -> bytes:
    cipher = AESGCMCipher(key)
    return cipher.encrypt(data)
