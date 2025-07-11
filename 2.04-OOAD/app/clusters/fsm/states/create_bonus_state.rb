module FSM
  module States
    class CreateBonusState < State
      def enter(context)
        matches = context.map.all_matches

        matches.each do |match|
          next unless context.bonus_manager.should_create_bonus?(match)

          context.bonus_manager.create_bonus(match)
        end
      end

      def update(context)
        context.state_machine.transition_to(:remove_matches)
      end
    end
  end
end
