package task05_async_programming;

public class RaceConditionExample {

    private static int counter = 0;

    public int run(int numberOfThreads, int incrementsPerThread) throws InterruptedException {
        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < incrementsPerThread; j++) {
                    counter++; // <-- здесь есть race condition
                }
            });
            threads[i].start();
        }

        for (Thread t : threads) {
            t.join();
        }

        return counter;
    }
}
