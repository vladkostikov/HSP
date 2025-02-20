# Bad
class Payment
  attr_reader :amount, :method

  def initialize(amount, method)
    @amount = amount
    @method = method
  end

  def process
    case method
    when "cash"
      "Processing cash payment of #{amount}"
    when "credit_card"
      "Processing credit card payment of #{amount}"
    when "crypto"
      "Processing crypto payment of #{amount}"
    else
      raise ArgumentError, "Unknown payment method"
    end
  end
end

payment = Payment.new(10, "cash")
puts payment.process

# Good
class Payment
  attr_reader :amount

  def initialize(amount)
    @amount = amount
  end

  def process
    raise NotImplementedError
  end
end

class CashPayment < Payment
  def process
    "Processing cash payment of #{amount}"
  end
end

class CreditCardPayment < Payment
  def process
    "Processing credit card payment of #{amount}"
  end
end

class CryptoPayment < Payment
  def process
    "Processing crypto payment of #{amount}"
  end
end

payments = [
  CashPayment.new(100),
  CreditCardPayment.new(200),
  CryptoPayment.new(300)
]
payments.each { |payment| puts payment.process }
