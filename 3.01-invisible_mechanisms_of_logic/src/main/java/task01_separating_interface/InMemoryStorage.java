package task01_separating_interface;

import java.util.HashMap;
import java.util.Map;

public class InMemoryStorage implements Storage {
    private final Map<Integer, String> storage = new HashMap<>();
    private int counter = 0;

    @Override
    public void save(String data) {
        storage.put(counter++, data);
    }

    @Override
    public String retrieve(int id) {
        return storage.get(id);
    }
}
