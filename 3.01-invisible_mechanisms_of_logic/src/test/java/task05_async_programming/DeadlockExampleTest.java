package task05_async_programming;

import org.junit.jupiter.api.Test;

public class DeadlockExampleTest {

    @Test
    void testDeadlock() throws InterruptedException {
        // Запуск в отдельном потоке, чтобы JUnit не завис
        Thread testThread = new Thread(() -> {
            try {
                DeadlockExample.run();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        testThread.start();

        testThread.join(1000);

        if (testThread.isAlive()) {
            System.out.println("Deadlock detected (thread is still alive after timeout)");
            testThread.interrupt();
        } else {
            System.out.println("No deadlock detected");
        }
    }
}
