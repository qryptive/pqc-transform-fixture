// Transform path: Java LOCAL keygen + sign -> JCA ML-DSA (agentic path is LIVE, inv #26).
//
// Expected (PQC_ONLY): KeyPairGenerator.getInstance("RSA") + Signature.getInstance(
//   "SHA256withRSA") migrate to getInstance("ML-DSA-65") + BouncyCastle provider
//   registration; the RSA initialize(2048) is removed.
// Expected (mode=HYBRID AND JAVA_COMPOSITE_ENABLED=true AND BC >= 1.83, inv #32):
//   emits standardized Composite ML-DSA -> getInstance("MLDSA65-RSA3072-PSS-SHA512").
package demo;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;
import java.security.Security;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class SignService {

static {
    if (java.security.Security.getProvider("BC") == null) {
        java.security.Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
    }
}

    public byte[] sign(byte[] message) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-DSA-65", "BC");
        KeyPair keyPair = kpg.generateKeyPair();

        Signature signer = Signature.getInstance("ML-DSA-65", "BC");
        signer.initSign(keyPair.getPrivate());
        signer.update(message);
        return signer.sign();
    }
}
