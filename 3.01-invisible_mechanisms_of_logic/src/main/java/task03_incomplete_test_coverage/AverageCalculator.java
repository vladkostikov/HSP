package task03_incomplete_test_coverage;

public class AverageCalculator {
    public double calculateAverage(int[] numbers) {
        if (numbers.length == 0) {
            throw new IllegalArgumentException("Array must not be empty");
        }

        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }

        return (double) sum / numbers.length;
    }
}
