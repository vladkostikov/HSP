package task01_separating_interface;

import java.sql.*;

public class StorageTest {
    public static void main(String[] args) {
        Storage memoryStorage = new InMemoryStorage();
        testStorage(memoryStorage);

        try (Connection connection = DriverManager.getConnection("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1")) {
            try (Statement stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE storage (id INT AUTO_INCREMENT(0,1) PRIMARY KEY, data VARCHAR(255))");
            }

            Storage databaseStorage = new DatabaseStorage(connection);
            testStorage(databaseStorage);

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void testStorage(Storage storage) {
        storage.save("Hello, World!");
        storage.save("Second string");

        String data1 = storage.retrieve(0);
        String data2 = storage.retrieve(1);

        System.out.println("Retrieved data1: " + data1);
        System.out.println("Retrieved data2: " + data2);
    }
}
