require_relative '../game_field/element'

class ElementFactory
  TYPES = %i[A B C D E]
  COLORS = {
    :A => :light_blue,
    :B => :light_green,
    :C => :yellow,
    :D => :magenta,
    :E => :red
  }

  def create_random_element
    type = TYPES.sample
    color = COLORS[type]
    Element.new(type, color)
  end
end
