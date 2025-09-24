package task05_async_programming;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotEquals;


public class RaceConditionExampleTest {

    @Test
    void testCounterWithRaceCondition() throws InterruptedException {
        final int numberOfThreads = 10;
        final int incrementsPerThread = 100_000;

        RaceConditionExample rc = new RaceConditionExample();

        int result = rc.run(numberOfThreads, incrementsPerThread);

        assertNotEquals(numberOfThreads * incrementsPerThread, result);
    }
}
