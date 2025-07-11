require_relative "../state"

module FSM
  module States
    class InputState < State
      def enter(context) end

      def update(context)
        puts "\nВведите координаты двух элементов для перестановки (A1 B2), 'b' для активации бонусов, 'q' для выхода:"
        print "> "
        input = gets.chomp.strip

        if input.downcase == "b"
          context.state_machine.transition_to(:activate_bonus)
          return
        end

        if input.downcase == "q"
          context.state_machine.transition_to(:exit)
          return
        end

        x1, y1, x2, y2 = parse_input(input)

        if valid_coordinates?(x1, y1, x2, y2)
          cell1 = context.map.cell_at(x1, y1)
          cell2 = context.map.cell_at(x2, y2)

          context.swap_cells = [cell1, cell2]

          context.state_machine.transition_to(:swap)
        else
          context.state_machine.transition_to(:invalid_swap)
        end
      end

      private

      def parse_input(input)
        parts = input.strip.upcase.split

        return [nil, nil, nil, nil] unless parts.size == 2 && parts.all? { |s| s.match?(/^[A-H][1-8]$/) }

        coordinates = parts.map do |coord|
          col_letter = coord[0]
          row_number = coord[1].to_i

          x = ("A".."H").to_a.index(col_letter)
          y = row_number - 1

          [x, y]
        end

        coordinates.flatten
      end

      def valid_coordinates?(*coordinates)
        coordinates.size == 4 && coordinates.none?(nil) && coordinates.all? { |n| n.between?(0, 7) }
      end
    end
  end
end
