class Cell
  attr_reader :x, :y, :element

  def initialize(x, y, element = nil)
    @x, @y = x, y
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
    raise ArgumentError, "Expected Element, got #{new_element.class}" unless new_element.is_a?(Element)

    if !empty? && !force
      raise "Cell at (#{x}, #{y}) is already occupied"
    end

    @element = new_element
  end
end
