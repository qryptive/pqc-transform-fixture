"""Transform path: LOCAL keygen -> sign (PQC_ONLY -> pure ML-DSA, deterministic).

The signing key is generated locally in this function and used ONLY by .sign(),
so M0's provenance gate proves it LOCAL and M2 I1 migrates it deterministically
(no LLM call). Expected: ec keypair+sign -> ml_dsa_65.generate_keypair()+sign().
"""
from pqcrypto.sign import ml_dsa_65
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


def sign_message(message: bytes) -> bytes:
    pk, private_key = ml_dsa_65.generate_keypair()
    signature = ml_dsa_65.sign(private_key, message)
    return signature
