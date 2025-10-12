package task11_code_protection;

import java.math.BigDecimal;

/**
 * Task: Write code using any protection against potential future changes.
 * Ways: Interfaces and Dependency Injection, Polymorphism, Configuration.
 * Done: PaymentProcessor interface and CheckoutService with Dependency Injection,
 * PaymentProcessorFactory to select payment type (Card, SBP, Crypto).
 */
public interface PaymentProcessor {
    void processPayment(BigDecimal amount);
}

class CardProcessor implements PaymentProcessor {
    @Override
    public void processPayment(BigDecimal amount) {
        System.out.println("Processing card payment: " + amount + " RUB");
    }
}

class SBPProcessor implements PaymentProcessor {
    @Override
    public void processPayment(BigDecimal amount) {
        System.out.println("Processing SBP payment: " + amount + " RUB");
    }
}

class CryptoProcessor implements PaymentProcessor {
    @Override
    public void processPayment(BigDecimal amount) {
        System.out.println("Processing crypto payment: " + amount + " BTC");
    }
}

class PaymentProcessorFactory {
    public static PaymentProcessor createProcessor(String type) {
        switch (type.toLowerCase()) {
            case "card": return new CardProcessor();
            case "sbp": return new SBPProcessor();
            case "crypto": return new CryptoProcessor();
            default: throw new IllegalArgumentException("Unknown payment type: " + type);
        }
    }
}

class CheckoutService {
    private final PaymentProcessor processor;

    public CheckoutService(PaymentProcessor processor) {
        this.processor = processor;
    }

    public void process(BigDecimal amount) {
        processor.processPayment(amount);
    }
}

class Main {
    public static void main(String[] args) {
        CheckoutService checkout;

        PaymentProcessor processor = PaymentProcessorFactory.createProcessor("card");
        checkout = new CheckoutService(processor);
        checkout.process(new BigDecimal("120.00"));

        processor = PaymentProcessorFactory.createProcessor("sbp");
        checkout = new CheckoutService(processor);
        checkout.process(new BigDecimal("1500.00"));

        processor = PaymentProcessorFactory.createProcessor("crypto");
        checkout = new CheckoutService(processor);
        checkout.process(new BigDecimal("0.005"));
    }
}
