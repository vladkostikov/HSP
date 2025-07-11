require_relative "bonuses/column_bonus"
require_relative "bonuses/cross_bonus"
require_relative "bonuses/row_bonus"

class BonusManager
  attr_reader :bonuses

  def initialize
    @bonuses = []
  end

  def should_create_bonus?(match)
    match.size >= 4
  end

  def create_bonus(match)
    bonus = case match.size
            when 4 then RowBonus.new
            when 5..6 then ColumnBonus.new
            when 7.. then CrossBonus.new
            else return nil
            end

    bonuses << bonus
  end
end
