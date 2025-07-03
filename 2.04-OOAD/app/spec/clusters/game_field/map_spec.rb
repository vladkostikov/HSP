require_relative '../../../clusters/game_field/map'
require_relative '../../../clusters/game_field/cell'
require_relative '../../../clusters/game_field/element'
require_relative '../../../clusters/factory/element_factory'

RSpec.describe Map do
  let(:factory) { ElementFactory.new }
  let(:map) { Map.new(factory) }

  describe '#initialize' do
    it 'creates a grid of 8x8 cells' do
      expect(map.instance_variable_get(:@grid).size).to eq(8)
      expect(map.instance_variable_get(:@grid).all? { |row| row.size == 8 }).to be true
    end

    it 'fills cells with elements from factory' do
      map.each_cell do |cell|
        expect(cell.element).to be_a(Element)
        expect(ElementFactory::TYPES).to include(cell.element.symbol)
      end
    end
  end

  describe '#cell_at' do
    it 'returns correct cell for valid coordinates' do
      cell = map.cell_at(3, 4)
      expect(cell).to be_a(Cell)
      expect(cell.x).to eq(3)
      expect(cell.y).to eq(4)
    end

    it 'returns nil for out-of-bound coordinates' do
      expect(map.cell_at(-1, 0)).to be_nil
      expect(map.cell_at(0, -1)).to be_nil
      expect(map.cell_at(8, 0)).to be_nil
      expect(map.cell_at(0, 8)).to be_nil
    end
  end

  describe '#swap' do
    it 'swaps elements of two adjacent cells' do
      cell1 = map.cell_at(1, 1)
      cell2 = map.cell_at(1, 2)
      e1 = cell1.element
      e2 = cell2.element

      result = map.swap(cell1, cell2)

      expect(result).to be true
      expect(cell1.element).to eq(e2)
      expect(cell2.element).to eq(e1)
    end

    it 'does not swap elements of non-adjacent cells' do
      cell1 = map.cell_at(0, 0)
      cell2 = map.cell_at(2, 2)
      e1 = cell1.element
      e2 = cell2.element

      result = map.swap(cell1, cell2)

      expect(result).to be false
      expect(cell1.element).to eq(e1)
      expect(cell2.element).to eq(e2)
    end

    it 'returns false if one of the cells is nil' do
      cell = map.cell_at(0, 0)
      result = map.swap(cell, nil)
      expect(result).to be false
    end
  end

  describe '#each_cell' do
    it 'iterates over all 64 cells' do
      cells = []
      map.each_cell { |cell| cells << cell }
      expect(cells.size).to eq(64)
      expect(cells.all? { |c| c.is_a?(Cell) }).to be true
    end
  end
end
