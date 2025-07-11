require_relative "../../../clusters/game_field/cell"
require_relative "../../../clusters/game_field/element"
require_relative "../../../clusters/factory/element_factory"

RSpec.describe Cell do
  let(:element) { Element.new(:A, :green) }

  describe "#initialize" do
    it "stores coordinates and element" do
      cell = Cell.new(3, 4, element)
      expect(cell.x).to eq(3)
      expect(cell.y).to eq(4)
      expect(cell.element).to eq(element)
    end

    it "defaults element to nil if not given" do
      cell = Cell.new(1, 2)
      expect(cell.element).to be_nil
    end
  end

  describe "#clear" do
    it "removes the element from the cell" do
      cell = Cell.new(1, 1, element)
      cell.clear
      expect(cell.element).to be_nil
      expect(cell.empty?).to be true
    end

    it "does nothing if the cell is already empty" do
      cell = Cell.new(1, 1)
      expect { cell.clear }.not_to raise_error
      expect(cell.element).to be_nil
    end
  end

  describe "#empty?" do
    it "returns true when element is nil" do
      cell = Cell.new(0, 0)
      expect(cell.empty?).to be true
    end

    it "returns false when element is present" do
      cell = Cell.new(0, 0, element)
      expect(cell.empty?).to be false
    end
  end

  describe "#present?" do
    it "returns true if element is present" do
      cell = Cell.new(0, 0, element)
      expect(cell.present?).to be true
    end

    it "returns false if cell is empty" do
      cell = Cell.new(0, 0)
      expect(cell.present?).to be false
    end
  end

  describe "#insert_element" do
    it "inserts into empty cell" do
      cell = Cell.new(0, 0)
      cell.insert_element(element)
      expect(cell.element).to eq(element)
    end

    it "raises if inserting into occupied cell without force" do
      cell = Cell.new(0, 0, element)
      expect do
        cell.insert_element(ElementFactory.new.create_random)
      end.to raise_error(RuntimeError, /already occupied/)
    end

    it "overwrites element if force is true" do
      cell = Cell.new(0, 0, element)
      new_element = ElementFactory.new.create_random
      cell.insert_element(new_element, force: true)
      expect(cell.element).to eq(new_element)
    end
  end

  describe "#match?" do
    let(:element_a1) { Element.new(:a, :green) }
    let(:element_a2) { Element.new(:a, :green) }
    let(:element_b) { Element.new(:b, :green) }

    it "returns true when both cells have equal elements" do
      cell1 = Cell.new(0, 0, element_a1)
      cell2 = Cell.new(1, 0, element_a2)
      expect(cell1.match?(cell2)).to be true
    end

    it "returns false when elements differ" do
      cell1 = Cell.new(0, 0, element_a1)
      cell2 = Cell.new(1, 0, element_b)
      expect(cell1.match?(cell2)).to be false
    end

    it "returns false when other cell is nil" do
      cell = Cell.new(0, 0, element_a1)
      expect(cell.match?(nil)).to be false
    end

    it "returns false if self has nil element" do
      cell1 = Cell.new(0, 0)
      cell2 = Cell.new(1, 0, element_a1)
      expect(cell1.match?(cell2)).to be false
    end

    it "returns false if both have nil elements" do
      cell1 = Cell.new(0, 0)
      cell2 = Cell.new(1, 0)
      expect(cell1.match?(cell2)).to be false
    end
  end
end
