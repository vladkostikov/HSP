package task10_functional_style;

import java.time.LocalDateTime;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * Task: rewrite SessionTracker in functional style.
 * Changes: made the class immutable, methods return new objects instead of mutating state, removed all side effects.
 */
public final class SessionTracker {
    private final Map<String, LocalDateTime> activeSessions;

    public SessionTracker() {
        this.activeSessions = Collections.emptyMap();
    }

    private SessionTracker(Map<String, LocalDateTime> sessions) {
        this.activeSessions = Map.copyOf(sessions);
    }

    public SessionTracker registerActivity(String userId) {
        if (userId == null || userId.isBlank()) {
            throw new IllegalArgumentException("User ID cannot be null or empty");
        }

        Map<String, LocalDateTime> newSessions = new HashMap<>(activeSessions);
        newSessions.put(userId, LocalDateTime.now());
        return new SessionTracker(newSessions);
    }

    public SessionTracker removeInactiveSessions(long timeoutMillis) {
        if (timeoutMillis < 0) {
            throw new IllegalArgumentException("Timeout must be non-negative");
        }

        LocalDateTime now = LocalDateTime.now();
        Map<String, LocalDateTime> newSessions = new HashMap<>();

        for (Map.Entry<String, LocalDateTime> entry : activeSessions.entrySet()) {
            long diffMillis = java.time.Duration.between(entry.getValue(), now).toMillis();
            if (diffMillis <= timeoutMillis) {
                newSessions.put(entry.getKey(), entry.getValue());
            }
        }

        return new SessionTracker(newSessions);
    }

    public boolean isActive(String userId) {
        return activeSessions.containsKey(userId);
    }

    public int activeCount() {
        return activeSessions.size();
    }

    public Map<String, LocalDateTime> getActiveSessions() {
        return activeSessions;
    }

    public static void main(String[] args) throws InterruptedException {
        SessionTracker tracker = new SessionTracker();

        tracker = tracker.registerActivity("user1");
        Thread.sleep(500);
        tracker = tracker.registerActivity("user2");
        Thread.sleep(600);
        tracker = tracker.registerActivity("user3");

        System.out.println("All sessions: " + tracker.getActiveSessions());

        tracker = tracker.removeInactiveSessions(1000);
        System.out.println("After cleanup: " + tracker.getActiveSessions());

        System.out.println("Is user1 active? " + tracker.isActive("user1"));
        System.out.println("Is user2 active? " + tracker.isActive("user2"));
        System.out.println("Is user3 active? " + tracker.isActive("user3"));

        System.out.println("Total active sessions: " + tracker.activeCount());
    }
}
