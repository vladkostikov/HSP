require 'colorize'

class ConsoleRenderer
  def initialize(map)
    @map = map
  end

  def render
    render_column_headers
    render_rows
  end

  private

  def render_column_headers
    print "    "
    ("A".."H").each { |x| print "#{x.to_s.rjust(2)}" }
    puts
  end

  def render_rows
    (0...Map::HEIGHT).each do |y|
      print (y + 1).to_s.rjust(2) + " |"
      (0...Map::WIDTH).each do |x|
        cell = @map.cell_at(x, y)
        print " #{format_element(cell.element)}"
      end
      puts
    end
  end

  def format_element(element)
    symbol = element.to_s
    color = element.color || :default
    symbol.colorize(color)
  end
end
