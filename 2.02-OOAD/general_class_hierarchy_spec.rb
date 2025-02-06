require 'rspec'
require_relative 'general_class_hierarchy'

class User < Any
  attr_accessor :name, :contacts

  def initialize(name = "", contacts = {})
    @name = name
    @contacts = contacts
  end
end

RSpec.describe User do
  let(:name) { 'Alice' }
  let(:contacts) { { email: 'alice@example.com', phones: ['123', '456'] } }
  let(:user1) { User.new(name, contacts) }
  let(:user2) { User.new('Bob', { email: 'bob@example.com', phones: [] }) }

  describe '#initialize' do
    it 'raises NotImplementedError when trying to instantiate General' do
      expect { General.new }.to raise_error(NotImplementedError)
    end

    it 'allows instantiation of User' do
      expect { User.new }.not_to raise_error
    end
  end

  describe '#copy_to' do
    it 'copies all instance variables to another object' do
      user1.copy_to(user2)
      expect(user2.name).to eq(user1.name)
      expect(user2.contacts).to eq(user1.contacts)
    end

    it 'creates a deep copy of nested objects' do
      user1.copy_to(user2)
      user2.contacts[:phones] << '789'
      expect(user1.contacts[:phones]).not_to include('789')
    end
  end

  describe '#clone' do
    it 'creates a new object with the same data' do
      cloned_user = user1.clone
      expect(cloned_user).to be_a(User)
      expect(cloned_user).to eq(user1)
    end

    it 'creates a deep copy of nested objects' do
      cloned_user = user1.clone
      cloned_user.contacts[:phones] << '789'
      expect(user1.contacts[:phones]).not_to include('789')
    end
  end

  describe '#==' do
    it 'returns true for objects with the same data' do
      user2.name = user1.name
      user2.contacts = user1.contacts
      expect(user1).to eq(user2)
    end

    it 'returns false for objects with different data' do
      expect(user1).not_to eq(user2)
    end
  end

  describe '#serialize and .deserialize' do
    it 'serializes and deserializes an object' do
      data = user1.serialize
      deserialized_user = User.deserialize(data)
      expect(deserialized_user).to eq(user1)
    end
  end
end
