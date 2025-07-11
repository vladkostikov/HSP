require_relative "../../../clusters/fsm/state_machine"

RSpec.describe FSM::StateMachine do
  let(:context) { double("context") }
  let(:state_machine) { FSM::StateMachine.new(context) }

  let(:state_a) { double("state_a") }
  let(:state_b) { double("state_b") }

  before do
    state_machine.add_state(:a, state_a)
    state_machine.add_state(:b, state_b)

    # Allow transitions
    state_machine.allow_transition(from: nil, to: :a) # initial state
    state_machine.allow_transition(from: :a, to: :b)
    state_machine.allow_transition(from: :b, to: :a)
  end

  describe "#add_state" do
    it "adds states correctly" do
      states = state_machine.instance_variable_get(:@states)
      expect(states).to include(a: state_a, b: state_b)
    end
  end

  describe "#allow_transition" do
    it "allows transitions between states" do
      transitions = state_machine.instance_variable_get(:@transitions)

      expect(transitions[nil]).to include(:a)
      expect(transitions[:a]).to include(:b)
      expect(transitions[:b]).to include(:a)
    end
  end

  describe "#transition_to" do
    context "when transitioning to an existing allowed state" do
      it "calls exit on the current state and enter on the new state" do
        allow(state_a).to receive(:enter)
        allow(state_a).to receive(:exit)
        allow(state_b).to receive(:enter)
        allow(state_b).to receive(:exit)

        # First transition - no current state, only enter called on :a
        state_machine.transition_to(:a)
        expect(state_a).to have_received(:enter).with(context)
        expect(state_a).not_to have_received(:exit)

        # Transition from :a to :b calls exit on :a and enter on :b
        state_machine.transition_to(:b)
        expect(state_a).to have_received(:exit).with(context)
        expect(state_b).to have_received(:enter).with(context)
      end
    end

    context "when transitioning to a non-existent state" do
      it "raises an error" do
        expect { state_machine.transition_to(:nonexistent) }.to raise_error("State nonexistent not found")
      end
    end

    context "when transitioning to a disallowed state" do
      it "raises an error" do
        allow(state_a).to receive(:enter)
        state_machine.transition_to(:a)
        # Trying to transition from :a to :a again, which is not allowed
        expect { state_machine.transition_to(:a) }.to raise_error("Transition from a to a is not allowed")
      end
    end
  end

  describe "#update" do
    it "calls update on the current state" do
      allow(state_a).to receive(:enter)
      allow(state_a).to receive(:update)
      state_machine.transition_to(:a)
      state_machine.update
      expect(state_a).to have_received(:update).with(context)
    end

    it "does nothing if there is no current state" do
      expect { state_machine.update }.not_to raise_error
    end
  end
end
