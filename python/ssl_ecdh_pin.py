"""Transform path: TLS KEM (M2 I4) -> remove the classical set_ecdh_curve pin.

The pin suppresses the OpenSSL >= 3.5 default hybrid group. The only correct
Python `ssl` transform is REMOVING the pin (NEVER emitting set_groups, which
AttributeErrors at runtime). After removal, OpenSSL >= 3.5 offers X25519MLKEM768
by default while keeping the classical curve as fallback. Disclosure cites the
OpenSSL >= 3.5 runtime floor.
"""
import ssl


def make_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.set_ecdh_curve("prime256v1")
    return ctx
