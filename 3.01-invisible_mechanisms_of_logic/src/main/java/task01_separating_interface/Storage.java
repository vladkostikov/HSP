package task01_separating_interface;

public interface Storage {
    void save(String data);
    String retrieve(int id);
}
