require_relative "clusters/bonus_system/bonus_manager"
require_relative "clusters/factory/element_factory"
require_relative "clusters/game_field/map"
require_relative "clusters/interface/console_renderer"
require_relative "clusters/statistics/statistics"
require_relative "clusters/fsm/state_machine"
Dir[File.join(__dir__, "clusters/fsm/states/*.rb")].each do |file|
  require_relative file
end

class Game
  attr_accessor :swap_cells, :next_state
  attr_reader :map, :renderer, :stats, :factory, :bonus_manager, :state_machine

  def initialize
    @map = Map.new
    @renderer = ConsoleRenderer.new(context: self)
    @stats = Statistics.new
    @factory = ElementFactory.new
    @bonus_manager = BonusManager.new
    @state_machine = FSM::StateMachine.new(self)

    add_states
    allow_transitions
  end

  def start
    @state_machine.transition_to(:fill)
    loop do
      @state_machine.update
    end
  end

  private

  def add_states
    states = {
      activate_bonus: FSM::States::ActivateBonusState.new,
      check_moves: FSM::States::CheckMovesState.new,
      collapse: FSM::States::CollapseElementsState.new,
      create_bonus: FSM::States::CreateBonusState.new,
      exit: FSM::States::ExitState.new,
      fill: FSM::States::FillState.new,
      input: FSM::States::InputState.new,
      invalid_swap: FSM::States::InvalidSwapState.new,
      remove_matches: FSM::States::RemoveMatchesState.new,
      render: FSM::States::RenderState.new,
      score_matches: FSM::States::ScoreMatchesState.new,
      swap: FSM::States::SwapState.new
    }

    states.each { |name, state| @state_machine.add_state(name, state) }
  end

  def allow_transitions
    @state_machine.allow_transition from: [:activate_bonus, :input, :render], to: :activate_bonus
    @state_machine.allow_transition from: [:render], to: :check_moves
    @state_machine.allow_transition from: [:render], to: :collapse
    @state_machine.allow_transition from: [:score_matches], to: :create_bonus
    @state_machine.allow_transition from: [:check_moves, :input], to: :exit
    @state_machine.allow_transition from: [nil, :render], to: :fill
    @state_machine.allow_transition from: [:remove_matches], to: :input
    @state_machine.allow_transition from: [:remove_matches, :input, :swap], to: :invalid_swap
    @state_machine.allow_transition from: [:create_bonus], to: :remove_matches
    @state_machine.allow_transition from: [:fill, :swap, :collapse, :invalid_swap, :remove_matches, :activate_bonus],
                                    to: :render
    @state_machine.allow_transition from: [:render, :check_moves], to: :score_matches
    @state_machine.allow_transition from: [:input], to: :swap
  end
end
