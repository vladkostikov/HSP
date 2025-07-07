class Element
  attr_reader :symbol, :color

  def initialize(symbol, color)
    @symbol = symbol
    @color = color
  end

  def to_s
    symbol.to_s
  end

  # Возвращает true, если символы совпадают
  def ==(other)
    other.is_a?(Element) && symbol == other.symbol && color == other.color
  end
end
