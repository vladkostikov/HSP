package task05_async_programming;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class RaceConditionExampleSafeSynchronizedTest {

    @Test
    void testCounterWithMultipleThreads() throws InterruptedException {
        final int numberOfThreads = 10;
        final int incrementsPerThread = 100_000;

        int result = RaceConditionExampleSafeSynchronized.run(numberOfThreads, incrementsPerThread);

        assertEquals(numberOfThreads * incrementsPerThread, result);
    }
}
