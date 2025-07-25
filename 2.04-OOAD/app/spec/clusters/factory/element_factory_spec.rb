require_relative "../../../clusters/factory/element_factory"

RSpec.describe ElementFactory do
  let(:factory) { ElementFactory.new }

  describe "#create_random" do
    it "returns an Element" do
      element = factory.create_random
      expect(element).to be_a(Element)
    end

    it "returns an Element with a valid symbol" do
      10.times do
        element = factory.create_random
        expect(ElementFactory::TYPES).to include(element.symbol)
      end
    end

    it "returns different elements over multiple calls" do
      elements = 100.times.map { factory.create_random.symbol }
      expect(elements.uniq.length).to be > 1
    end
  end
end
