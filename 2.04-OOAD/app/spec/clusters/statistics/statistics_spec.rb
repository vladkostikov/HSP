require_relative "../../../clusters/statistics/statistics"

RSpec.describe Statistics do
  let(:stats) { Statistics.new }

  describe "#increment_score" do
    it "adds to the total score" do
      expect { stats.increment_score(50) }.to change { stats.score }.by(50)
    end
  end

  describe "#increment_moves" do
    it "increments moves count" do
      expect { stats.increment_moves }.to change { stats.moves }.by(1)
    end
  end

  describe "#decrement_moves" do
    it "decrements moves count" do
      stats.increment_moves
      expect { stats.decrement_moves }.to change { stats.moves }.by(-1)
    end
  end

  describe "#calculate_score" do
    it "returns 0 if match size less than 3" do
      expect(stats.calculate_score(2)).to eq(0)
    end

    it "calculates score correctly for match size 3" do
      expect(stats.calculate_score(3)).to eq(3 * (10 + (5 * (3 - 3)))) # 3 * 10 = 30
    end

    it "calculates score correctly for match size 4" do
      expect(stats.calculate_score(4)).to eq(4 * (10 + (5 * (4 - 3)))) # 4 * 15 = 60
    end

    it "calculates score correctly for match size 5" do
      expect(stats.calculate_score(5)).to eq(5 * (10 + (5 * (5 - 3)))) # 5 * 20 = 100
    end

    it "calculates score correctly for match size 6" do
      expect(stats.calculate_score(6)).to eq(6 * (10 + (5 * (6 - 3)))) # 6 * 25 = 150
    end
  end
end
