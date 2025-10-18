package task13_hoare_logic;

public class HoareTriples {
    /*
     * {P: arr.length > 0} findMax(arr) {Q: result = max(arr)}
     *
     * Precondition P: the array is not empty (arr.length > 0)
     * Postcondition Q: result is the maximum element in the array
     *
     * Loop invariant I:
     * 0 <= i <= arr.length and max = max(arr[0..i-1])
     *
     * Invariant proof:
     * 1. Initialization:
     * Before the first iteration i = 1, max = arr[0]
     * Check invariant: max = max(arr[0..i-1]) = arr[0], true for the first element
     *
     * 2. Maintenance:
     * Assume the invariant is true before iteration i (max = max(arr[0..i-1]))
     * Compare arr[i] with max and update max if needed
     * After the iteration, max = max(arr[0..i])
     * Invariant still holds
     *
     *
     * 3. Termination:
     * The loop ends when i = arr.length
     * Then max = max(arr[0..arr.length-1]) = max(arr)
     * Postcondition holds
     *
     * Thus, findMax(arr) correctly finds the maximum element
     * using the loop invariant and Hoare triples.
     */
    public static int findMax(int[] arr) {
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        return max;
    }

    public static void main(String[] args) {
        System.out.println("findMax([-5, -1, 0, 5, 10]) = " + findMax(new int[]{-5, -1, 0, 5, 10})); // 10
        System.out.println("findMax([3, 7, 2, 9, 1]) = " + findMax(new int[]{3, 7, 2, 9, 1})); // 9
        System.out.println("findMax([-10, -20, -3]) = " + findMax(new int[]{-10, -20, -3})); // -3
    }
}
