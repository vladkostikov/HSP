package task06_async_programming;

import java.util.concurrent.CompletableFuture;

/**
 * TaskQueue simulates a reactive task queue using CompletableFuture
 * to process tasks asynchronously.
 */
class TaskQueue {
    public void submitTask(String taskName) {
        CompletableFuture.supplyAsync(() -> {
            System.out.println("Processing " + taskName);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return taskName + " completed";
        }).thenAccept(System.out::println);
    }
}


public class CompletableFutureQueueExample {
    public static void main(String[] args) throws InterruptedException {
        TaskQueue queue = new TaskQueue();

        for (int i = 0; i < 10; i++) {
            String taskName = "Task-" + i;
            queue.submitTask(taskName);
        }

        Thread.sleep(2000);
    }
}
