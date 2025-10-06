package task09_parallel_processing;

import java.util.Random;

public class ComplexMultiThreadProcessing {
    private static final int SIZE = 1000000;
    private static final int THREADS = 4;
    private static final int[] data = new int[SIZE];
    private static volatile int sum = 0;

    public static void main(String[] args) {
        Random random = new Random();
        for (int i = 0; i < SIZE; i++) {
            data[i] = random.nextInt(100);
        }

        Thread[] threads = new Thread[THREADS];
        int chunkSize = SIZE / THREADS;

        for (int i = 0; i < THREADS; i++) {
            final int start = i * chunkSize;
            final int end = (i + 1) * chunkSize;
            threads[i] = new Thread(() -> {
                int localSum = 0;
                for (int j = start; j < end; j++) {
                    localSum += data[j];
                }
                synchronized (ComplexMultiThreadProcessing.class) {
                    sum += localSum;
                }
            });
            threads[i].start();
        }

        for (int i = 0; i < THREADS; i++) {
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("Sum of all elements: " + sum);
    }
}
