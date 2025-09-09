import java.sql.*;

public interface Storage {
    void save(String data);
    String retrieve(int id);
}

public class DatabaseStorage implements Storage {
    private final Connection connection;

    public DatabaseStorage(Connection connection) {
        this.connection = connection;
    }

    @Override
    public void save(String data) {
        String sql = "INSERT INTO storage_data (data) VALUES (?)";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, data);
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("Error saving data: " + e.getMessage(), e);
        }
    }

    @Override
    public String retrieve(int id) {
        String sql = "SELECT data FROM storage_data WHERE id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return rs.getString("data");
            }
            return null;
        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving data: " + e.getMessage(), e);
        }
    }
}
