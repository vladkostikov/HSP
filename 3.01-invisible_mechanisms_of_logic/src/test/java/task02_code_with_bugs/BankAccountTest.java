package task02_code_with_bugs;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BankAccountTest {
    private BankAccount account;

    @BeforeEach
    public void setUp() {
        account = new BankAccount(1000);
    }

    @Test
    public void testDeposit() {
        System.out.println("Initial balance: " + account.getBalance());
        account.deposit(300);
        assertEquals(1300, account.getBalance());
        System.out.println("After deposit 300: " + account.getBalance());
    }
    
    @Test
    public void testWithdraw() {
        System.out.println("Initial balance: " + account.getBalance());
        account.withdraw(300);
        assertEquals(700, account.getBalance());
        System.out.println("After withdraw 300: " + account.getBalance());
    }

    @Test
    public void testDepositWithNegativeAmount() {
        System.out.println("Initial balance: " + account.getBalance());
        assertThrows(IllegalArgumentException.class, () -> account.withdraw(-2000));
        assertEquals(1000, account.getBalance());
        System.out.println("After withdraw -2000: " + account.getBalance());
    }

    @Test
    public void testWithdrawWithNegativeAmount() {
        System.out.println("Initial balance: " + account.getBalance());
        assertThrows(IllegalArgumentException.class, () -> account.withdraw(-10000));
        assertEquals(1000, account.getBalance());
        System.out.println("After withdraw -10000: " + account.getBalance());
    }
}
