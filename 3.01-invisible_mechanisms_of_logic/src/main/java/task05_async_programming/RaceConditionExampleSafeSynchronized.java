package task05_async_programming;

public class RaceConditionExampleSafeSynchronized {

    private static int counter = 0;

    private static synchronized void increment() {
        counter++;
    }

    /**
     * Запускает несколько потоков, каждый из которых увеличивает счётчик
     * incrementsPerThread раз.
     *
     * В небезопасной версии итоговое значение может быть неверным
     * из-за race condition — несколько потоков одновременно читают и записывают
     * одно и то же значение counter.
     *
     * В этой версии используется synchronized increment(), чтобы избежать этой проблемы.
     */
    public static int run(int numberOfThreads, int incrementsPerThread) throws InterruptedException {
        counter = 0;

        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < incrementsPerThread; j++) {
                    increment();
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
