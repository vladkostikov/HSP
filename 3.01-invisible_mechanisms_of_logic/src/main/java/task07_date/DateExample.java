package task07_date;

import java.time.*;
import java.time.format.DateTimeFormatter;

/**
 * Task: to improve the code.
 * Changes: switched from Date/SimpleDateFormat to java.time (thread-safe, with explicit timezone)
 */
public class DateExample {
    public static void main(String[] args) {
        String dateString = "2024-05-13 14:30:00";

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        ZoneId zone = ZoneId.of("Europe/Moscow");

        LocalDateTime localDateTime = LocalDateTime.parse(dateString, formatter);
        ZonedDateTime zonedDateTime = localDateTime.atZone(zone);

        System.out.println("LocalDateTime: " + localDateTime);
        System.out.println("ZonedDateTime: " + zonedDateTime);
    }
}
