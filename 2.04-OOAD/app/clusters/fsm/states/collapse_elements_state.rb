require_relative "../state"

module FSM
  module States
    class CollapseElementsState < State
      def enter(context)
        collapse_map(context.map)
      end

      def update(context)
        context.next_state = :fill if context.map.has_empty_cells?
        context.state_machine.transition_to(:render)
      end

      private

      def collapse_map(map)
        (0...map.width).each do |x|
          collapse_column(map, x)
        end
      end

      def collapse_column(map, x)
        column = (0...map.height).map { |y| map.cell_at(x, y) }

        # Извлекаем все элементы, сохраняя порядок
        elements = column.select(&:present?).map(&:element)

        empty_count = column.size - elements.size

        column.each_with_index do |cell, idx|
          if idx < empty_count
            cell.clear
          else
            cell.insert_element(elements[idx - empty_count], force: true)
          end
        end
      end
    end
  end
end
