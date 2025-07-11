require_relative "../state"

module FSM
  module States
    class ActivateBonusState < State
      def enter(_context); end

      def update(context)
        bonuses = context.bonus_manager.bonuses

        if bonuses.empty?
          puts "Нет бонусов для активации."
          puts "Нажмите Enter."
          gets
          return context.state_machine.transition_to(:render)
        end

        print "Введите номер бонуса и ячейку (например, 2 B5): "
        @input = gets&.strip

        return context.state_machine.transition_to(:render) if @input.nil? || @input&.empty?

        match = @input.match(/^(\d+)\s*([A-Za-z])(\d+)$/)
        unless match
          puts "Неверный формат ввода. Используйте такой формат: 2 B5"
          puts "Нажмите Enter."
          gets
          context.next_state = :activate_bonus
          return context.state_machine.transition_to(:render)
        end

        bonus_index = match[1].to_i - 1
        col_letter = match[2].upcase
        row_number = match[3].to_i

        x = col_letter.ord - "A".ord
        y = row_number - 1

        if bonus_index.negative? || bonus_index >= bonuses.size
          puts "Неверный номер бонуса ввода."
          puts "Нажмите Enter."
          gets
          context.next_state = :activate_bonus
          return context.state_machine.transition_to(:render)
        end

        if context.map.cell_at(x, y).nil?
          puts "Неверная ячейка."
          puts "Нажмите Enter"
          gets
          context.next_state = :activate_bonus
          return context.state_machine.transition_to(:render)
        end

        selected_bonus = bonuses[bonus_index]
        cleared_cells = selected_bonus.activate(context.map, context.map.cell_at(x, y))
        bonuses.delete_at(bonus_index)

        context.stats.increment_score(context.stats.calculate_score(cleared_cells.size)) if cleared_cells.any?

        context.next_state = :fill
        context.state_machine.transition_to(:render)
      end
    end
  end
end
