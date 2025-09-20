package task04_testing_boundary_conditions;

import java.util.List;

public class GradeCalculator {
    public double calculateAverage(List<Integer> grades) {
        if (grades == null) {
            throw new IllegalArgumentException("Grades list cannot be null");
        }

        double sum = 0;
        int count = 0;

        for (Integer grade : grades) {
            if (grade != null && grade > 0) {
                sum += grade;
                count++;
            }
        }

        if (count == 0) {
            return 0;
        }

        return sum / count;
    }
}
