"""Transform path: weak cipher (DES) -> AES-GCM (deterministic head)."""
from pqc_crypto_helpers import mlkem768_hybrid_encrypt, mlkem768_hybrid_decrypt
from pqc_des_compat import AESGCMCipher
from Crypto.Cipher import DES


def encrypt(key: bytes, data: bytes) -> bytes:
    cipher = AESGCMCipher(key)
    return mlkem768_hybrid_encrypt(cipher, data)
