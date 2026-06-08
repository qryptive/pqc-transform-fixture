"""REFUSAL demo (NOT a transform): external-key verify.

`public_key` is a bare parameter — its origin is outside this file (caller / loaded
PEM / partner). M0 (#29) cannot prove it LOCAL, so it REFUSES rather than ship a
broken ml_dsa verify against a key it does not control. Expected output: a
`failed_symbol` "manual migration required" carrying an M1 migration recommendation
in the PR comment / scan Issue. NO code change here is the CORRECT result.
"""


def verify_signature(public_key, signature: bytes, message: bytes) -> None:
    # If this ever gets transformed to ml_dsa_65.verify(...), that is a regression
    # (broken-key ship) — M0 must keep refusing it.
    public_key.verify(signature, message)
