require_relative "../game"
require "rspec"

RSpec.describe Game do
  subject(:game) { Game.new }

  describe "#initialize" do
    it "initializes map, renderer, stats, factory, bonus_manager and state_machine" do
      expect(game.map).to be_a(Map)
      expect(game.renderer).to be_a(ConsoleRenderer)
      expect(game.stats).to be_a(Statistics)
      expect(game.factory).to be_a(ElementFactory)
      expect(game.bonus_manager).to be_a(BonusManager)
      expect(game.state_machine).to be_a(FSM::StateMachine)
    end

    it "adds all states to the state machine" do
      expected_states = [
        :activate_bonus, :check_moves, :collapse, :create_bonus, :exit,
        :fill, :input, :invalid_swap, :remove_matches, :render,
        :score_matches, :swap
      ]
      expect(game.state_machine.instance_variable_get(:@states).keys).to match_array(expected_states)
    end

    it "sets up allowed transitions correctly" do
      transitions = game.state_machine.instance_variable_get(:@transitions)

      expect(transitions[:activate_bonus]).to include(:activate_bonus, :render)
      expect(transitions[:input]).to include(:activate_bonus, :exit, :invalid_swap, :swap)
      expect(transitions[nil]).to include(:fill)
      expect(transitions[:remove_matches]).to include(:input, :invalid_swap, :render)
      expect(transitions[:create_bonus]).to include(:remove_matches)
    end
  end

  describe "#start" do
    it "transitions to :fill state on start" do
      expect(game.state_machine).to receive(:transition_to).with(:fill)
      # raise an exception to exit the infinite loop after the first update.
      allow(game.state_machine).to receive(:update).and_raise("stop loop")

      expect { game.start }.to raise_error("stop loop")
    end
  end
end
