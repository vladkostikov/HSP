require_relative "../state"

module FSM
  module States
    class CheckMovesState < FSM::State
      def enter(context) end

      def update(context)
        if context.map.has_possible_moves?
          context.state_machine.transition_to(:score_matches)
        else
          puts "Ходов не осталось! Game over."
          context.state_machine.transition_to(:exit)
        end
      end
    end
  end
end
