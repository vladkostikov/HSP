require_relative "../state"
require_relative "../../factory/element_factory"

module FSM
  module States
    class FillState < FSM::State
      def enter(context)
        context.map.fill_top_row_empty_cells(ElementFactory.new)
      end

      def update(context)
        context.next_state = if context.map.has_empty_cells?
                               :collapse
                             else
                               :check_moves
                             end

        context.state_machine.transition_to(:render)
      end
    end
  end
end
