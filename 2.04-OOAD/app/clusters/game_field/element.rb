class Element
  attr_reader :symbol

  def initialize(symbol)
    @symbol = symbol
  end

  def to_s
    symbol
  end

  # Возвращает true, если символы совпадают
  def ==(other) end
end
