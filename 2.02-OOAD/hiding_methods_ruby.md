# Политика скрытия методов при наследовании в Ruby

В Ruby существует возможность управления видимостью методов с помощью ключевых слов public, protected и private.
По умолчанию все методы являются публичными.

Всего существует четыре варианта скрытия методов:
- метод публичен в родительском классе А и публичен в его потомке B
```ruby
class A1
  def hello
    puts "Hello from #{self.class}"
  end
end

class B1 < A1
end

A1.new.hello # Hello from A1
B1.new.hello # Hello from B1
```

- метод публичен в родительском классе А и скрыт в его потомке B
```ruby
class A2
  def hello
    puts "Hello from #{self.class}"
  end
end

class B2 < A2
  private :hello
end

A2.new.hello # Hello from A2
B2.new.hello # private method 'hello' called for an instance of B2 (NoMethodError)
```

- метод скрыт в родительском классе А и публичен в его потомке B
```ruby
class A3
  private
  
  def hello
    puts "Hello from #{self.class}"
  end
end

class B3 < A3
  public :hello
end

A3.new.hello # private method 'hello' called for an instance of A3 (NoMethodError)
B3.new.hello # Hello from B3
```

- метод скрыт в родительском классе А и скрыт в его потомке B
```ruby
class A4
  private 
  
  def hello
    puts "Hello from #{self.class}"
  end
end

class B4 < A4
end

A4.new.hello # => private method 'hello' called for an instance of A4 (NoMethodError)
B4.new.hello # => private method 'hello' called for an instance of B4 (NoMethodError)
```
