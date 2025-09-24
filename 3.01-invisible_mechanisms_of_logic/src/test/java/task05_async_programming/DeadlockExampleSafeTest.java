package task05_async_programming;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class DeadlockExampleSafeTest {

    @Test
    void testNoDeadlock() throws InterruptedException {
        Thread testThread = new Thread(() -> {
            try {
                DeadlockExampleSafe.run();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        testThread.start();

        testThread.join(2000);

        assertTrue(!testThread.isAlive());
    }
}
