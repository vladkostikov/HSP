package task06_async_programming;

import java.util.concurrent.locks.ReentrantLock;

/**
 * Cinema simulates a ticket booking system with ReentrantLock
 * to avoid double booking the same seat.
 */
class Cinema {
    private final boolean[] seats;
    private final ReentrantLock lock = new ReentrantLock();

    public Cinema(int numberOfSeats) {
        this.seats = new boolean[numberOfSeats];
    }

    public void bookSeat(String threadName, int seatNumber) {
        lock.lock();
        try {
            if (!seats[seatNumber]) {
                System.out.println(threadName + " successfully booked a seat" + seatNumber);
                seats[seatNumber] = true;
            } else {
                System.out.println(threadName + " failed to book seat" + seatNumber + "(already taken)");
            }
        } finally {
                lock.unlock();
        }
    }
}

public class ReentrantLockCinemaExample {
    public static void main(String[] args) {
        Cinema cinema = new Cinema(5);

        for (int i = 0; i < 10; i++) {
            String threadName = "User-" + i;
            int seatNumber = i % 5;
            new Thread(() -> cinema.bookSeat(threadName, seatNumber)).start();
        }
    }
}
