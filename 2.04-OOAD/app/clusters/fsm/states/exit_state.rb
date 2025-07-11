require_relative "../state"

module FSM
  module States
    class ExitState < State
      def enter(_context)
        puts "👋 Спасибо за игру!"
        Kernel.exit(0)
      end
    end
  end
end
