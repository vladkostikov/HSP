require_relative 'clusters/game_field/map'
require_relative 'clusters/interface/console_renderer'

class App
  def initialize
    @map = Map.new
    @renderer = ConsoleRenderer.new(@map)
  end

  def start
    loop do
      clear_screen
      @renderer.render

      puts "\nВведите координаты двух элементов для перестановки (A1 A2) или 'q' для выхода:"
      print "> "
      input = gets.chomp.strip

      break if input.downcase == 'q'

      x1, y1, x2, y2 = parse_input(input)

      unless valid_coordinates?(x1, y1, x2, y2)
        puts "❌ Неверный формат. Используйте: A1 B1 (буквы A–H, цифры 1–8)"
        wait_for_keypress
        next
      end

      cell1 = @map.cell_at(x1, y1)
      cell2 = @map.cell_at(x2, y2)

      if @map.adjacent?(cell1, cell2)
        @map.swap(cell1, cell2)
        puts "\n✅ Перестановка выполнена:"
        @renderer.render
        wait_for_keypress
      else
        puts "❌ Эти элементы не соседние!"
        wait_for_keypress
        next
      end
    end

    puts "\n👋 Игра завершена."
  end

  private

  def clear_screen
    system('clear') || system('cls')
  end

  def wait_for_keypress
    puts "\nНажмите Enter для продолжения..."
    gets
  end

  def parse_input(input)
    parts = input.strip.upcase.split

    return nil unless parts.size == 2 && parts.all? { |s| s.match?(/^[A-H][1-8]$/) }

    coordinates = parts.map do |coord|
      col_letter = coord[0]
      row_number = coord[1].to_i

      x = ('A'..'H').to_a.index(col_letter)
      y = row_number - 1

      [x, y]
    end

    coordinates.flatten
  end

  def valid_coordinates?(*coordinates)
    coordinates.size == 4 && coordinates.none?(nil) &&  coordinates.all? { |n| n.between?(0, 7) }
  end
end

App.new.start
