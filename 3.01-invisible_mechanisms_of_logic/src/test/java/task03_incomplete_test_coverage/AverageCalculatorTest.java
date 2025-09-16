package task03_incomplete_test_coverage;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AverageCalculatorTest {
    private AverageCalculator calculator;

    @BeforeEach
    public void setUp() {
        calculator = new AverageCalculator();
    }
    
    @Test
    public void testCalculateAverage() {
        int[] numbers = {1, 2, 3, 4, 5};
        double average = calculator.calculateAverage(numbers);
        assertEquals(3, average);
    }
    
    
    @Test
    public void testCalculateAverageWithEmptyArray() {
        int[] numbers = {};
        assertThrows(IllegalArgumentException.class, () -> calculator.calculateAverage(numbers));
    }
    
    // Bug: NullPointerException is thrown instead of IllegalArgumentException
    @Test
    public void testCalculateAverageWithNullArray() {
        int[] numbers = null;
        assertThrows(NullPointerException.class, () -> calculator.calculateAverage(numbers));
    }
}
