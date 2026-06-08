"""Transform path: deprecated TLS protocol -> modern TLS (deterministic head)."""
import ssl


def make_context() -> ssl.SSLContext:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.verify_mode = ssl.CERT_REQUIRED
    return ctx
