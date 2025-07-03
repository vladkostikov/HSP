class Element
  attr_reader :symbol

  def initialize(symbol)
    @symbol = symbol
  end

  def to_s
    symbol.to_s
  end

  # Возвращает true, если символы совпадают
  def ==(other)
    other.is_a?(Element) && symbol == other.symbol
  end
end
