import com.android.apksig.ApkSigner;

import java.io.File;
import java.io.FileInputStream;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.cert.X509Certificate;
import java.util.Collections;
import java.util.List;

/** Signs an APK (v1 + v2 + v3) with a PKCS12 keystore using apksig. */
public final class SignApk {

    public static void main(String[] args) throws Exception {
        if (args.length != 5) {
            System.err.println("Usage: SignApk <in.apk> <out.apk> <keystore> <alias> <password>");
            System.exit(2);
        }
        String in = args[0];
        String out = args[1];
        String keystorePath = args[2];
        String alias = args[3];
        String password = args[4];

        KeyStore keyStore = KeyStore.getInstance("PKCS12");
        try (FileInputStream fin = new FileInputStream(keystorePath)) {
            keyStore.load(fin, password.toCharArray());
        }
        PrivateKey key = (PrivateKey) keyStore.getKey(alias, password.toCharArray());
        if (key == null) {
            throw new IllegalStateException("No key found in keystore for alias " + alias);
        }
        X509Certificate cert = (X509Certificate) keyStore.getCertificate(alias);
        List<X509Certificate> certs = Collections.singletonList(cert);

        ApkSigner.SignerConfig config =
                new ApkSigner.SignerConfig.Builder("literature", key, certs).build();
        ApkSigner signer = new ApkSigner.Builder(Collections.singletonList(config))
                .setInputApk(new File(in))
                .setOutputApk(new File(out))
                .setMinSdkVersion(24)
                .setV1SigningEnabled(true)
                .setV2SigningEnabled(true)
                .setV3SigningEnabled(true)
                .setCreatedBy("English Literature build.py")
                .build();
        signer.sign();
        System.out.println("Signed: " + out);
    }
}
