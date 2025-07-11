require_relative "../state"

module FSM
  module States
    class RenderState < State
      def enter(context)
        clear_screen
        context.renderer.render
      end

      def update(context)
        next_state = context.next_state || :score_matches
        context.next_state = nil
        context.state_machine.transition_to(next_state)
      end

      private

      def clear_screen
        sleep(0.3)
        system("clear") || system("cls")
      end
    end
  end
end
