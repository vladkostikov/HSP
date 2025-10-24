# 1
```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    // Переопределение метода makeSound
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myCat = new Cat();
        myCat.makeSound();  // "Meow"
    }
}
```

Как отработает программа, если

```java
class Animal {
    // Изменен метод в суперклассе
    public void makeGenericSound() {
        System.out.println("Some generic animal sound");
    }
}
```

### Ответ
Произойдёт ошибка компиляции, компилятор не найдёт метод makeSound в классе Animal.\
Нарушен контракт, в Animal определён makeGenericSound, а в Cat makeSound.\
Хрупкая зависимость, одно изменение в базовом классе разрушает остальной код.

# 2
```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound(int numberOfSounds) {
        for (int i = 0; i < numberOfSounds; i++) {
            System.out.println("Meow");
        }
    }
    
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.makeSound();
        cat.makeSound(3);
    }
}
```

Как отработает такая программа?

### Ответ

Произойдёт ошибка компиляции.\
В main используется ложное знание, что Animal принимает makeSound(int).\
Разрыв контракта, Cat добавляет поведение, о котором родитель ничего не знает.

# 3
```java
/*
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.10</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version>
</dependency>
*/

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Создаем объект ObjectMapper для парсинга JSON
        ObjectMapper objectMapper = new ObjectMapper();

        String jsonString = "{\"name\":\"John\", \"age\":30}";

        try {
            // Парсим JSON-строку в HashMap
            Map<String, Object> result = objectMapper.readValue(jsonString, HashMap.class);

            System.out.println("Name: " + result.get("name"));
        } catch (IOException e) {
            // Обработка ошибки парсинга
            e.printStackTrace();
        }

        try {
            String prettyJson = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(result);
            System.out.println("Pretty JSON: " + prettyJson);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

Какие незримые механизмы логики могут проявиться тут?

### Ответ

Конфликт версий одной зависимости, указано две версии одной библиотеки Jackson.\
В разных версиях могут быть разные сигнатуры.\
Код не скомпилируется, переменная result объявлена внутри первого блока try и недоступна во втором.
