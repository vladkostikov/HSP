require_relative '../game_field/element'

class ElementFactory
  TYPES = %i[A B C D E]

  def create_random_element
    Element.new(TYPES.sample)
  end
end
