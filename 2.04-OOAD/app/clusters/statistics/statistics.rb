class Statistics
  attr_reader :score, :moves

  def initialize
    @score = 0
    @moves = 0
  end

  def increment_score(score)
    @score += score
  end

  def increment_moves
    @moves += 1
  end

  def decrement_moves
    @moves -= 1
  end

  def calculate_score(match_size)
    return 0 if match_size < 3

    # The progression formula: score = n * (10 + 5 * (n - 3))
    match_size * (10 + (5 * (match_size - 3)))
  end
end
