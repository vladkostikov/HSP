module FSM
  class StateMachine
    def initialize(context)
      @context = context
      @states = {}
      @transitions = Hash.new { |hash, key| hash[key] = [] }
      @current_state = nil
    end

    def add_state(name, state)
      @states[name] = state
    end

    def allow_transition(from:, to:)
      states = from.nil? ? [nil] : Array(from)
      states.each do |from_state|
        @transitions[from_state] << to
      end
    end

    def transition_to(name)
      raise "State #{name} not found" unless @states.key?(name)

      if @current_state
        from = @states.key(@current_state)
        allowed = @transitions[from]

        raise "Transition from #{from} to #{name} is not allowed" unless allowed.include?(name)
      end

      @current_state&.exit(@context)
      @current_state = @states[name]
      @current_state&.enter(@context)
    end

    def update
      @current_state&.update(@context)
    end
  end
end
