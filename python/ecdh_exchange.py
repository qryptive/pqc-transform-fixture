"""Transform path: LOCAL key-exchange (ECDH .exchange()) -> ML-KEM encaps.

The private key is local, so the exchange migrates deterministically to
ml_kem_768.encaps(...). Sender side only — the transform leaves a TODO comment
for the receiver-side decaps (DH is one-call symmetric; ML-KEM is encaps/decaps).
"""
from cryptography.hazmat.primitives.asymmetric import ec


def derive_shared_secret(peer_public_key) -> bytes:
    private_key = ec.generate_private_key(ec.SECP256R1())
    shared = private_key.exchange(ec.ECDH(), peer_public_key)
    return shared
