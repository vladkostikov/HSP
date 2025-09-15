package task01_separating_interface;

public class Main {
    public static void main(String[] args) {
        Storage memoryStorage = new InMemoryStorage();
        memoryStorage.save("Data in memory");
        System.out.println("InMemoryStorage: " + memoryStorage.retrieve(0));

        Storage fileStorage = new FileStorage();
        fileStorage.save("Data in file");
        System.out.println("FileStorage: " + fileStorage.retrieve(0));
    }
}
