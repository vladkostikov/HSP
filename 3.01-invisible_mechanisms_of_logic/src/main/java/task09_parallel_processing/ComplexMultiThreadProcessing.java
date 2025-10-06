package task09_parallel_processing;

import java.util.Arrays;
import java.util.Random;

/**
 * Task: to simplify the code.
 * Changes: replaced manual thread management with parallel streams.
 */
public class ComplexMultiThreadProcessing {
    private static final int SIZE = 1_000_000;
    private static final int MAX_VALUE = 100;

    public static void main(String[] args) {
        int[] data = generateData(SIZE);
        long sum = calculateSum(data);
        printResult(sum);
    }

    private static int[] generateData(int size) {
        Random random = new Random();
        int[] data = new int[size];
        for (int i = 0; i < size; i++) {
            data[i] = random.nextInt(MAX_VALUE);
        }
        return data;
    }

    private static long calculateSum(int[] data) {
        return Arrays.stream(data)
                .parallel()
                .asLongStream()
                .sum();
    }

    private static void printResult(long sum) {
        System.out.println("Sum of all elements: " + sum);
    }
}
