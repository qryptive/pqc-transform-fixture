"""Transform path: weak hash -> SHA3-256 (deterministic head). Expected: md5 -> sha3_256."""
import hashlib


def fingerprint(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()
