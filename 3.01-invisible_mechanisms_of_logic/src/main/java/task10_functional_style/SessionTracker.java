package task10_functional_style;

import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * Task: rewrite SessionTracker in functional style.
 */
public class SessionTracker {
    private final Map<String, Date> activeSessions = new HashMap<>();

    public void registerActivity(String userId) {
        activeSessions.put(userId, new Date());
        System.out.println("User activity registered: " + userId);
    }

    public void removeInactiveSessions(long timeoutMillis) {
        Date now = new Date();
        Iterator<Map.Entry<String, Date>> iterator = activeSessions.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, Date> entry = iterator.next();
            if (now.getTime() - entry.getValue().getTime() > timeoutMillis) {
                System.out.println("Removing inactive session: " + entry.getKey());
                iterator.remove();
            }
        }
    }

    public boolean isActive(String userId) {
        return activeSessions.containsKey(userId);
    }

    public int activeCount() {
        return activeSessions.size();
    }

    public void printActiveSessions() {
        System.out.println("Active sessions:");
        for (Map.Entry<String, Date> entry : activeSessions.entrySet()) {
            System.out.println(entry.getKey() + " - last active at " + entry.getValue());
        }
    }

    public static void main(String[] args) throws InterruptedException {
        SessionTracker tracker = new SessionTracker();

        tracker.registerActivity("user1");
        Thread.sleep(500);
        tracker.registerActivity("user2");
        Thread.sleep(600);
        tracker.registerActivity("user3");

        tracker.printActiveSessions();

        tracker.removeInactiveSessions(1000);

        tracker.printActiveSessions();

        System.out.println("Is user1 active? " + tracker.isActive("user1"));
        System.out.println("Is user2 active? " + tracker.isActive("user2"));
        System.out.println("Is user3 active? " + tracker.isActive("user3"));

        System.out.println("Total active sessions: " + tracker.activeCount());
    }
}
