package task06_async_programming;

import java.util.concurrent.Semaphore;

/**
 * Database simulates a database with limited connections.
 */
class Database {
    private final Semaphore semaphore = new Semaphore(3);

    public void connect(String threadName) {
        try {
            System.out.println("Connecting " + threadName);
            semaphore.acquire();
            System.out.println("Connected " + threadName);

            Thread.sleep(2000);
            System.out.println("Closing " + threadName);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
        }
    }
}

public class SemaphoreDatabaseExample {
    public static void main(String[] args) {
        Database db = new Database();

        for (int i = 0; i < 10; i++) {
            String threadName = "Thread-" + i;
            new Thread(() -> db.connect(threadName)).start();
        }
    }
}
