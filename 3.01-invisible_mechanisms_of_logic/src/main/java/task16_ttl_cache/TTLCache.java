package task16_ttl_cache;

import java.util.HashMap;
import java.util.Map;

public class TTLCache {
    private Map<String, Object> cache = new HashMap<>();
    private Map<String, Long> expiry = new HashMap<>();
    private long ttlMillis;

    public TTLCache(long ttlMillis) { this.ttlMillis = ttlMillis; }

    public void put(String key, Object value) {
        cache.put(key, value);
        expiry.put(key, System.currentTimeMillis() + ttlMillis);
    }

    public Object get(String key) {
        if (!cache.containsKey(key)) return null;
        if (System.currentTimeMillis() > expiry.get(key)) {
            cache.remove(key);
            expiry.remove(key);
            return null;
        }
        return cache.get(key);
    }
}

class Main {
    public static void main(String[] args) throws InterruptedException {
        TTLCache cache = new TTLCache(500);

        cache.put("user_1", "John");
        cache.put("user_2", "Doe");

        System.out.println("user_1: " + cache.get("user_1")); // John
        System.out.println("user_2: " + cache.get("user_2")); // Doe

        Thread.sleep(1000);

        System.out.println("user_1 after expiry: " + cache.get("user_1")); // null
        System.out.println("user_2 after expiry: " + cache.get("user_2")); // null
    }
}
