require_relative "../state"

module FSM
  module States
    class InvalidSwapState < State
      def enter(context)
        context.map.swap(*context.swap_cells) if context.swap_cells
        context.swap_cells = nil
        puts "❌ Неверный ход! Попробуйте ещё раз."
        puts "Нажмите Enter для продолжения..."
        gets
        context.state_machine.transition_to(:render)
      end

      def update(context) end
    end
  end
end
