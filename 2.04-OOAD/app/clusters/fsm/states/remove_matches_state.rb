require_relative "../state"

module FSM
  module States
    class RemoveMatchesState < State
      def enter(context) end

      def update(context)
        if context.map.has_matches?
          puts "Есть комбинации, приступаю к удалению!\n\n"

          context.map.remove_matches!

          unless context.swap_cells.nil?
            context.stats.increment_moves
            context.swap_cells = nil
          end

          context.next_state = :collapse
          context.state_machine.transition_to(:render)
        else
          return context.state_machine.transition_to(:input) if context.swap_cells.nil?

          context.state_machine.transition_to(:invalid_swap)
        end
      end
    end
  end
end
