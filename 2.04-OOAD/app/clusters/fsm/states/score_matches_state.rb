require_relative "../state"

module FSM
  module States
    class ScoreMatchesState < State
      def enter(context)
        matches = context.map.all_matches
        total_score = matches.map(&:size)
                             .map { |match_size| context.stats.calculate_score(match_size) }
                             .sum

        context.stats.increment_score(total_score) if total_score.positive?
      end

      def update(context)
        context.state_machine.transition_to(:create_bonus)
      end
    end
  end
end
