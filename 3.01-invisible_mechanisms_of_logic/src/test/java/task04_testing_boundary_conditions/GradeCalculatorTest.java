package task04_testing_boundary_conditions;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class GradeCalculatorTest {
    private GradeCalculator calculator;

    @BeforeEach
    public void setUp() {
        calculator = new GradeCalculator();
    }

    @Test
    public void testCalculateAverageWithValidGrades() {
        List<Integer> grades = Arrays.asList(5, 4, 3, 4, 5);
        double result = calculator.calculateAverage(grades);
        assertEquals(4.2, result, 0.01);
    }

    @Test
    void testCalculateAverageWithNegativesAndZeros() {
        List<Integer> grades = Arrays.asList(-1, 0, -5, 5, 10);
        double result = calculator.calculateAverage(grades);
        assertEquals(7.5, result, 0.01);
    }

    @Test
    void testCalculateAverageWithNullList() {
        assertThrows(IllegalArgumentException.class, () -> calculator.calculateAverage(null));
    }

    @Test
    public void testCalculateAverageWithEmptyGrades() {
        List<Integer> grades = Collections.emptyList();
        double result = calculator.calculateAverage(grades);
        assertEquals(0, result);
    }

    @Test
    void testCalculateAverageWithNullValues() {
        List<Integer> grades = Arrays.asList(5, null, 3, null, 4);
        double result = calculator.calculateAverage(grades);
        assertEquals(4, result);
    }

    @Test
    void testCalculateAverageWithOnlyNonPositive() {
        List<Integer> grades = Arrays.asList(0, -1, -2, -3);
        double result = calculator.calculateAverage(grades);
        assertEquals(0, result);
    }
}
