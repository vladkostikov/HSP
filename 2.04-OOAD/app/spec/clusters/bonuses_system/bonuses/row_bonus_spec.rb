require_relative "../../../../clusters/bonus_system/bonuses/row_bonus"
require_relative "../../../../clusters/game_field/map"
require_relative "../../../../clusters/game_field/cell"
require_relative "../../../../clusters/game_field/element"

RSpec.describe RowBonus do
  let(:bonus) { RowBonus.new }

  def cell(x, y, value = :a, color = :green)
    Cell.new(x, y, Element.new(value, color))
  end

  describe "#activate" do
    it "clears all cells in the same row and returns them" do
      # Create a 3x3 grid with different elements
      grid = [
        [cell(0, 0, :a), cell(1, 0, :b), cell(2, 0, :c)],
        [cell(0, 1, :d), cell(1, 1, :e), cell(2, 1, :f)],
        [cell(0, 2, :g), cell(1, 2, :h), cell(2, 2, :i)]
      ]

      map = Map.new(grid)
      target_cell = map.cell_at(1, 1) # Middle cell in the second row

      cleared = bonus.activate(map, target_cell)

      # Check that all cells in the same row (y = 1) are cleared
      expect(cleared.size).to eq(3)

      (0...map.width).each do |x|
        cell = map.cell_at(x, 1)
        expect(cleared).to include(cell)
        expect(cell&.element).to be_nil
      end

      # Cells in other rows should remain unchanged
      [[0, 0], [1, 0], [2, 0], [0, 2], [1, 2], [2, 2]].each do |x, y|
        expect(map.cell_at(x, y)&.element).not_to be_nil
      end
    end
  end
end
