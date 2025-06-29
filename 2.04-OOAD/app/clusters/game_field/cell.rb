class Cell
  attr_reader :x, :y
  attr_accessor :element

  def initialize(x, y, element = nil)
    @x, @y = x, y
    @element = element
  end

  def empty?
    element.nil?
  end
end
