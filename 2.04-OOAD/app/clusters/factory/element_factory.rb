require_relative "../game_field/element"

class ElementFactory
  TYPES = %i[A B C D E].freeze
  COLORS = {
    A: :blue,
    B: :green,
    C: :cyan,
    D: :magenta,
    E: :red
  }.freeze

  def create(type, color)
    Element.new(type, color)
  end

  def create_random
    type = TYPES.sample
    color = COLORS[type]
    Element.new(type, color)
  end
end
