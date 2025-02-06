# Базовый абстрактный класс с фундаментальным набором операций.
# Закрыт для модификации.
class General < Object
  # Запрет на создание объектов General.
  def initialize
    raise NotImplementedError if self.class == General
  end

  # Глубокое копирование содержимого одного объекта в другой существующий объект.
  def copy_to(other_object)
    instance_variables.each do |var|
      value = instance_variable_get(var)
      other_object.instance_variable_set(var, deep_copy(value))
    end
  end

  # Создание нового объекта и глубокое копирование в него исходного объекта.
  def clone
    new_object = self.class.allocate
    copy_to(new_object)
    new_object.send(:initialize) if new_object.respond_to?(:initialize)
    new_object
  end

  # Глубокое сравнение объектов по-содержимому.
  def ==(other)
    return false unless other.is_a?(self.class)

    instance_variables.all? do |var|
      self_value = instance_variable_get(var)
      other_value = other.instance_variable_get(var)
      self_value == other_value
    end
  end

  # Сериализация объекта.
  def serialize
    Marshal.dump(self)
  end

  # Десериализация объекта.
  def self.deserialize(data)
    Marshal.load(data)
  end

  # Наглядное представление содержимого объекта в текстовом формате.
  def to_s
    vars = instance_variables.map { |var| "#{var}=#{instance_variable_get(var)}" }.join(", ")
    "#<#{self.class}:#{self.object_id} (#{vars})>"
  end

  # Проверка типа. Является ли тип текущего объекта указанным типом. Реализовано в Kernel.
  # def is_a?(klass) end

  # Получение реального типа объекта, экземпляром которого он был создан. Реализовано в Kernel.
  # def class end

  private

  def deep_copy(obj = self)
    Marshal.load(Marshal.dump(obj))
  rescue TypeError
    obj.dup
  end
end

# Базовый класс, от которого наследуются все новые классы в проекте.
# Открыт для модификации.
class Any < General
end
