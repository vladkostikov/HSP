require_relative "../state"

module FSM
  module States
    class SwapState < State
      def enter(context) end

      def update(context)
        cell1, cell2 = context.swap_cells

        if context.map.adjacent?(cell1, cell2)
          context.map.swap(cell1, cell2)
          context.state_machine.transition_to(:render)
        else
          context.state_machine.transition_to(:invalid_swap)
        end
      end
    end
  end
end
