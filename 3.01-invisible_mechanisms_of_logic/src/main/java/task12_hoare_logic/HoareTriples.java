package task12_hoare_logic;

public class HoareTriples {
    /*
     * {P: x = n} abs(x) {Q: result = |n|}
     *
     * Proof of correctness:
     * 1. Precondition: x = n
     * 2. If branch: if (x < 0) then x = -x. Since x = n and n < 0, result = -n = |n|
     * 3. Else branch: if (x >= 0) then the function returns x. Since x = n and n >= 0, result = n = |n|
     * 4. Therefore, Q: result = |n| holds in all cases.
     */
    public static int abs(int x) {
        if (x < 0) {
            return -x;
        }
        return x;
    }

    /*
     * {P: a = m, b = n} max(a, b) {Q: result = max(m, n)}
     *
     * Proof of correctness:
     * 1. Precondition: a = m, b = n
     * 2. If branch: if (a >= b) then the function returns a. Since a = m and m >= n, result = m = max(m, n)
     * 3. Else branch: if (a < b) then the function returns b. Since b = n and n > m, result = n = max(m, n)
     * 4. Therefore, Q: result = max(m, n) holds in all cases.
     */
    public static int max(int a, int b) {
        if (a >= b) {
            return a;
        }
        return b;
    }

    /*
     * {P: a = m, b = n} maxAbs(a, b) {Q: result = max(|m|, |n|)}
     *
     * Proof of correctness:
     * 1. Precondition: a = m, b = n
     * 2. Step 1: absA = abs(a). By correctness of abs(), absA = |m|
     * 3. Step 2: absB = abs(b). By correctness of abs(), absB = |n|
     * 4. Step 3: result = max(absA, absB). By correctness of max(), result = max(|m|, |n|)
     * 5. Therefore, Q: result = max(|m|, |n|) holds in all cases.
     */
    public static int maxAbs(int a, int b) {
        int absA = abs(a);
        int absB = abs(b);
        return max(absA, absB);
    }

    public static void main(String[] args) {
        System.out.println("abs(-5) = " + abs(-5)); // 5
        System.out.println("max(3, 7) = " + max(3, 7)); // 7
        System.out.println("maxAbs(-8, 5) = " + maxAbs(-8, 5)); // 8
    }
}
