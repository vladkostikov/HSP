import java.util.ArrayList;
import java.util.List;

class General {
    public General add(General other) {
        throw new UnsupportedOperationException("Subclasses must implement add method");
    }
}

class Any extends General { }

class Integer extends Any {
    private final int value;

    public Integer(int value) {
        this.value = value;
    }

    @Override
    public Integer add(General other) {
        if (!(other instanceof Integer)) {
            throw new UnsupportedOperationException("Cannot add different types");
        }
        return new Integer(this.value + ((Integer) other).value);
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}

class Vector<T extends Any> extends Any {
    private final List<T> elements;

    public Vector(List<T> elements) {
        this.elements = List.copyOf(elements);
    }

    public List<T> getElements() {
        return elements;
    }

    @Override
    public Vector<T> add(General other) {
        if (!(other instanceof Vector<?> otherVector)) {
            throw new UnsupportedOperationException("Cannot add different types");
        }

        if (this.elements.size() != otherVector.getElements().size()) {
            return null;
        }

        List<T> resultElements = new ArrayList<>();
        for (int i = 0; i < elements.size(); i++) {
            @SuppressWarnings("unchecked")
            T sum = (T) elements.get(i).add(otherVector.getElements().get(i));
            resultElements.add(sum);
        }
        return new Vector<>(resultElements);
    }

    @Override
    public String toString() {
        return elements.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        List<Integer> list1 = List.of(new Integer(1), new Integer(2), new Integer(3));
        List<Integer> list2 = List.of(new Integer(4), new Integer(5), new Integer(6));
        List<Integer> list3 = List.of(new Integer(7), new Integer(8));

        Vector<Integer> vector1 = new Vector<>(list1);
        Vector<Integer> vector2 = new Vector<>(list2);
        Vector<Integer> result = vector1.add(vector2);
        System.out.println("Vector 1: " + vector1);
        System.out.println("Vector 2: " + vector2);
        System.out.println("Sum: " + result);

        Vector<Integer> vector3 = new Vector<>(list3);
        Vector<Integer> nullResult = vector2.add(vector3);
        System.out.println("Vector 2: " + vector2);
        System.out.println("Vector 3: " + vector3);
        System.out.println("Null Sum: " + nullResult);

        Vector<Vector<Integer>> nestedVector1 = new Vector<>(List.of(vector1, vector3));
        Vector<Vector<Integer>> nestedVector2 = new Vector<>(List.of(vector2, vector3));
        Vector<Vector<Integer>> nestedResult = nestedVector1.add(nestedVector2);
        System.out.println("Nested Vector 1: " + nestedVector1);
        System.out.println("Nested Vector 2: " + nestedVector2);
        System.out.println("Nested Sum: " + nestedResult);
    }
}
