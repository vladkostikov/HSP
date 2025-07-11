module FSM
  class State
    # Вызывается при входе в состояние
    def enter(context)
      raise NotImplementedError, "#{self.class}#enter must be implemented"
    end

    # Вызывается при выходе из состояния
    def exit(_context) end

    # Обновление состояния (если нужно)
    def update(_context) end
  end
end
