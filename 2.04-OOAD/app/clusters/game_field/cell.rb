class Cell
  attr_reader :x, :y, :element

  def initialize(x, y, element = nil)
    @x = x
    @y = y
    @element = element
  end

  def clear
    @element = nil
  end

  def empty?
    @element.nil?
  end

  def present?
    !empty?
  end

  def insert_element(new_element, force: false)
    raise "Cell at (#{x}, #{y}) is already occupied" if !empty? && !force

    @element = new_element
  end

  def match?(other)
    return false if other.nil? || element.nil?

    element == other.element
  end
end
