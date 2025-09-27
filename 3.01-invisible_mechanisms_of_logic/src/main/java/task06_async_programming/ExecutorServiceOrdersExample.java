package task06_async_programming;

import java.util.concurrent.*;

/**
 * OnlineStore simulates order processing with ExecutorService
 * to handle multiple orders concurrently.
 */
class OnlineStore {
    private final ExecutorService executor = Executors.newFixedThreadPool(3);

    public void processOrder(String orderName) {
        executor.submit(() -> {
            try {
                System.out.println("Processing " + orderName);
                Thread.sleep(2000);
                System.out.println("Completed " + orderName);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
    }

    public void shutdown() {
        executor.shutdown();
        try {
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
        }
    }
}

public class ExecutorServiceOrdersExample {
    public static void main(String[] args) {
        OnlineStore store = new OnlineStore();

        for (int i = 0; i < 10; i++) {
            String orderName = "Order" + i;
            store.processOrder(orderName);
        }

        store.shutdown();
    }
}
