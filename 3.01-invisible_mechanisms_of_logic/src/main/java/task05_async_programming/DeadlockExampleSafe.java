package task05_async_programming;

/**
 * Исправленная версия DeadlockExample.
 *
 * В предыдущей версии два потока захватывали lock1 и lock2 в разном порядке, что могло привести
 * к взаимной блокировке.
 *
 * В этой версии все потоки захватывают блокировки в одном и том же порядке, что исключает deadlock.
 */
public class DeadlockExampleSafe {

    private static final Object lock1 = new Object();
    private static final Object lock2 = new Object();

    public static void run() throws InterruptedException {
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1 acquired lock1");
                try { Thread.sleep(50); } catch (InterruptedException e) { e.printStackTrace(); }

                synchronized (lock2) {
                    System.out.println("Thread 1 acquired lock2");
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 2 acquired lock1");
                try { Thread.sleep(50); } catch (InterruptedException e) { e.printStackTrace(); }

                synchronized (lock2) {
                    System.out.println("Thread 2 acquired lock2");
                }
            }
        });

        thread1.start();
        thread2.start();

        thread1.join();
        thread2.join();
    }
}
