"""Transform path: weak hash -> SHA3-256 (deterministic head). Expected: md5 -> sha3_256."""
import hashlib


def fingerprint(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()  # PQC-CAVEAT: SHA3-256/SHA3-512 output size may differ from SHA-1(20B)/MD5(16B). Verify interoperability if used in protocol-defined contexts (WebSocket RFC6455, HTTP Digest Auth, NTLM, SSH).
