class Bonus
  def initialize; end

  # Вызывает эффект на Map
  def activate(_game_map)
    raise NotImplementedError, "#{self.class}#activate must be implemented"
  end
end
