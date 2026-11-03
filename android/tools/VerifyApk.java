import com.android.apksig.ApkVerifier;

import java.io.File;

/** Verifies an APK's signature schemes using apksig. Exits 0 when verified. */
public final class VerifyApk {

    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: VerifyApk <apk>");
            System.exit(2);
        }
        ApkVerifier verifier = new ApkVerifier.Builder(new File(args[0])).build();
        ApkVerifier.Result result = verifier.verify();
        System.out.println("Verified: " + result.isVerified());
        System.out.println("  v1 scheme: " + result.isVerifiedUsingV1Scheme());
        System.out.println("  v2 scheme: " + result.isVerifiedUsingV2Scheme());
        System.out.println("  v3 scheme: " + result.isVerifiedUsingV3Scheme());
        if (!result.isVerified()) {
            for (ApkVerifier.IssueWithParams issue : result.getErrors()) {
                System.err.println("ERROR: " + issue);
            }
            System.exit(1);
        }
    }
}
