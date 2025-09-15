package task01_separating_interface;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class FileStorage implements Storage {
    private final File file = new File("storage.txt");
    private Map<Integer, String> storage = new HashMap<>();

    public FileStorage() {
        loadFromFile();
    }

    @Override
    public void save(String data) {
        storage.put(storage.size(), data);
        saveToFile();
    }

    @Override
    public String retrieve(int id) {
        return storage.get(id);
    }

    private void saveToFile() {
        try (ObjectOutputStream oos =
                     new ObjectOutputStream(new FileOutputStream(file))) {
            oos.writeObject(storage);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @SuppressWarnings("unchecked")
    private void loadFromFile() {
        if (!file.exists()) return;

        try (ObjectInputStream ois =
                     new ObjectInputStream(new FileInputStream(file))) {
            storage = (Map<Integer, String>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
