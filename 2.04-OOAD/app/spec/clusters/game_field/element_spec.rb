require_relative '../../../clusters/game_field/element'

RSpec.describe Element do
  describe '#initialize' do
    it 'stores the symbol' do
      element = Element.new(:A)
      expect(element.symbol).to eq(:A)
    end
  end

  describe '#==' do
    it 'returns true for elements with the same symbol' do
      e1 = Element.new(:B)
      e2 = Element.new(:B)
      expect(e1.==(e2)).to be true
    end

    it 'returns false for elements with different symbols' do
      e1 = Element.new(:C)
      e2 = Element.new(:D)
      expect(e1.==(e2)).to be false
    end

    it 'returns false if other is not an Element' do
      e = Element.new(:E)
      expect(e.==(nil)).to be false
      expect(e.==(:E)).to be false
    end
  end

  describe '#to_s' do
    it 'returns symbol as string' do
      element = Element.new(:D)
      expect(element.to_s).to eq('D')
    end
  end
end
