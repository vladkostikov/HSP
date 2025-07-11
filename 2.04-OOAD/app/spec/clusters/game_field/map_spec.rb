require_relative "../../../clusters/game_field/map"
require_relative "../../../clusters/game_field/cell"
require_relative "../../../clusters/game_field/element"
require_relative "../../../clusters/factory/element_factory"

RSpec.describe Map do
  let(:factory) { ElementFactory.new }
  let(:map) { Map.new }

  def cell(value = :a, color = :green)
    Cell.new(0, 0, Element.new(value, color))
  end

  describe "#initialize" do
    it "creates a grid of 8x8 cells" do
      expect(map.instance_variable_get(:@grid).size).to eq(8)
      expect(map.instance_variable_get(:@grid).all? { |row| row.size == 8 }).to be true
    end

    it "not fills cells with elements" do
      map.each_cell do |cell|
        expect(cell.element).to be_nil
      end
    end
  end

  describe "#cell_at" do
    it "returns correct cell for valid coordinates" do
      cell = map.cell_at(3, 4)
      expect(cell).to be_a(Cell)
      expect(cell&.x).to eq(3)
      expect(cell&.y).to eq(4)
    end

    it "returns nil for out-of-bound coordinates" do
      expect(map.cell_at(-1, 0)).to be_nil
      expect(map.cell_at(0, -1)).to be_nil
      expect(map.cell_at(8, 0)).to be_nil
      expect(map.cell_at(0, 8)).to be_nil
    end
  end

  describe "#swap" do
    it "swaps elements of two adjacent cells" do
      cell1 = map.cell_at(1, 1)
      cell2 = map.cell_at(1, 2)

      cell1&.insert_element(factory.create_random)
      cell2&.insert_element(factory.create_random)

      e1 = cell1&.element
      e2 = cell2&.element

      result = map.swap(cell1, cell2)

      expect(result).to be true
      expect(cell1&.element).to eq(e2)
      expect(cell2&.element).to eq(e1)
    end

    it "does not swap elements of non-adjacent cells" do
      cell1 = map.cell_at(0, 0)
      cell2 = map.cell_at(2, 2)
      e1 = cell1&.element
      e2 = cell2&.element

      result = map.swap(cell1, cell2)

      expect(result).to be false
      expect(cell1&.element).to eq(e1)
      expect(cell2&.element).to eq(e2)
    end

    it "returns false if one of the cells is nil" do
      cell = map.cell_at(0, 0)
      result = map.swap(cell, nil)
      expect(result).to be false
    end
  end

  describe "#each_cell" do
    it "iterates over all 64 cells" do
      cells = []
      map.each_cell { |cell| cells << cell }
      expect(cells.size).to eq(64)
      expect(cells.all? { |c| c.is_a?(Cell) }).to be true
    end
  end

  describe "#fill_top_row_empty_cells" do
    it "fills cells with elements from factory" do
      map.fill_top_row_empty_cells(factory)
      map.instance_variable_get(:@grid)[0].each do |cell|
        expect(cell.element).to be_a(Element)
        expect(ElementFactory::TYPES).to include(cell.element.symbol)
      end
    end
  end

  describe "#horizontal_matches" do
    it "finds horizontal matches" do
      grid = [
        [cell(:a), cell(:a), cell(:a), cell(:b)],
        [cell(:b), cell(:c), cell(:d), cell(:e)],
        [cell(:f), cell(:b), cell(:b), cell(:b)]
      ]

      map = Map.new(grid)

      matches = map.send(:horizontal_matches)

      expect(matches.size).to eq(2)
      expect(matches[0].map(&:element).map(&:symbol)).to eq(%i[a a a])
      expect(matches[1].map(&:element).map(&:symbol)).to eq(%i[b b b])
    end
  end

  describe "#vertical_matches" do
    it "finds vertical matches" do
      grid = [
        [cell(:x), cell(:a)],
        [cell(:x), cell(:b)],
        [cell(:x), cell(:b)],
        [cell(:y), cell(:b)],
        [cell(:y), cell(:b)]
      ]
      map = Map.new(grid)

      matches = map.send(:vertical_matches)

      expect(matches.size).to eq(2)
      expect(matches[0].map(&:element).map(&:symbol)).to eq(%i[x x x])
      expect(matches[1].map(&:element).map(&:symbol)).to eq(%i[b b b b])
    end
  end

  describe "#all_matches" do
    it "merges intersecting horizontal and vertical matches" do
      grid = [
        [cell(:x), cell(:x), cell(:x), cell(:a)],
        [cell(:x), cell(:b), cell(:c), cell(:a)],
        [cell(:x), cell(:d), cell(:e), cell(:a)],
        [cell(:y), cell(:y), cell(:y), cell(:a)]
      ]
      map = Map.new(grid)

      matches = map.all_matches

      expect(matches.size).to eq(3)

      # First match — intersection of x elements in both vertical and horizontal directions
      first_match = matches.find { |m| m.any? { |c| c.element.symbol == :x } }
      expect(first_match&.map(&:element)&.map(&:symbol)&.tally).to eq({ x: 5 })

      # Second match — horizontal match of a elements
      second_match = matches.find { |m| m.any? { |c| c.element.symbol == :a } }
      expect(second_match&.map(&:element)&.map(&:symbol))&.to eq(%i[a a a a])

      # Third match — vertical match of a elements
      third_match = matches.find { |m| m.any? { |c| c.element.symbol == :y } }
      expect(third_match&.map(&:element)&.map(&:symbol))&.to eq(%i[y y y])
    end

    it "finds a single cross match of 5 identical elements" do
      grid = [
        [cell(:b), cell(:a), cell(:c)],
        [cell(:a), cell(:a), cell(:a)],
        [cell(:d), cell(:a), cell(:e)]
      ]
      map = Map.new(grid)

      matches = map.send(:all_matches)

      expect(matches.size).to eq(1)
      expect(matches[0].map(&:element).map(&:symbol)).to match_array(%i[a a a a a])
    end
  end

  describe "#has_matches?" do
    it "returns true if there are any matches" do
      grid = [
        [cell(:z), cell(:z), cell(:z)],
        [cell(:a), cell(:b), cell(:c)]
      ]
      map = Map.new(grid)

      expect(map.has_matches?).to eq(true)
    end

    it "returns false if there are no matches" do
      grid = [
        [cell(:a), cell(:b), cell(:c)],
        [cell(:d), cell(:e), cell(:f)]
      ]
      map = Map.new(grid)

      expect(map.has_matches?).to eq(false)
    end
  end
end
