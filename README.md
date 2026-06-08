# Transform fixture — one file per transform path

A purpose-built scan/fix target that exercises each transform path the engine supports, with **predictable before→after** so you can eyeball M0+M1+M2 after a `/deploy-scanner`. Contrast with paramiko (which is all correct *refusals* — a bad demo). Re-run after each milestone as a regression demo.

**How to run:** point the scanner + fix-batch at this directory (e.g. `/test-real-repo-full` against a copy, or scan + `fix-batch`). Default mode = `PQC_ONLY`. To see Java Composite ML-DSA, set `JAVA_COMPOSITE_ENABLED=true` on `pqc-scanner` AND run `mode=HYBRID` AND ensure BC ≥ 1.83.

## Expected results

| File | Path exercised | Expected (PQC_ONLY) | Notes |
|---|---|---|---|
| `python/sign_local.py` | local keygen → sign | **TRANSFORM** → `ml_dsa_65.generate_keypair()` + `ml_dsa_65.sign(...)` | deterministic, **no LLM call** (M2 I1) |
| `python/hash_md5.py` | weak hash | **TRANSFORM** → SHA3-256 | deterministic head |
| `python/des_cipher.py` | weak cipher | **TRANSFORM** → AES-GCM | deterministic head |
| `python/tls_context.py` | deprecated TLS | **TRANSFORM** → modern TLS context | deterministic head |
| `python/ssl_ecdh_pin.py` | TLS KEM (I4) | **TRANSFORM** → `set_ecdh_curve(...)` pin **removed** | OpenSSL ≥ 3.5 then offers `X25519MLKEM768` by default; **no `set_groups` emitted** (inv #33) + disclosure |
| `python/ecdh_exchange.py` | key-exchange | **TRANSFORM** → `ml_kem_768.encaps(...)` | sender-side only + receiver-side TODO comment (encaps/decaps asymmetry) |
| `python/verify_external.py` | external-key verify | **REFUSE + recommendation** | M0 (#29): bare-param key = UNKNOWN → honest "manual migration required" + M1 recommendation. *No code change — this is correct.* |
| `java/SignService.java` | Java local keygen + sign | **TRANSFORM** → JCA `getInstance("ML-DSA-65")` + provider reg | Java agentic is live (#26). With `JAVA_COMPOSITE_ENABLED=true` + `mode=HYBRID` + BC ≥ 1.83 → **Composite ML-DSA** (`MLDSA65-RSA3072-PSS-SHA512`) instead. |

## What a healthy result looks like
- **7 files with real code transforms** + **1 honest refusal** (`verify_external.py`) carrying a precise migration recommendation.
- Disclosures present (e.g. ML-DSA signature-size caveat; OpenSSL ≥ 3.5 floor for the TLS pin; BC ≥ 1.83 floor if composite).
- The refusal is a `failed_symbol` with a recommendation in the PR comment / scan Issue — **not** a silent drop, and **not** a broken ML-DSA-against-an-external-key ship.

## What would be WRONG (regressions to watch)
- Any transform of `verify_external.py` (would be a broken-key ship — M0 must refuse it).
- A `set_groups(...)` call emitted for `ssl_ecdh_pin.py` (AttributeErrors at runtime — inv #33).
- An LLM call for `sign_local.py` (it must be fully deterministic — M2 I1 short-circuit).
- PQH1 / a custom hybrid envelope anywhere (retired — M2 I2a/I2b).
