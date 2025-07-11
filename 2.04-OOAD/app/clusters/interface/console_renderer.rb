require "colorize"
require_relative "../statistics/statistics"

class ConsoleRenderer
  def initialize(context: nil, map: nil)
    @map = map || context&.map
    @context = context
  end

  def render
    render_stats
    render_bonuses
    render_column_headers
    render_rows
  end

  private

  def render_stats
    puts "Очки: #{@context&.stats&.score}"
    puts "Ходы: #{@context&.stats&.moves}"
  end

  def render_bonuses
    bonuses = @context&.bonus_manager&.bonuses || []

    if bonuses.empty?
      puts "Бонусы: отсутствуют"
    else
      list = bonuses.each_with_index.map do |bonus, index|
        "#{index + 1}: #{bonus.class.name}"
      end
      puts "Бонусы: #{list.join(', ')}"
    end
  end

  def render_column_headers
    print "    "
    ("A".."H").each { |x| print x.to_s.rjust(2) }
    puts
  end

  def render_rows
    (0...Map::HEIGHT).each do |y|
      print "#{(y + 1).to_s.rjust(2)} |"
      (0...Map::WIDTH).each do |x|
        cell = @map.cell_at(x, y)
        print " #{format_element(cell.element)}"
      end
      puts
    end
  end

  def format_element(element)
    return " " if element.nil?

    symbol = element.to_s
    color = element.color || :default
    symbol.colorize(color)
  end
end
