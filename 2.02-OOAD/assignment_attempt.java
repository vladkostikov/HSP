import java.io.Serializable;

class General implements Serializable {
    public Any attemptAssignment(Any source) {
        if (this.getClass().isAssignableFrom(source.getClass())) {
            return source;
        }
        return new None();
    }
}

class Any extends General { }

final class None extends Any { }

class Other extends Any {}

public class Test {
    public static Any assignment_attempt(Any target, Any source) {
        Any result = target.attemptAssignment(source);
        if (source instanceof None || !(result instanceof None)) {
            System.out.println("Присваивание успешно. Результат: " + result.getClass().getSimpleName());
            return result;
        }

        System.out.println("Присваивание не удалось. Результат: None");
        return result;
    }

    public static void main(String[] args) {
        Any anyTarget = new Any();
        Any anySource = new Any();
        Other otherTarget = new Other();
        Other otherSource = new Other();
        None noneTarget = new None();
        None noneSource = new None();

        assignment_attempt(anyTarget, anySource); // Присваивание успешно. Результат: Any
        assignment_attempt(anyTarget, otherSource); // Присваивание успешно. Результат: Other
        assignment_attempt(anyTarget, noneSource); // Присваивание успешно. Результат: None

        assignment_attempt(otherTarget, anySource); // Присваивание не удалось. Результат: None
        assignment_attempt(otherTarget, otherSource); // Присваивание успешно. Результат: Other
        assignment_attempt(otherTarget, noneSource); // Присваивание успешно. Результат: None


        assignment_attempt(noneTarget, anySource); // Присваивание не удалось. Результат: None
        assignment_attempt(noneTarget, otherSource); // Присваивание не удалось. Результат: None
        assignment_attempt(noneTarget, noneSource); // Присваивание успешно. Результат: None
    }
}
