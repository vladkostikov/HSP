require '../game_field/element'

class ElementFactory
  TYPES = %w[A B C D E]

  def create_random_element
    Element.new(TYPES.sample)
  end
end
