require_relative "../../../../clusters/bonus_system/bonuses/column_bonus"
require_relative "../../../../clusters/game_field/map"
require_relative "../../../../clusters/game_field/cell"
require_relative "../../../../clusters/game_field/element"

RSpec.describe ColumnBonus do
  let(:bonus) { ColumnBonus.new }

  def cell(x, y, value = :a, color = :green)
    Cell.new(x, y, Element.new(value, color))
  end

  describe "#activate" do
    it "clears all cells in the same column and returns them" do
      # Create a 2x5 map with varying values in the left column
      grid = [
        [cell(0, 0, :a), cell(1, 0, :x)],
        [cell(0, 1, :b), cell(1, 1, :x)],
        [cell(0, 2, :c), cell(1, 2, :x)],
        [cell(0, 3, :d), cell(1, 3, :x)],
        [cell(0, 4, :e), cell(1, 4, :x)]
      ]

      map = Map.new(grid)
      target_cell = map.cell_at(0, 2) # :c in column 0

      cleared = bonus.activate(map, target_cell)

      # Expect all cells in the same column to be cleared
      expect(cleared.size).to eq(5)
      expect(cleared.map(&:element)).to all(be_nil)

      # The second column remains unchanged
      (0..4).each do |y|
        expect(map.cell_at(1, y)&.element).not_to be_nil
        expect(map.cell_at(1, y)&.element&.symbol).to eq(:x)
      end
    end
  end
end
