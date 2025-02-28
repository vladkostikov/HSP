# Используем композицию и наследования видов для типов передвижения и питания.
class Animal
  attr_reader :name, :movement, :diet

  def initialize(name, movement, diet)
    @name = name
    @movement = movement
    @diet = diet
  end

  def description
    "#{name} - #{movement.type}, #{diet.type}"
  end
end

class MovementType
  attr_reader :type

  def initialize(type)
    @type = type
  end
end

class Land < MovementType
  def initialize
    super("Наземное")
  end
end

class Air < MovementType
  def initialize
    super("Летающее")
  end
end

class Water < MovementType
  def initialize
    super("Водное")
  end
end

class DietType
  attr_reader :type

  def initialize(type)
    @type = type
  end
end

class Herbivore < DietType
  def initialize
    super("Травоядное")
  end
end

class Carnivore < DietType
  def initialize
    super("Плотоядное")
  end
end

class Omnivore < DietType
  def initialize
    super("Всеядное")
  end
end
