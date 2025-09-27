package task06_async_programming;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * WebsiteCounter simulates counting visitors with AtomicInteger
 * to safely handle multiple threads.
 */
class WebsiteCounter
{
    private final AtomicInteger visitors = new AtomicInteger(0);

   public void visit(String visitorName) {
       int count = visitors.incrementAndGet();
       System.out.println(visitorName + " visited, total visitors: " + count);
   }
}

public class AtomicIntegerWebsiteExample {
    public static void main(String[] args) {
        WebsiteCounter counter = new WebsiteCounter();

        for (int i = 0; i < 10; i++) {
            String visitorName = "User-" + i;
            new Thread(() -> counter.visit(visitorName)).start();
        }
    }
}
