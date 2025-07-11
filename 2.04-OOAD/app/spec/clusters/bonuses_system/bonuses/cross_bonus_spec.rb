require_relative "../../../../clusters/bonus_system/bonuses/cross_bonus"
require_relative "../../../../clusters/game_field/map"
require_relative "../../../../clusters/game_field/cell"
require_relative "../../../../clusters/game_field/element"

RSpec.describe CrossBonus do
  let(:bonus) { CrossBonus.new }

  def cell(x, y, value = :a, color = :green)
    Cell.new(x, y, Element.new(value, color))
  end

  describe "#activate" do
    it "clears center and adjacent (cross) cells and returns them" do
      # Create a 3x3 map, activate bonus at center (1,1)
      grid = [
        [cell(0, 0, :a), cell(1, 0, :b), cell(2, 0, :c)],
        [cell(0, 1, :d), cell(1, 1, :e), cell(2, 1, :f)],
        [cell(0, 2, :g), cell(1, 2, :h), cell(2, 2, :i)]
      ]

      map = Map.new(grid)
      target_cell = map.cell_at(1, 1)

      cleared = bonus.activate(map, target_cell)

      # Expect 5 cleared cells: center + one in each direction
      expect(cleared.size).to eq(5)

      expected_coords = [
        [1, 1], # center
        [0, 1], # left
        [2, 1], # right
        [1, 0], # top
        [1, 2] # bottom
      ]

      expected_coords.each do |x, y|
        cell = map.cell_at(x, y)
        expect(cleared).to include(cell)
        expect(cell&.element).to be_nil
      end

      # Other cells remain intact
      untouched_coords = [
        [0, 0], [2, 0],
        [0, 2], [2, 2]
      ]

      untouched_coords.each do |x, y|
        cell = map.cell_at(x, y)
        expect(cell&.element).not_to be_nil
      end
    end
  end
end
