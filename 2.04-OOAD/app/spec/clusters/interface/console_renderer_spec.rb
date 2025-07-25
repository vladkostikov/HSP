require "stringio"
require_relative "../../../clusters/interface/console_renderer"
require_relative "../../../clusters/game_field/map"
require_relative "../../../clusters/game_field/cell"
require_relative "../../../clusters/game_field/element"
require_relative "../../../clusters/statistics/statistics"
require_relative "../../../clusters/bonus_system/bonus_manager"

RSpec.describe ConsoleRenderer do
  let(:map) { Map.new }
  let(:context) { Struct.new(:stats, :bonus_manager).new(Statistics.new, BonusManager.new) }
  subject { described_class.new(map: map, context: context) }

  before do
    # Заполним поле предсказуемыми элементами для теста
    (0...Map::WIDTH).each do |x|
      (0...Map::HEIGHT).each do |y|
        cell = map.cell_at(x, y)
        cell&.insert_element(Element.new("A", :green), force: true)
      end
    end
  end

  it "prints stats" do
    output = capture_stdout { subject.render }
    expect(output).to include("Очки: 0")
    expect(output).to include("Ходы: 0")
  end

  it "prints bonuses" do
    output = capture_stdout { subject.render }
    expect(output).to include("Бонусы: отсутствуют")
  end

  it "prints column headers" do
    output = capture_stdout { subject.render }
    expect(output).to include(("A".."H").to_a.join(" "))
  end

  it "prints row numbers and elements" do
    output = capture_stdout { subject.render }
    (1..Map::HEIGHT).each do |y|
      expect(output).to include(y.to_s.rjust(2))
    end

    expect(output).to include("A")
  end

  def capture_stdout(&block)
    original_stdout = $stdout
    $stdout = StringIO.new
    block.call
    $stdout.string
  ensure
    $stdout = original_stdout
  end
end
