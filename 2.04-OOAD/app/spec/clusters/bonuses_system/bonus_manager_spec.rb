require_relative "../../../clusters/bonus_system/bonus_manager"

RSpec.describe BonusManager do
  let(:manager) { BonusManager.new }

  describe "#should_create_bonus?" do
    it "returns true for match size 4" do
      expect(manager.should_create_bonus?([1, 2, 3, 4])).to be true
    end

    it "returns true for match size greater than 4" do
      expect(manager.should_create_bonus?([1, 2, 3, 4, 5])).to be true
    end

    it "returns false for match size less than 4" do
      expect(manager.should_create_bonus?([1, 2, 3])).to be false
    end
  end

  describe "#create_bonus" do
    it "creates a RowBonus for match of 4" do
      manager.create_bonus([:a, :b, :c, :d])
      expect(manager.bonuses.last).to be_a(RowBonus)
    end

    it "creates a ColumnBonus for match of 5" do
      manager.create_bonus([:a, :b, :c, :d, :e])
      expect(manager.bonuses.last).to be_a(ColumnBonus)
    end

    it "creates a ColumnBonus for match of 6" do
      manager.create_bonus([:a] * 6)
      expect(manager.bonuses.last).to be_a(ColumnBonus)
    end

    it "creates a CrossBonus for match of 7" do
      manager.create_bonus([:a] * 7)
      expect(manager.bonuses.last).to be_a(CrossBonus)
    end

    it "creates a CrossBonus for match greater than 7" do
      manager.create_bonus([:a] * 10)
      expect(manager.bonuses.last).to be_a(CrossBonus)
    end

    it "does not create bonus for match smaller than 4" do
      result = manager.create_bonus([:a, :b, :c])
      expect(result).to be_nil
      expect(manager.bonuses).to be_empty
    end
  end
end
