require_relative '../../../clusters/game_field/element'

RSpec.describe Element do
  describe '#initialize' do
    it 'stores the symbol' do
      element = Element.new(:A, :green)
      expect(element.symbol).to eq(:A)
    end

    it 'stores the color' do
      element = Element.new(:A, :green)
      expect(element.color).to eq(:green)
    end
  end

  describe '#==' do
    it 'returns true for elements with the same symbol and the same color' do
      e1 = Element.new(:B, :green)
      e2 = Element.new(:B, :green)
      expect(e1.==(e2)).to be true
    end

    it 'returns false for elements with different symbols' do
      e1 = Element.new(:C, :green)
      e2 = Element.new(:D, :green)
      expect(e1.==(e2)).to be false
    end

    it 'returns false for elements with different colors' do
      e1 = Element.new(:B, :green)
      e2 = Element.new(:B, :red)
      expect(e1.==(e2)).to be false
    end

    it 'returns false if other is not an Element' do
      e = Element.new(:E, :green)
      expect(e.==(nil)).to be false
      expect(e.==(:E)).to be false
    end
  end

  describe '#to_s' do
    it 'returns symbol as string' do
      element = Element.new(:D, :green)
      expect(element.to_s).to eq('D')
    end
  end
end
