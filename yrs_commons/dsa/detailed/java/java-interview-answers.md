# Java and Spring Boot Interview Questions and Answers

## Core Java Concepts

### 1. OOPs Concepts and Usage

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects that contain data and code. The main principles of OOP are:

1. **Encapsulation**: Bundling data and methods that operate on the data within a single unit (class) and restricting direct access to some of the object's components.
   
   *Example*: Creating private class variables with public getter/setter methods.
   ```java
   public class Employee {
       private String name;
       
       public String getName() { return name; }
       public void setName(String name) { this.name = name; }
   }
   ```

2. **Inheritance**: Mechanism where a new class inherits properties and behaviors from an existing class.

   *Example*: Creating specialized classes from a base class.
   ```java
   public class Person { /* code */ }
   public class Employee extends Person { /* code */ }
   ```

3. **Polymorphism**: Ability of different objects to respond to the same method call in different ways.

   *Example*: Method overriding and overloading.
   ```java
   public class Animal {
       public void makeSound() { System.out.println("Some sound"); }
   }
   
   public class Dog extends Animal {
       @Override
       public void makeSound() { System.out.println("Bark"); }
   }
   ```

4. **Abstraction**: Hiding complex implementation details and showing only necessary features.

   *Example*: Using abstract classes or interfaces.
   ```java
   public interface PaymentProcessor {
       void processPayment(double amount);
   }
   
   public class CreditCardProcessor implements PaymentProcessor {
       @Override
       public void processPayment(double amount) { /* implementation */ }
   }
   ```

### 2. String vs StringBuffer vs StringBuilder

**String:**
- Immutable (once created, cannot be modified)
- Thread-safe
- Each operation creates a new String object

**StringBuffer:**
- Mutable (can be modified)
- Thread-safe (synchronized methods)
- Good for multithreaded environments

**StringBuilder:**
- Mutable (can be modified)
- Not thread-safe
- Faster than StringBuffer (no synchronization overhead)
- Introduced in Java 5

**When to use:**
- Use **String** when the text won't change
- Use **StringBuffer** when the text will change and thread safety is required
- Use **StringBuilder** when the text will change and thread safety is not required (most common in single-threaded contexts)

### 3. Fail-Fast vs Fail-Safe Iterators

**Fail-Fast Iterators:**
- Throw `ConcurrentModificationException` if the collection is modified while iterating
- Work directly on the collection
- Examples: Iterator from ArrayList, HashMap, Vector

```java
ArrayList<String> list = new ArrayList<>();
// ... add elements
Iterator<String> iterator = list.iterator();
while(iterator.hasNext()) {
    String item = iterator.next();
    list.remove(0); // This will throw ConcurrentModificationException
}
```

**Fail-Safe Iterators:**
- Don't throw exceptions if collection is modified during iteration
- Work on a copy of the collection
- May not reflect the latest state of the collection
- Examples: Iterator from ConcurrentHashMap, CopyOnWriteArrayList

```java
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
// ... add elements
Iterator<String> iterator = list.iterator();
while(iterator.hasNext()) {
    String item = iterator.next();
    list.remove(0); // This is safe, iterator works on a copy
}
```

### 5. Binary Tree Implementation in Java

```java
class Node {
    int data;
    Node left, right;
    
    public Node(int item) {
        data = item;
        left = right = null;
    }
}

class BinaryTree {
    Node root;
    
    // Constructor
    BinaryTree() {
        root = null;
    }
    
    // Insert a node
    void insert(int key) {
        root = insertRec(root, key);
    }
    
    Node insertRec(Node root, int key) {
        // If the tree is empty, return a new node
        if (root == null) {
            root = new Node(key);
            return root;
        }
        
        // Otherwise, recur down the tree
        if (key < root.data)
            root.left = insertRec(root.left, key);
        else if (key > root.data)
            root.right = insertRec(root.right, key);
            
        // Return the unchanged node pointer
        return root;
    }
    
    // Inorder traversal
    void inorder() {
        inorderRec(root);
    }
    
    void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }
}
```

### 6. Breaking Out of a Running Loop in Java

There are several ways to exit a running loop:

1. **Using `break` statement**:
   ```java
   for (int i = 0; i < 10; i++) {
       if (i == 5) {
           break; // Exit the loop when i equals 5
       }
       System.out.println(i);
   }
   ```

2. **Using `return` statement** (exits the method):
   ```java
   public void loopMethod() {
       for (int i = 0; i < 10; i++) {
           if (i == 5) {
               return; // Exit the method when i equals 5
           }
           System.out.println(i);
       }
   }
   ```

3. **Using boolean flag**:
   ```java
   boolean shouldContinue = true;
   for (int i = 0; i < 10 && shouldContinue; i++) {
       if (i == 5) {
           shouldContinue = false; // Exit the loop when i equals 5
       }
       System.out.println(i);
   }
   ```

4. **Using labeled breaks** (for nested loops):
   ```java
   outerLoop: for (int i = 0; i < 5; i++) {
       for (int j = 0; j < 5; j++) {
           if (i == 2 && j == 2) {
               break outerLoop; // Exit both loops
           }
           System.out.println(i + " " + j);
       }
   }
   ```

### 7. Access Modifiers in Java

Java has four access modifiers:

1. **private**: Accessible only within the declared class
2. **default** (no modifier): Accessible within the same package
3. **protected**: Accessible within the same package and subclasses
4. **public**: Accessible from anywhere

Example:
```java
public class AccessModifiers {
    private int privateVar;           // accessible only in this class
    int defaultVar;                   // accessible in same package
    protected int protectedVar;       // accessible in same package and subclasses
    public int publicVar;             // accessible from anywhere
    
    private void privateMethod() { }  // accessible only in this class
    void defaultMethod() { }          // accessible in same package
    protected void protectedMethod() { } // accessible in same package and subclasses
    public void publicMethod() { }    // accessible from anywhere
}
```

### 8. New Features in Java 8

Key features introduced in Java 8:

1. **Lambda Expressions**: Enable functional programming
   ```java
   List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
   numbers.forEach(n -> System.out.println(n));
   ```

2. **Method References**: Shorthand for lambda expressions
   ```java
   numbers.forEach(System.out::println);
   ```

3. **Functional Interfaces**: Interfaces with a single abstract method
   ```java
   @FunctionalInterface
   interface Converter<F, T> {
       T convert(F from);
   }
   ```

4. **Stream API**: Process collections of objects in a functional way
   ```java
   List<String> filtered = names.stream()
       .filter(name -> name.startsWith("A"))
       .collect(Collectors.toList());
   ```

5. **Optional Class**: Container object to represent null with absent values
   ```java
   Optional<String> optional = Optional.of("value");
   optional.isPresent();           // true
   optional.get();                 // "value"
   optional.orElse("default");     // "value"
   ```

6. **Default and Static Methods in Interfaces**
   ```java
   interface Vehicle {
       default void print() {
           System.out.println("I am a vehicle!");
       }
       
       static void blowHorn() {
           System.out.println("Blowing horn!");
       }
   }
   ```

7. **New Date and Time API**
   ```java
   LocalDate date = LocalDate.now();
   LocalTime time = LocalTime.now();
   LocalDateTime dateTime = LocalDateTime.now();
   ```

8. **Nashorn JavaScript Engine**
9. **Base64 Encoding/Decoding**
10. **Parallel Array Sorting**

### 9. Difference Between JVM, JRE, and JDK

**JVM (Java Virtual Machine)**:
- Abstract machine that enables computer to run Java programs
- Provides runtime environment for Java bytecode execution
- Platform-dependent (different for different OS)
- Responsible for memory management and garbage collection

**JRE (Java Runtime Environment)**:
- Implementation of JVM
- Provides libraries and classes needed to run Java programs
- Contains JVM + libraries + other components
- End-users only need JRE to run Java applications

**JDK (Java Development Kit)**:
- Software development environment for building Java applications
- Contains JRE + development tools (compiler, debugger, etc.)
- Includes tools like javac (compiler), java (launcher), javadoc, etc.
- Needed by developers to create Java applications

Relationship: JDK > JRE > JVM (JDK contains JRE, which contains JVM)

### 10. Shallow vs Deep Comparison in Strings

**Shallow Comparison (==)**:
- Compares object references (memory addresses)
- Returns true if both references point to the same object

**Deep Comparison (equals())**:
- Compares actual content of the objects
- Returns true if the content is the same, regardless of memory address

Example:
```java
String s1 = "Hello";
String s2 = "Hello";
String s3 = new String("Hello");

// Shallow comparison
System.out.println(s1 == s2);      // true (same string pool reference)
System.out.println(s1 == s3);      // false (different objects)

// Deep comparison
System.out.println(s1.equals(s2)); // true (same content)
System.out.println(s1.equals(s3)); // true (same content)
```

### 11. Why Char Arrays Are Preferred Over Strings for Passwords

Char arrays are preferred over Strings for storing passwords for security reasons:

1. **Immutability**: Strings are immutable in Java, meaning they can't be modified after creation. Once a password is stored in a String, it remains in memory until garbage collection, which might not happen immediately.

2. **Explicit clearing**: Char arrays can be explicitly cleared (overwritten) after use:
   ```java
   char[] password = new char[] {'p','a','s','s'};
   // Use the password
   // ...
   // Explicitly clear the password when done
   Arrays.fill(password, '0');
   ```

3. **String Pool**: Strings might be interned and remain in the String pool for the duration of the application, increasing the risk of exposure.

4. **Memory Dump**: If a memory dump occurs, passwords stored in Strings might be visible in plain text for longer periods.

### 12. Lambda Expressions and Their Uses

Lambda expressions provide a clear and concise way to implement functional interfaces (interfaces with a single abstract method). They enable functional programming in Java.

**Syntax**: `(parameters) -> expression` or `(parameters) -> { statements; }`

**Uses**:

1. **Iteration**:
   ```java
   List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
   names.forEach(name -> System.out.println(name));
   ```

2. **Filtering**:
   ```java
   List<String> filtered = names.stream()
       .filter(name -> name.startsWith("A"))
       .collect(Collectors.toList());
   ```

3. **Mapping/Transforming**:
   ```java
   List<Integer> lengths = names.stream()
       .map(name -> name.length())
       .collect(Collectors.toList());
   ```

4. **Sorting**:
   ```java
   names.sort((a, b) -> a.compareTo(b));
   ```

5. **Event Handling**:
   ```java
   button.addActionListener(e -> System.out.println("Button clicked"));
   ```

6. **Runnable Implementation**:
   ```java
   new Thread(() -> {
       System.out.println("Thread running");
   }).start();
   ```

### 13. Iterating and Removing Elements from ArrayList

Direct removal during iteration using a standard for loop or forEach will throw a `ConcurrentModificationException`. Safe ways to handle this:

1. **Using Iterator's remove method**:
   ```java
   List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
   Iterator<String> iterator = list.iterator();
   while (iterator.hasNext()) {
       String item = iterator.next();
       if ("B".equals(item)) {
           iterator.remove(); // Safe way to remove
       }
   }
   ```

2. **Using removeIf() (Java 8+)**:
   ```java
   List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
   list.removeIf(item -> "B".equals(item));
   ```

3. **Using CopyOnWriteArrayList**:
   ```java
   List<String> list = new CopyOnWriteArrayList<>(Arrays.asList("A", "B", "C", "D"));
   for (String item : list) {
       if ("B".equals(item)) {
           list.remove(item); // Safe with CopyOnWriteArrayList
       }
   }
   ```

4. **Removing after iteration** (collect items to remove first):
   ```java
   List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
   List<String> toRemove = new ArrayList<>();
   
   for (String item : list) {
       if ("B".equals(item)) {
           toRemove.add(item);
       }
   }
   
   list.removeAll(toRemove);
   ```

### 14. How HashMap Stores and Retrieves Data

**Storage Mechanism**:

1. **Hashing**: HashMap uses an array of buckets (aka nodes) to store entries
2. **Key's hashCode()**: When adding a key-value pair, the key's hashCode() is used to determine the bucket location
3. **Bucket**: Each bucket can contain multiple entries (in case of hash collisions)
4. **LinkedList/Tree**: In a bucket, entries are stored in a linked list (or a tree in Java 8+ if the bucket size exceeds a threshold)

**Retrieval Process**:

1. Calculate the hashCode of the key
2. Find the corresponding bucket
3. Search through the linked list/tree in that bucket using equals() to find the exact match
4. Return the associated value

**Example**:
```java
HashMap<String, Integer> map = new HashMap<>();
map.put("One", 1);

// Internally:
// 1. hashCode of "One" is calculated
// 2. Index in the bucket array is determined
// 3. Entry is stored in that bucket

// Retrieval
int value = map.get("One");

// Internally:
// 1. hashCode of "One" is calculated
// 2. Index in the bucket array is found
// 3. LinkedList/Tree is traversed to find the exact match
// 4. Value 1 is returned
```

**Key Properties**:
- Time complexity: O(1) for best case, O(n) worst case (if all keys hash to the same bucket)
- Not thread-safe (use ConcurrentHashMap for thread safety)
- Allows null keys and values
- No guaranteed order (use LinkedHashMap for insertion order)

### 15. Thread Pool in Java and Its Uses

A thread pool is a collection of pre-initialized, reusable worker threads that are available to perform tasks.

**Implementation in Java**:
```java
// Fixed thread pool with 5 threads
ExecutorService executor = Executors.newFixedThreadPool(5);

// Submit tasks
for (int i = 0; i < 10; i++) {
    final int taskId = i;
    executor.submit(() -> {
        System.out.println("Task " + taskId + " executed by " + 
                           Thread.currentThread().getName());
    });
}

// Shutdown the executor
executor.shutdown();
```

**Types of Thread Pools in Java**:
1. **Fixed Thread Pool**: Fixed number of threads
   ```java
   ExecutorService executor = Executors.newFixedThreadPool(5);
   ```

2. **Cached Thread Pool**: Expands/contracts based on demand
   ```java
   ExecutorService executor = Executors.newCachedThreadPool();
   ```

3. **Scheduled Thread Pool**: For delayed or periodic execution
   ```java
   ScheduledExecutorService executor = Executors.newScheduledThreadPool(5);
   ```

4. **Single Thread Executor**: Uses a single worker thread
   ```java
   ExecutorService executor = Executors.newSingleThreadExecutor();
   ```

**Benefits**:
- Reduces overhead of thread creation/destruction
- Enables task queuing and thread management
- Improves application responsiveness
- Controls the maximum number of concurrent threads
- Reuses threads for multiple tasks

**Uses**:
- Web servers handling multiple requests
- Background task processing
- Parallel data processing
- Asynchronous task execution
- Managing resource utilization

### 17. LRU Cache Implementation in Java

LRU (Least Recently Used) Cache removes the least recently accessed items when the cache reaches its capacity.

```java
public class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    
    public LRUCache(int capacity) {
        // true for access-order, false for insertion-order
        super(capacity + 1, 1.0f, true);
        this.capacity = capacity;
    }
    
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        // Remove the oldest entry when size exceeds capacity
        return size() > capacity;
    }
    
    public static void main(String[] args) {
        LRUCache<Integer, String> cache = new LRUCache<>(3);
        
        cache.put(1, "One");
        cache.put(2, "Two");
        cache.put(3, "Three");
        
        System.out.println(cache); // {1=One, 2=Two, 3=Three}
        
        // Access key 1, making it the most recently used
        cache.get(1);
        
        // Adding a new entry will remove the least recently used (key 2)
        cache.put(4, "Four");
        
        System.out.println(cache); // {1=One, 3=Three, 4=Four}
    }
}
```

Alternative implementation using HashMap and DoublyLinkedList:

```java
class LRUCache {
    class Node {
        int key;
        int value;
        Node prev;
        Node next;
    }
    
    private void addNode(Node node) {
        // Always add node right after head
        node.prev = head;
        node.next = head.next;
        
        head.next.prev = node;
        head.next = node;
    }
    
    private void removeNode(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        
        prev.next = next;
        next.prev = prev;
    }
    
    private void moveToHead(Node node) {
        removeNode(node);
        addNode(node);
    }
    
    private Node popTail() {
        Node res = tail.prev;
        removeNode(res);
        return res;
    }
    
    private Map<Integer, Node> cache = new HashMap<>();
    private int size;
    private int capacity;
    private Node head, tail;
    
    public LRUCache(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        
        head = new Node();
        tail = new Node();
        
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) return -1;
        
        // Move to head (recently used)
        moveToHead(node);
        
        return node.value;
    }
    
    public void put(int key, int value) {
        Node node = cache.get(key);
        
        if (node == null) {
            Node newNode = new Node();
            newNode.key = key;
            newNode.value = value;
            
            cache.put(key, newNode);
            addNode(newNode);
            
            ++size;
            
            if (size > capacity) {
                // Remove the least recently used item
                Node tail = popTail();
                cache.remove(tail.key);
                --size;
            }
        } else {
            // Update the value
            node.value = value;
            moveToHead(node);
        }
    }
}
```

### 18. Single-Threaded Application in Java

A single-threaded application executes operations sequentially in a single thread of control.

```java
public class SingleThreadedApp {
    public static void main(String[] args) {
        System.out.println("Starting single-threaded application");
        
        // All code runs in the main thread
        for (int i = 1; i <= 5; i++) {
            System.out.println("Processing task " + i);
            // Simulate work
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        
        System.out.println("All tasks completed");
    }
}
```

For more control using ExecutorService:

```java
public class SingleThreadedExecutor {
    public static void main(String[] args) {
        System.out.println("Starting single-threaded executor");
        
        // Create a single-threaded executor
        ExecutorService executor = Executors.newSingleThreadExecutor();
        
        // Submit multiple tasks that will be executed sequentially
        for (int i = 1; i <= 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                System.out.println("Processing task " + taskId);
                // Simulate work
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                return "Task " + taskId + " result";
            });
        }
        
        // Shutdown the executor
        executor.shutdown();
        try {
            // Wait for all tasks to complete
            if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
        }
        
        System.out.println("All tasks completed");
    }
}
```

### 19. Autoboxing in Java

Autoboxing is the automatic conversion between primitive types and their corresponding wrapper classes:
- int ↔ Integer
- boolean ↔ Boolean
- char ↔ Character
- etc.

**Examples**:

Autoboxing (primitive to wrapper):
```java
Integer number = 42; // Autoboxing: int to Integer
```

Unboxing (wrapper to primitive):
```java
int primitiveNum = number; // Unboxing: Integer to int
```

In collections:
```java
ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(1); // Autoboxing: int to Integer
int firstNum = numbers.get(0); // Unboxing: Integer to int
```

In expressions:
```java
Integer a = 10;
Integer b = 20;
Integer sum = a + b; // Unboxing, addition, then autoboxing
```

**Performance Considerations**:
- Autoboxing/unboxing has some performance overhead
- Can lead to unexpected behavior if not properly understood
- Can cause NullPointerException if unboxing a null wrapper

### 20. Custom Connection Pool in Java

A connection pool manages database connections for reuse, improving performance by avoiding connection creation overhead.

```java
public class ConnectionPool {
    private static final int MAX_POOL_SIZE = 10;
    private static final int MAX_TIMEOUT = 5000; // ms
    
    private final LinkedList<Connection> availableConnections = new LinkedList<>();
    private final LinkedList<Connection> usedConnections = new LinkedList<>();
    
    private final String url;
    private final String user;
    private final String password;
    
    public ConnectionPool(String url, String user, String password) throws SQLException {
        this.url = url;
        this.user = user;
        this.password = password;
        
        // Initialize the pool with connections
        for (int i = 0; i < MAX_POOL_SIZE; i++) {
            availableConnections.add(createConnection());
        }
    }
    
    private Connection createConnection() throws SQLException {
        return DriverManager.getConnection(url, user, password);
    }
    
    public synchronized Connection getConnection() throws SQLException {
        if (availableConnections.isEmpty()) {
            if (usedConnections.size() < MAX_POOL_SIZE) {
                availableConnections.add(createConnection());
            } else {
                // No connections available, and at max pool size
                // Wait for a connection to be released or timeout
                try {
                    this.wait(MAX_TIMEOUT);
                    if (availableConnections.isEmpty()) {
                        throw new SQLException("Connection timeout");
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    throw new SQLException("Interrupted while waiting for connection");
                }
            }
        }
        
        Connection connection = availableConnections.removeFirst();
        usedConnections.add(connection);
        return connection;
    }
    
    public synchronized void releaseConnection(Connection connection) {
        usedConnections.remove(connection);
        availableConnections.add(connection);
        // Notify waiting threads that a connection is available
        this.notify();
    }
    
    public synchronized void closeAllConnections() throws SQLException {
        for (Connection connection : availableConnections) {
            connection.close();
        }
        availableConnections.clear();
        
        for (Connection connection : usedConnections) {
            connection.close();
        }
        usedConnections.clear();
    }
    
    public int getAvailableConnectionsCount() {
        return availableConnections.size();
    }
    
    public int getUsedConnectionsCount() {
        return usedConnections.size();
    }
}
```

Usage example:
```java
ConnectionPool pool = new ConnectionPool("jdbc:mysql://localhost:3306/mydb", "user", "password");

try {
    Connection connection = pool.getConnection();
    // Use the connection
    Statement stmt = connection.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT * FROM users");
    // Process results
    
    // Release the connection back to the pool
    pool.releaseConnection(connection);
} catch (SQLException e) {
    e.printStackTrace();
}

// When application is shutting down
pool.closeAllConnections();
```

### 22. Design Patterns Implementation

**Singleton Pattern**:
```java
public class Singleton {
    // Private static instance
    private static volatile Singleton instance;
    
    // Private constructor
    private Singleton() {}
    
    // Public method to get instance
    public static Singleton getInstance() {
        // Double-checked locking
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
    
    // Methods
    public void doSomething() {
        System.out.println("Singleton is doing something");
    }
}
```

**Factory Pattern**:
```java
// Product interface
interface Product {
    void operation();
}

// Concrete products
class ConcreteProductA implements Product {
    @Override
    public void operation() {
        System.out.println("ConcreteProductA operation");
    }
}

class ConcreteProductB implements Product {
    @Override
    public void operation() {
        System.out.println("ConcreteProductB operation");
    }
}

// Factory
class ProductFactory {
    public static Product createProduct(String type) {
        if ("A".equals(type)) {
            return new ConcreteProductA();
        } else if ("B".equals(type)) {
            return new ConcreteProductB();
        }
        throw new IllegalArgumentException("Unknown product type: " + type);
    }
}

// Usage
public class FactoryDemo {
    public static void main(String[] args) {
        Product productA = ProductFactory.createProduct("A");
        productA.operation();
        
        Product productB = ProductFactory.createProduct("B");
        productB.operation();
    }
}
```

**Observer Pattern**:
```java
import java.util.ArrayList;
import java.util.List;

// Observer interface
interface Observer {
    void update(String message);
}

// Concrete observer
class ConcreteObserver implements Observer {
    private String name;
    
    public ConcreteObserver(String name) {
        this.name = name;
    }
    
    @Override
    public void update(String message) {
        System.out.println(name + " received: " + message);
    }
}

// Subject
class Subject {
    private List<Observer> observers = new ArrayList<>();
    
    public void attach(Observer observer) {
        observers.add(observer);
    }
    
    public void detach(Observer observer) {
        observers.remove(observer);
    }
    
    public void notifyObservers(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }
}

// Usage
public class ObserverDemo {
    public static void main(String[] args) {
        Subject subject = new Subject();
        
        Observer observer1 = new ConcreteObserver("Observer 1");
        Observer observer2 = new ConcreteObserver("Observer 2");
        
        subject.attach(observer1);
        subject.attach(observer2);
        
        subject.notifyObservers("Hello Observers!");
        
        subject.detach(observer1);
        
        subject.notifyObservers("Observer 1 has left");
    }
}
```

### 23. JavaFX

JavaFX is a software platform for creating desktop applications and rich internet applications (RIAs) that can run on multiple devices. It's the successor to Swing for building GUI applications in Java.

**Key Components**:
- **Stage**: The top-level container (window)
- **Scene**: The container for all content
- **Nodes**: UI elements like buttons, text fields, etc.
- **Layout Panes**: Containers that arrange nodes (VBox, HBox, BorderPane, etc.)
- **FXML**: XML markup for defining UI
- **CSS**: Styling for JavaFX applications

**Simple Example**:
```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class JavaFXExample extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        // Create a label
        Label label = new Label("Hello, JavaFX!");
        
        // Create a button
        Button button = new Button("Click Me");
        button.setOnAction(e -> label.setText("Button clicked!"));
        
        // Create a layout container
        VBox root = new VBox(10); // 10px spacing
        root.getChildren().addAll(label, button);
        
        // Create a scene
        Scene scene = new Scene(root, 300, 200);
        
        // Setup the stage
        primaryStage.setTitle("JavaFX Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

**Features**:
- Modern UI components
- Hardware-accelerated graphics
- CSS styling
- FXML for UI definition
- Animation framework
- 3D graphics support
- Media playback
- WebView component

### 24. Remove Duplicates in an Array

**For primitive arrays**:
```java
public static int[] removeDuplicates(int[] array) {
    if (array == null || array.length == 0) {
        return array;
    }
    
    // Use Set to automatically handle duplicates
    Set<Integer> set = new LinkedHashSet<>();
    for (int item : array) {
        set.add(item);
    }
    
    // Convert back to array
    int[] result = new int[set.size()];
    int i = 0;
    for (Integer item : set) {
        result[i++] = item;
    }
    
    return result;
}
```

**For object arrays**:
```java
public static <T> T[] removeDuplicates(T[] array) {
    if (array == null || array.length == 0) {
        return array;
    }
    
    // Use LinkedHashSet to maintain order
    Set<T> set = new LinkedHashSet<>(Arrays.asList(array));
    
    // Create a new array of the same type
    @SuppressWarnings("unchecked")
    T[] result = (T[]) Array.newInstance(array.getClass().getComponentType(), set.size());
    
    return set.toArray(result);
}
```

**Using Java 8+ Stream API**:
```java
public static int[] removeDuplicates(int[] array) {
    return Arrays.stream(array)
                 .distinct()
                 .toArray();
}

public static <T> T[] removeDuplicates(T[] array) {
    @SuppressWarnings("unchecked")
    T[] result = (T[]) Arrays.stream(array)
                             .distinct()
                             .toArray(size -> (T[]) Array.newInstance(array.getClass().getComponentType(), size));
    return result;
}
```

### 25. Compare Top Two Records Using SQL

```sql
-- Using LIMIT and ORDER BY
SELECT * 
FROM your_table 
ORDER BY column_name DESC 
LIMIT 2;

-- Using window function (for complex comparisons)
SELECT * FROM (
    SELECT *, 
           DENSE_RANK() OVER (ORDER BY column_name DESC) as rnk 
    FROM your_table
) ranked 
WHERE rnk <= 2;

-- For comparing values between top two records
WITH TopTwo AS (
    SELECT *, 
           ROW_NUMBER() OVER (ORDER BY column_name DESC) as rn 
    FROM your_table 
    LIMIT 2
)
SELECT 
    a.column_name as top_value,
    b.column_name as second_value,
    a.column_name - b.column_name as difference
FROM 
    TopTwo a, TopTwo b
WHERE 
    a.rn = 1 AND b.rn = 2;
```

### 26. Call a Stored Procedure from Java

```java
import java.sql.*;

public class StoredProcedureExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydb";
        String username = "username";
        String password = "password";
        
        try (Connection conn = DriverManager.getConnection(url, username, password)) {
            // For a procedure with IN parameters
            callProcedureWithInParams(conn);
            
            // For a procedure with OUT parameters
            callProcedureWithOutParams(conn);
            
            // For a procedure with INOUT parameters
            callProcedureWithInOutParams(conn);
            
            // For a procedure that returns a result set
            callProcedureWithResultSet(conn);
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    // Example with IN parameters
    private static void callProcedureWithInParams(Connection conn) throws SQLException {
        String sql = "{CALL add_employee(?, ?, ?)}";
        
        try (CallableStatement stmt = conn.prepareCall(sql)) {
            stmt.setString(1, "John Doe");
            stmt.setString(2, "IT");
            stmt.setDouble(3, 50000.0);
            
            stmt.execute();
            System.out.println("Employee added successfully");
        }
    }
    
    // Example with OUT parameters
    private static void callProcedureWithOutParams(Connection conn) throws SQLException {
        String sql = "{CALL get_employee_count(?)}";
        
        try (CallableStatement stmt = conn.prepareCall(sql)) {
            // Register the OUT parameter
            stmt.registerOutParameter(1, Types.INTEGER);
            
            stmt.execute();
            
            // Get the OUT parameter value
            int count = stmt.getInt(1);
            System.out.println("Employee count: " + count);
        }
    }
    
    // Example with INOUT parameters
    private static void callProcedureWithInOutParams(Connection conn) throws SQLException {
        String sql = "{CALL update_salary(?, ?)}";
        
        try (CallableStatement stmt = conn.prepareCall(sql)) {
            // Set IN parameter
            stmt.setInt(1, 101); // Employee ID
            
            // Register the INOUT parameter
            stmt.registerOutParameter(2, Types.DOUBLE);
            stmt.setDouble(2, 55000.0); // New salary
            
            stmt.execute();
            
            // Get the INOUT parameter value after execution
            double updatedSalary = stmt.getDouble(2);
            System.out.println("Updated salary: " + updatedSalary);
        }
    }
    
    // Example with Result Set
    private static void callProcedureWithResultSet(Connection conn) throws SQLException {
        String sql = "{CALL get_employees_by_dept(?)}";
        
        try (CallableStatement stmt = conn.prepareCall(sql)) {
            stmt.setString(1, "IT");
            
            // Execute and process result set
            boolean hasResults = stmt.execute();
            
            if (hasResults) {
                try (ResultSet rs = stmt.getResultSet()) {
                    while (rs.next()) {
                        int id = rs.getInt("id");
                        String name = rs.getString("name");
                        double salary = rs.getDouble("salary");
                        
                        System.out.println(id + ", " + name + ", " + salary);
                    }
                }
            }
        }
    }
}
```

### 27. SQL Query for Pagination by Oldest Records

```sql
-- Using LIMIT and OFFSET
SELECT * 
FROM your_table 
ORDER BY created_date ASC 
LIMIT page_size OFFSET (page_number - 1) * page_size;

-- Example with specific values
SELECT * 
FROM your_table 
ORDER BY created_date ASC 
LIMIT 10 OFFSET 20; -- For page 3 with page size 10
```

In Java, you can implement pagination as follows:

```java
public List<User> getUsersByPage(int pageNumber, int pageSize) {
    List<User> users = new ArrayList<>();
    
    String sql = "SELECT * FROM users ORDER BY created_date ASC LIMIT ? OFFSET ?";
    
    try (Connection conn = getConnection();
         PreparedStatement stmt = conn.prepareStatement(sql)) {
        
        stmt.setInt(1, pageSize);
        stmt.setInt(2, (pageNumber - 1) * pageSize);
        
        try (ResultSet rs = stmt.executeQuery()) {
            while (rs.next()) {
                User user = new User();
                user.setId(rs.getLong("id"));
                user.setName(rs.getString("name"));
                // Set other fields
                
                users.add(user);
            }
        }
    } catch (SQLException e) {
        e.printStackTrace();
    }
    
    return users;
}
```

### 28. Database Indexes and Types

**What is a DB Index?**
A database index is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional storage space and slower write operations.

**Types of DB Indexes**:

1. **B-Tree Index** (Balanced Tree):
   - Most common type
   - Good for equality and range queries
   - Supports <, <=, =, >=, >, BETWEEN, and LIKE (with prefix only)
   - Default index in most databases

2. **Hash Index**:
   - Optimized for equality comparisons (=)
   - Very fast lookups
   - Cannot be used for range queries
   - Fixed size in memory

3. **Bitmap Index**:
   - Good for columns with low cardinality (few unique values)
   - Uses bit vectors for each possible value
   - Efficient for multiple conditions using AND/OR
   - Good for data warehousing

4. **Clustered Index**:
   - Determines the physical order of data in a table
   - Only one per table
   - In MySQL/InnoDB, typically the primary key
   - Faster access for range queries on the indexed column

5. **Non-Clustered Index**:
   - Doesn't affect physical ordering of data
   - Contains pointers to the actual data rows
   - Multiple can exist per table
   - Requires extra storage for pointers

6. **Composite Index**:
   - Uses multiple columns in a single index
   - Order of columns matters
   - Most effective when leading columns are used in queries

7. **Full-Text Index**:
   - Optimized for searching text content
   - Supports complex search operations
   - Ignores common words (stopwords)
   - Allows relevance ranking

8. **Spatial Index**:
   - Optimized for geometric data types
   - Used for GIS applications
   - Supports queries like "find all points within this polygon"

9. **Partial/Filtered Index**:
   - Only indexes a subset of rows based on a condition
   - Reduces index size
   - Improves performance for specific queries

10. **Function-Based/Expression Index**:
    - Built on the result of an expression or function
    - Speeds up queries that use that expression

### 29. Handling Out of Memory Exception

```java
public class OutOfMemoryHandler {
    public static void handleOOME() {
        // 1. Configure the JVM with appropriate heap settings
        // java -Xms512m -Xmx1024m -XX:+HeapDumpOnOutOfMemoryError YourApp
        
        // 2. Use try-catch to handle specific operations that might cause OOME
        try {
            // Operation that might cause OOME
            byte[] largeArray = new byte[1000 * 1024 * 1024]; // 1 GB
        } catch (OutOfMemoryError e) {
            System.err.println("Out of memory detected: " + e.getMessage());
            
            // 3. Free resources - e.g., clear caches or large collections
            clearCaches();
            
            // 4. Log the event
            logOOME(e);
            
            // 5. Take action based on severity
            if (isCritical()) {
                // Graceful shutdown if necessary
                initiateGracefulShutdown();
            } else {
                // Continue with reduced functionality
                switchToLowMemoryMode();
            }
        }
    }
    
    private static void clearCaches() {
        // Clear any application caches
        System.gc(); // Request garbage collection
    }
    
    private static void logOOME(Error e) {
        // Log the error to file/monitoring system
        e.printStackTrace();
    }
    
    private static boolean isCritical() {
        // Determine if this OOME is critical
        return true; // Example
    }
    
    private static void initiateGracefulShutdown() {
        // Notify services, save state, etc.
        System.exit(1);
    }
    
    private static void switchToLowMemoryMode() {
        // Adjust application behavior for low memory conditions
    }
    
    // Prevention strategies:
    // 1. Use memory-efficient data structures
    // 2. Implement resource pooling
    // 3. Use weak references for caches
    // 4. Stream large datasets instead of loading into memory
    // 5. Monitor memory usage
    public static void preventOOME() {
        // Example: Use a SoftReference for caching
        Map<String, SoftReference<byte[]>> cache = new HashMap<>();
        
        // Put item in cache
        cache.put("key", new SoftReference<>(new byte[1024]));
        
        // Get item from cache
        SoftReference<byte[]> ref = cache.get("key");
        if (ref != null) {
            byte[] data = ref.get();
            if (data != null) {
                // Use data
            } else {
                // Reference was cleared by GC - recreate data
            }
        }
    }
}
```

### 30. Traverse LinkedList Forward and Reverse

**Forward traversal**:
```java
public void traverseForward(LinkedList<Integer> list) {
    // Using Iterator
    Iterator<Integer> iterator = list.iterator();
    while (iterator.hasNext()) {
        Integer value = iterator.next();
        System.out.print(value + " ");
    }
    
    // OR using enhanced for loop
    for (Integer value : list) {
        System.out.print(value + " ");
    }
    
    // OR using ListIterator
    ListIterator<Integer> listIterator = list.listIterator();
    while (listIterator.hasNext()) {
        Integer value = listIterator.next();
        System.out.print(value + " ");
    }
}
```

**Backward traversal**:
```java
public void traverseBackward(LinkedList<Integer> list) {
    // Using descendingIterator (available in LinkedList)
    Iterator<Integer> descendingIterator = list.descendingIterator();
    while (descendingIterator.hasNext()) {
        Integer value = descendingIterator.next();
        System.out.print(value + " ");
    }
    
    // OR using ListIterator starting from the end
    ListIterator<Integer> listIterator = list.listIterator(list.size());
    while (listIterator.hasPrevious()) {
        Integer value = listIterator.previous();
        System.out.print(value + " ");
    }
}
```

**For custom LinkedList implementation**:
```java
class Node {
    int data;
    Node next;
    Node prev; // For doubly linked list
    
    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    private Node head;
    private Node tail;
    
    // Forward traversal
    public void traverseForward() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
    }
    
    // Backward traversal
    public void traverseBackward() {
        Node current = tail;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.prev;
        }
    }
}
```

### 31. Creating an Immutable Class

```java
// 1. Make the class final (cannot be extended)
public final class ImmutablePerson {
    // 2. Make all fields private and final
    private final String name;
    private final int age;
    private final List<String> hobbies; // Reference to mutable object
    
    // 3. Constructor for initialization
    public ImmutablePerson(String name, int age, List<String> hobbies) {
        this.name = name;
        this.age = age;
        
        // 4. Defensive copy for mutable objects
        this.hobbies = new ArrayList<>(hobbies);
    }
    
    // 5. Provide only getter methods (no setters)
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    // 6. Return defensive copies of mutable fields
    public List<String> getHobbies() {
        return new ArrayList<>(hobbies); // Defensive copy
    }
    
    // 7. Override methods that might affect immutability
    @Override
    public String toString() {
        return "Person [name=" + name + ", age=" + age + ", hobbies=" + hobbies + "]";
    }
}
```

Usage example:
```java
List<String> hobbiesList = new ArrayList<>();
hobbiesList.add("Reading");
hobbiesList.add("Swimming");

ImmutablePerson person = new ImmutablePerson("John", 30, hobbiesList);

// Original list modification doesn't affect the immutable object
hobbiesList.add("Running");
System.out.println(person.getHobbies()); // Still only [Reading, Swimming]

// Getting and modifying the list from the object doesn't affect the original
List<String> personHobbies = person.getHobbies();
personHobbies.add("Cycling");
System.out.println(person.getHobbies()); // Still only [Reading, Swimming]
```

### 32. Orchestrator in Microservices

An orchestrator in microservices architecture is responsible for coordinating and managing multiple services to execute a business process or workflow.

**Key Functions**:
- Service coordination
- Workflow management
- Service discovery
- Load balancing
- Failure handling
- State management
- Transaction management

**Common Orchestrators**:
1. **Kubernetes**:
   - Container orchestration
   - Service discovery
   - Load balancing
   - Self-healing capabilities
   - Horizontal scaling

2. **Spring Cloud Netflix (Zuul, Eureka, Ribbon)**:
   - API Gateway
   - Service discovery
   - Client-side load balancing

3. **Apache Camel**:
   - Enterprise Integration Patterns
   - Route definition
   - Protocol bridging

4. **Apache Airflow**:
   - Workflow orchestration
   - Task scheduling
   - Dependency management

5. **Conductor (Netflix)**:
   - Workflow orchestration
   - Task coordination
   - State management

**Example with Spring Cloud**:
```java
// Service Registry (Eureka)
@EnableEurekaServer
@SpringBootApplication
public class ServiceRegistryApplication {
    public static void main(String[] args) {
        SpringApplication.run(ServiceRegistryApplication.class, args);
    }
}

// API Gateway (Zuul)
@EnableZuulProxy
@EnableDiscoveryClient
@SpringBootApplication
public class GatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }
}

// Microservice (with service discovery)
@EnableDiscoveryClient
@SpringBootApplication
public class UserServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }
}
```

## Spring Boot Concepts

### 33. How SpringBootApplication Works

The `@SpringBootApplication` annotation is a convenience annotation that combines:
1. `@Configuration`: Tags the class as a source of bean definitions
2. `@EnableAutoConfiguration`: Enables Spring Boot's auto-configuration mechanism
3. `@ComponentScan`: Scans for components in the package of the annotated class and sub-packages

**Startup Process**:
1. JVM starts and locates the main class
2. Spring Boot initializes the Spring application context
3. Banner is printed (if enabled)
4. Spring Boot creates beans defined in configuration classes
5. Auto-configuration process runs
6. ApplicationRunner and CommandLineRunner beans are executed
7. Application is considered "started"

**Example**:
```java
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**Behind the scenes**:
```java
@Configuration
@EnableAutoConfiguration
@ComponentScan(basePackages = "com.example.myapp")
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### 34. Difference Between Spring Boot and Spring Framework

**Spring Framework**:
- Core framework providing dependency injection, AOP, etc.
- Requires extensive configuration (XML, Java config)
- Needs explicit server configuration
- Manual dependency management
- Manual setup for production-ready features

**Spring Boot**:
- Built on top of Spring Framework
- Convention over configuration approach
- Embedded server support (Tomcat, Jetty, etc.)
- Starter dependencies (simplified dependency management)
- Auto-configuration
- Production-ready features (metrics, monitoring, etc.)
- Spring Actuator for application insights

**Key Differences**:

1. **Configuration**:
   - Spring Framework: Requires explicit configuration
   - Spring Boot: Provides auto-configuration with sensible defaults

2. **Deployment**:
   - Spring Framework: Typically requires external server setup
   - Spring Boot: Includes embedded servers, standalone applications

3. **Dependencies**:
   - Spring Framework: Manual dependency management
   - Spring Boot: Starter dependencies simplify configuration

4. **Production Readiness**:
   - Spring Framework: Requires manual setup for monitoring, metrics, etc.
   - Spring Boot: Built-in support via Spring Actuator

5. **Development Speed**:
   - Spring Framework: More boilerplate code and configuration
   - Spring Boot: Faster development with less configuration

### 35. @SpringBootApplication and @ComponentScan Annotations

**@SpringBootApplication**:
- Combines `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan`
- Entry point for Spring Boot applications
- Places it on your main class to enable auto-configuration and component scanning

```java
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**@ComponentScan**:
- Tells Spring where to look for components
- Scans the package of the annotated class and its sub-packages by default
- Can be customized to include/exclude specific packages or classes

```java
// Default: scans current package and sub-packages
@ComponentScan
public class Config { /* ... */ }

// Specific base packages
@ComponentScan(basePackages = {"com.example.service", "com.example.repository"})
public class Config { /* ... */ }

// Using classes to define scan packages
@ComponentScan(basePackageClasses = {ServiceMarker.class, RepositoryMarker.class})
public class Config { /* ... */ }

// Include specific components
@ComponentScan(includeFilters = @ComponentScan.Filter(type = FilterType.REGEX, pattern = ".*Service"))
public class Config { /* ... */ }

// Exclude specific components
@ComponentScan(excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Deprecated.class))
public class Config { /* ... */ }
```

Components detected during scanning include:
- `@Component`
- `@Service`
- `@Repository`
- `@Controller`
- `@RestController`
- `@Configuration`

### 36. Define Request and Response Types in Spring Boot REST

```java
// Controller with different request/response types
@RestController
@RequestMapping("/api/users")
public class UserController {

    // JSON response (default)
    @GetMapping
    public List<User> getAllUsers() {
        // Returns JSON by default
        return userService.findAll();
    }
    
    // Specific MediaType for response
    @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public User getUserById(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    // XML response
    @GetMapping(value = "/xml", produces = MediaType.APPLICATION_XML_VALUE)
    public User getUserAsXml(@RequestParam Long id) {
        return userService.findById(id);
    }
    
    // Multiple response types
    @GetMapping(value = "/multi", 
                produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE})
    public User getUserMultiFormat(@RequestParam Long id) {
        return userService.findById(id);
    }
    
    // Accepting specific request type
    @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<User> createUser(@RequestBody User user) {
        User created = userService.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }
    
    // Form-encoded data
    @PostMapping(value = "/form", 
                consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE,
                produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<User> createUserFromForm(@ModelAttribute UserForm form) {
        User user = convertFromForm(form);
        User created = userService.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }
    
    // Custom response type
    @GetMapping(value = "/download", produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
    public ResponseEntity<byte[]> downloadUserData(@RequestParam Long id) {
        byte[] data = userService.generateUserReport(id);
        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=user-" + id + ".pdf")
                .body(data);
    }
    
    // Custom request type with ResponseEntity
    @PostMapping(value = "/upload", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<?> uploadUserPhoto(
            @RequestParam("id") Long id,
            @RequestParam("file") MultipartFile file) {
        try {
            userService.saveUserPhoto(id, file);
            return ResponseEntity.ok("Photo uploaded successfully");
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Failed to upload: " + e.getMessage());
        }
    }
}
```

For XML support, add the following dependency:
```xml
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-xml</artifactId>
</dependency>
```

### 37. Configure Spring to Read Properties Based on Environment

```java
// Option 1: Using application-{profile}.properties files
// application.properties - common properties
// application-dev.properties - development properties
// application-prod.properties - production properties

// Option 2: Setting active profile
// In application.properties
spring.profiles.active=dev

// Or via command line
// java -jar myapp.jar --spring.profiles.active=prod

// Option 3: Using @Profile annotation
@Configuration
@Profile("dev")
public class DevConfig {
    // Development-specific beans
}

@Configuration
@Profile("prod")
public class ProdConfig {
    // Production-specific beans
}

// Option 4: Using @ConfigurationProperties
@Configuration
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private String name;
    private String environment;
    private Map<String, String> features;
    
    // Getters and setters
}

// Option 5: Using Environment directly
@RestController
public class ConfigController {
    @Autowired
    private Environment env;
    
    @GetMapping("/config")
    public String getConfig() {
        return "Database URL: " + env.getProperty("spring.datasource.url");
    }
}

// Option 6: Using @Value annotation
@Service
public class ConfigService {
    @Value("${app.name}")
    private String appName;
    
    @Value("${app.description:Default description}")
    private String description; // With default value
    
    @Value("${app.features}")
    private List<String> features;
}
```

**Example of a complete configuration**:

```java
// Custom PropertySource
@Configuration
public class PropertiesConfig {
    @Bean
    public PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        PropertySourcesPlaceholderConfigurer configurer = new PropertySourcesPlaceholderConfigurer();
        configurer.setIgnoreResourceNotFound(true);
        configurer.setIgnoreUnresolvablePlaceholders(true);
        return configurer;
    }
    
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer(Environment env) {
        PropertySourcesPlaceholderConfigurer configurer = new PropertySourcesPlaceholderConfigurer();
        YamlPropertiesFactoryBean yaml = new YamlPropertiesFactoryBean();
        
        // Load properties based on environment
        String profile = env.getActiveProfiles().length > 0 ? env.getActiveProfiles()[0] : "default";
        Resource[] resources = new Resource[] {
            new ClassPathResource("application.yml"),
            new ClassPathResource("application-" + profile + ".yml")
        };
        
        yaml.setResources(resources);
        configurer.setProperties(yaml.getObject());
        return configurer;
    }
}
```

### 38. Spring Boot Actuator and Its Usage

Spring Boot Actuator provides production-ready features to help monitor and manage your application.

**Setup**:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

**Configuration** (application.properties):
```properties
# Enable all endpoints
management.endpoints.web.exposure.include=*

# Or enable specific endpoints
management.endpoints.web.exposure.include=health,info,metrics,loggers

# Base path for actuator endpoints (default is /actuator)
management.endpoints.web.base-path=/management

# Health endpoint configuration
management.endpoint.health.show-details=always

# Customize info endpoint
info.app.name=My Spring Application
info.app.description=Spring Boot Actuator Demo
info.app.version=1.0.0
```

**Key Endpoints**:
- `/actuator/health`: Application health information
- `/actuator/info`: Application information
- `/actuator/metrics`: Application metrics
- `/actuator/env`: Environment properties
- `/actuator/loggers`: View and modify logger configurations
- `/actuator/mappings`: HTTP request mappings
- `/actuator/beans`: Spring beans in the context
- `/actuator/configprops`: Configuration properties
- `/actuator/threaddump`: Thread dump
- `/actuator/heapdump`: Heap dump (returns a file)

**Custom Health Indicator**:
```java
@Component
public class DatabaseHealthIndicator implements HealthIndicator {
    
    @Autowired
    private DataSource dataSource;
    
    @Override
    public Health health() {
        try (Connection connection = dataSource.getConnection()) {
            PreparedStatement statement = connection.prepareStatement("SELECT 1");
            statement.execute();
            return Health.up()
                .withDetail("database", "Available")
                .withDetail("status", "Connected")
                .build();
        } catch (Exception e) {
            return Health.down()
                .withDetail("database", "Unavailable")
                .withDetail("error", e.getMessage())
                .build();
        }
    }
}
```

**Custom Metrics**:
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private MeterRegistry meterRegistry;
    
    @GetMapping
    public List<User> getAllUsers() {
        // Record metric for API call
        meterRegistry.counter("api.calls", "endpoint", "getAllUsers").increment();
        return userService.findAll();
    }
}
```

**Custom Actuator Endpoint**:
```java
@Component
@Endpoint(id = "customFeatures")
public class FeaturesEndpoint {
    
    @ReadOperation
    public Map<String, Object> features() {
        Map<String, Object> features = new HashMap<>();
        features.put("feature1", true);
        features.put("feature2", false);
        features.put("featureList", Arrays.asList("a", "b", "c"));
        return features;
    }
    
    @ReadOperation
    public String feature(@Selector String name) {
        return "Feature " + name + " details";
    }
    
    @WriteOperation
    public void configureFeature(@Selector String name, @Nullable Boolean enabled) {
        // Toggle feature state
        System.out.println("Toggling feature " + name + " to " + enabled);
    }
}
```

### 39. Setting Active Profiles in Spring Boot

**1. Using application.properties/yml**:
```properties
# application.properties
spring.profiles.active=dev
```

```yaml
# application.yml
spring:
  profiles:
    active: dev
```

**2. Using command-line arguments**:
```bash
java -jar myapp.jar --spring.profiles.active=prod
```

**3. Using environment variables**:
```bash
export SPRING_PROFILES_ACTIVE=prod
java -jar myapp.jar
```

**4. Using JVM system properties**:
```bash
java -Dspring.profiles.active=prod -jar myapp.jar
```

**5. Programmatically**:
```java
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication application = new SpringApplication(MyApplication.class);
        application.setAdditionalProfiles("prod");
        application.run(args);
    }
}
```

**6. Using Spring Boot starter class**:
```java
@SpringBootApplication
public class MyApplication {
    
    @Autowired
    private ConfigurableEnvironment env;
    
    @PostConstruct
    public void setup() {
        env.setActiveProfiles("prod");
    }
    
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**Using profiles with beans**:
```java
@Component
@Profile("dev")
public class DevDataInitializer implements CommandLineRunner {
    @Override
    public void run(String... args) {
        // Initialize development data
    }
}

@Component
@Profile("prod")
public class ProdDataInitializer implements CommandLineRunner {
    @Override
    public void run(String... args) {
        // Initialize production data
    }
}
```

**Multiple active profiles**:
```properties
spring.profiles.active=prod,metrics,actuator
```

**Profile-specific properties**:
- `application-dev.properties`
- `application-prod.properties`
- `application-test.properties`

### 40. ORM Technologies Configuration in Spring Boot

**1. Hibernate/JPA with Spring Boot**:

Add dependencies:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

Configuration in application.properties:
```properties
# Database connection
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=password
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# Hibernate properties
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL5InnoDBDialect
```

Entity class:
```java
@Entity
@Table(name = "users")
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "first_name", nullable = false)
    private String firstName;
    
    @Column(name = "last_name")
    private String lastName;
    
    @Column(unique = true)
    private String email;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Order> orders;
    
    // Getters and setters
}
```

Spring Data JPA Repository:
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    List<User> findByLastName(String lastName);
    
    @Query("SELECT u FROM User u WHERE u.email LIKE %:domain%")
    List<User> findByEmailDomain(@Param("domain") String domain);
}
```

Service class:
```java
@Service
@Transactional
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public User findById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new EntityNotFoundException("User not found"));
    }
    
    public List<User> findAll() {
        return userRepository.findAll();
    }
    
    public User save(User user) {
        return userRepository.save(user);
    }
    
    public void delete(Long id) {
        userRepository.deleteById(id);
    }
}
```

**2. Custom Hibernate Configuration**:

```java
@Configuration
@EnableTransactionManagement
public class HibernateConfig {
    
    @Autowired
    private Environment env;
    
    @Bean
    public LocalSessionFactoryBean sessionFactory() {
        LocalSessionFactoryBean sessionFactory = new LocalSessionFactoryBean();
        sessionFactory.setDataSource(dataSource());
        sessionFactory.setPackagesToScan("com.example.model");
        sessionFactory.setHibernateProperties(hibernateProperties());
        return sessionFactory;
    }
    
    @Bean
    public DataSource dataSource() {
        HikariDataSource dataSource = new HikariDataSource();
        dataSource.setDriverClassName(env.getProperty("spring.datasource.driver-class-name"));
        dataSource.setJdbcUrl(env.getProperty("spring.datasource.url"));
        dataSource.setUsername(env.getProperty("spring.datasource.username"));
        dataSource.setPassword(env.getProperty("spring.datasource.password"));
        dataSource.setMaximumPoolSize(10);
        return dataSource;
    }
    
    @Bean
    public PlatformTransactionManager hibernateTransactionManager() {
        HibernateTransactionManager transactionManager = new HibernateTransactionManager();
        transactionManager.setSessionFactory(sessionFactory().getObject());
        return transactionManager;
    }
    
    private Properties hibernateProperties() {
        Properties properties = new Properties();
        properties.put("hibernate.dialect", env.getProperty("spring.jpa.properties.hibernate.dialect"));
        properties.put("hibernate.show_sql", env.getProperty("spring.jpa.show-sql"));
        properties.put("hibernate.format_sql", env.getProperty("spring.jpa.properties.hibernate.format_sql"));
        properties.put("hibernate.hbm2ddl.auto", env.getProperty("spring.jpa.hibernate.ddl-auto"));
        return properties;
    }
}
```

### 41. REST WebService with OAuth2.0 in Spring Boot

**1. Add dependencies**:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.security.oauth.boot</groupId>
    <artifactId>spring-security-oauth2-autoconfigure</artifactId>
    <version>2.5.2</version>
</dependency>
```

**2. Configure OAuth2 Server**:
```java
@Configuration
@EnableAuthorizationServer
public class AuthServerConfig extends AuthorizationServerConfigurerAdapter {
    
    @Autowired
    private AuthenticationManager authenticationManager;
    
    @Autowired
    private PasswordEncoder passwordEncoder;
    
    @Override
    public void configure(ClientDetailsServiceConfigurer clients) throws Exception {
        clients.inMemory()
            .withClient("client-id")
            .secret(passwordEncoder.encode("client-secret"))
            .authorizedGrantTypes("password", "refresh_token")
            .scopes("read", "write")
            .accessTokenValiditySeconds(3600)
            .refreshTokenValiditySeconds(86400);
    }
    
    @Override
    public void configure(AuthorizationServerEndpointsConfigurer endpoints) {
        endpoints.authenticationManager(authenticationManager);
    }
}
```

**3. Configure Security**:
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Autowired
    private UserDetailsService userDetailsService;
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService)
            .passwordEncoder(passwordEncoder());
    }
    
    @Override
    @Bean
    public AuthenticationManager authenticationManagerBean() throws Exception {
        return super.authenticationManagerBean();
    }
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .authorizeRequests()
            .antMatchers("/api/public/**").permitAll()
            .anyRequest().authenticated();
    }
}
```

**4. Implement User Details Service**:
```java
@Service
public class CustomUserDetailsService implements UserDetailsService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found: " + username));
        
        return new org.springframework.security.core.userdetails.User(
            user.getUsername(),
            user.getPassword(),
            getAuthorities(user.getRoles())
        );
    }
    
    private Collection<? extends GrantedAuthority> getAuthorities(List<String> roles) {
        return roles.stream()
            .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
            .collect(Collectors.toList());
    }
}
```

**5. Create REST Controller**:
```java
@RestController
@RequestMapping("/api")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/public/info")
    public String publicInfo() {
        return "This is public information";
    }
    
    @GetMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public List<User> getAllUsers() {
        return userService.findAll();
    }
    
    @GetMapping("/users/{id}")
    @PreAuthorize("hasRole('USER')")
    public User getUserById(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PostMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public User createUser(@RequestBody User user) {
        return userService.save(user);
    }
    
    @GetMapping("/me")
    public UserDetails getCurrentUser(Principal principal) {
        return (UserDetails) ((Authentication) principal).getPrincipal();
    }
}
```

**6. Resource Server Configuration**:
```java
@Configuration
@EnableResourceServer
public class ResourceServerConfig extends ResourceServerConfigurerAdapter {
    
    @Override
    public void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
            .antMatchers("/api/public/**").permitAll()
            .antMatchers("/api/admin/**").hasRole("ADMIN")
            .antMatchers("/api/**").authenticated();
    }
}
```

### 42. Making SOAP Call from Spring Boot with SSL Certificate

**1. Add dependencies**:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web-services</artifactId>
</dependency>
```

**2. Configure SOAP client**:
```java
@Configuration
public class SoapClientConfig {
    
    @Bean
    public Jaxb2Marshaller marshaller() {
        Jaxb2Marshaller marshaller = new Jaxb2Marshaller();
        marshaller.setContextPath("com.example.generated");
        return marshaller;
    }
    
    @Bean
    public WebServiceTemplate webServiceTemplate(Jaxb2Marshaller marshaller) {
        WebServiceTemplate template = new WebServiceTemplate();
        template.setMarshaller(marshaller);
        template.setUnmarshaller(marshaller);
        template.setMessageFactory(messageFactory());
        
        // Configure HTTP client
        HttpsUrlConnectionMessageSender messageSender = new HttpsUrlConnectionMessageSender();
        messageSender.setTrustManagers(trustManager());
        messageSender.setKeyManagers(keyManager());
        template.setMessageSender(messageSender);
        
        return template;
    }
    
    @Bean
    public SaajSoapMessageFactory messageFactory() {
        SaajSoapMessageFactory factory = new SaajSoapMessageFactory();
        factory.setSoapVersion(SoapVersion.SOAP_12);
        return factory;
    }
    
    private TrustManager[] trustManager() {
        try {
            KeyStore trustStore = KeyStore.getInstance("JKS");
            try (InputStream is = new FileInputStream("truststore.jks")) {
                trustStore.load(is, "truststore-password".toCharArray());
            }
            
            TrustManagerFactory trustManagerFactory = 
                TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            trustManagerFactory.init(trustStore);
            return trustManagerFactory.getTrustManagers();
        } catch (Exception e) {
            throw new RuntimeException("Error creating trust manager", e);
        }
    }
    
    private KeyManager[] keyManager() {
        try {
            KeyStore keyStore = KeyStore.getInstance("JKS");
            try (InputStream is = new FileInputStream("keystore.jks")) {
                keyStore.load(is, "keystore-password".toCharArray());
            }
            
            KeyManagerFactory keyManagerFactory = 
                KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
            keyManagerFactory.init(keyStore, "key-password".toCharArray());
            return keyManagerFactory.getKeyManagers();
        } catch (Exception e) {
            throw new RuntimeException("Error creating key manager", e);
        }
    }
}
```

**3. Create SOAP client service**:
```java
@Service
public class SoapClientService {
    
    @Autowired
    private WebServiceTemplate webServiceTemplate;
    
    public GetWeatherResponse getWeather(String city) {
        GetWeatherRequest request = new GetWeatherRequest();
        request.setCity(city);
        
        try {
            return (GetWeatherResponse) webServiceTemplate.marshalSendAndReceive(
                "https://example.com/soap/weather", 
                request,
                new SoapActionCallback("http://example.com/GetWeather")
            );
        } catch (WebServiceIOException e) {
            // Handle SSL/connection errors
            throw new RuntimeException("Error connecting to SOAP service", e);
        } catch (WebServiceClientException e) {
            // Handle other client errors
            throw new RuntimeException("Error invoking SOAP service", e);
        }
    }
}
```

**4. Alternative approach using Apache CXF**:
```java
@Configuration
public class CxfClientConfig {
    
    @Bean
    public WeatherService weatherService() throws Exception {
        JaxWsProxyFactoryBean factory = new JaxWsProxyFactoryBean();
        factory.setServiceClass(WeatherService.class);
        factory.setAddress("https://example.com/soap/weather");
        
        // SSL configuration
        HTTPConduit conduit = (HTTPConduit) factory.getOutInterceptors();
        TLSClientParameters tlsParams = new TLSClientParameters();
        
        // Trust store configuration
        KeyStore trustStore = KeyStore.getInstance("JKS");
        trustStore.load(new FileInputStream("truststore.jks"), "password".toCharArray());
        TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        tmf.init(trustStore);
        tlsParams.setTrustManagers(tmf.getTrustManagers());
        
        // Key store configuration
        KeyStore keyStore = KeyStore.getInstance("JKS");
        keyStore.load(new FileInputStream("keystore.jks"), "password".toCharArray());
        KeyManagerFactory kmf = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
        kmf.init(keyStore, "password".toCharArray());
        tlsParams.setKeyManagers(kmf.getKeyManagers());
        
        conduit.setTlsClientParameters(tlsParams);
        
        return (WeatherService) factory.create();
    }
}
```

### 43. Configure Different Data Sources in Spring Boot

**1. Using application.properties**:
```properties
# Primary DataSource
spring.datasource.primary.jdbc-url=jdbc:mysql://localhost:3306/primary_db
spring.datasource.primary.username=root
spring.datasource.primary.password=password
spring.datasource.primary.driver-class-name=com.mysql.cj.jdbc.Driver

# Secondary DataSource
spring.datasource.secondary.jdbc-url=jdbc:postgresql://localhost:5432/secondary_db
spring.datasource.secondary.username=postgres
spring.datasource.secondary.password=password
spring.datasource.secondary.driver-class-name=org.postgresql.Driver
```

**2. Configure multiple DataSources**:
```java
@Configuration
@EnableTransactionManagement
@EnableJpaRepositories(
    basePackages = {"com.example.repository.primary"},
    entityManagerFactoryRef = "primaryEntityManagerFactory",
    transactionManagerRef = "primaryTransactionManager"
)
public class PrimaryDataSourceConfig {
    
    @Primary
    @Bean
    @ConfigurationProperties("spring.datasource.primary")
    public DataSourceProperties primaryDataSourceProperties() {
        return new DataSourceProperties();
    }
    
    @Primary
    @Bean
    @ConfigurationProperties("spring.datasource.primary.configuration")
    public DataSource primaryDataSource() {
        return primaryDataSourceProperties()
            .initializeDataSourceBuilder()
            .type(HikariDataSource.class)
            .build();
    }
    
    @Primary
    @Bean
    public LocalContainerEntityManagerFactoryBean primaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder) {
        return builder
            .dataSource(primaryDataSource())
            .packages("com.example.model.primary")
            .persistenceUnit("primary")
            .properties(jpaProperties())
            .build();
    }
    
    @Primary
    @Bean
    public PlatformTransactionManager primaryTransactionManager(
            @Qualifier("primaryEntityManagerFactory") EntityManagerFactory entityManagerFactory) {
        return new JpaTransactionManager(entityManagerFactory);
    }
    
    private Map<String, Object> jpaProperties() {
        Map<String, Object> props = new HashMap<>();
        props.put("hibernate.dialect", "org.hibernate.dialect.MySQL5InnoDBDialect");
        props.put("hibernate.hbm2ddl.auto", "update");
        return props;
    }
}
```

```java
@Configuration
@EnableTransactionManagement
@EnableJpaRepositories(
    basePackages = {"com.example.repository.secondary"},
    entityManagerFactoryRef = "secondaryEntityManagerFactory",
    transactionManagerRef = "secondaryTransactionManager"
)
public class SecondaryDataSourceConfig {
    
    @Bean
    @ConfigurationProperties("spring.datasource.secondary")
    public DataSourceProperties secondaryDataSourceProperties() {
        return new DataSourceProperties();
    }
    
    @Bean
    @ConfigurationProperties("spring.datasource.secondary.configuration")
    public DataSource secondaryDataSource() {
        return secondaryDataSourceProperties()
            .initializeDataSourceBuilder()
            .type(HikariDataSource.class)
            .build();
    }
    
    @Bean
    public LocalContainerEntityManagerFactoryBean secondaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder) {
        return builder
            .dataSource(secondaryDataSource())
            .packages("com.example.model.secondary")
            .persistenceUnit("secondary")
            .properties(jpaProperties())
            .build();
    }
    
    @Bean
    public PlatformTransactionManager secondaryTransactionManager(
            @Qualifier("secondaryEntityManagerFactory") EntityManagerFactory entityManagerFactory) {
        return new JpaTransactionManager(entityManagerFactory);
    }
    
    private Map<String, Object> jpaProperties() {
        Map<String, Object> props = new HashMap<>();
        props.put("hibernate.dialect", "org.hibernate.dialect.PostgreSQLDialect");
        props.put("hibernate.hbm2ddl.auto", "update");
        return props;
    }
}
```

**3. Create separate repositories**:
```java
// Primary repository
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // Methods
}

// Secondary repository
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    // Methods
}
```

**4. Use in service**:
```java
@Service
public class ApplicationService {
    
    @Autowired
    private UserRepository userRepository; // Primary datasource
    
    @Autowired
    private ProductRepository productRepository; // Secondary datasource
    
    @Transactional("primaryTransactionManager")
    public void saveUserData(User user) {
        userRepository.save(user);
    }
    
    @Transactional("secondaryTransactionManager")
    public void saveProductData(Product product) {
        productRepository.save(product);
    }
    
    // Cross-datasource transaction (requires additional setup)
    public void saveUserAndProduct(User user, Product product) {
        saveUserData(user);
        saveProductData(product);
    }
}
```

### 44. Exception Handling in Spring Boot

**1. Using @ExceptionHandler annotation**:
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    // Controller methods
    
    @ExceptionHandler(UserNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleUserNotFound(UserNotFoundException ex) {
        return new ErrorResponse("USER_NOT_FOUND", ex.getMessage());
    }
    
    @ExceptionHandler(ValidationException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleValidation(ValidationException ex) {
        return new ErrorResponse("VALIDATION_ERROR", ex.getMessage());
    }
}
```

**2. Using @ControllerAdvice for global exception handling**:
```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(EntityNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleEntityNotFound(EntityNotFoundException ex) {
        return new ErrorResponse("ENTITY_NOT_FOUND", ex.getMessage());
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleValidationExceptions(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error -> 
            errors.put(error.getField(), error.getDefaultMessage()));
        
        return new ErrorResponse("VALIDATION_ERROR", "Validation failed", errors);
    }
    
    @ExceptionHandler(AccessDeniedException.class)
    @ResponseStatus(HttpStatus.FORBIDDEN)
    public ErrorResponse handleAccessDenied(AccessDeniedException ex) {
        return new ErrorResponse("ACCESS_DENIED", "You don't have permission to access this resource");
    }
    
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleAllUncaughtException(Exception ex) {
        return new ErrorResponse("INTERNAL_SERVER_ERROR", "An unexpected error occurred");
    }
}
```

**3. Custom error response class**:
```java
public class ErrorResponse {
    private final String code;
    private final String message;
    private final Map<String, Object> details;
    private final LocalDateTime timestamp;
    
    public ErrorResponse(String code, String message) {
        this.code = code;
        this.message = message;
        this.details = new HashMap<>();
        this.timestamp = LocalDateTime.now();
    }
    
    public ErrorResponse(String code, String message, Map<String, String> errors) {
        this.code = code;
        this.message = message;
        this.details = new HashMap<>(errors);
        this.timestamp = LocalDateTime.now();
    }
    
    // Getters
}
```

**4. Custom exception classes**:
```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String message) {
        super(message);
    }
}

public class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}
```

**5. Handling validation errors with Bean Validation (JSR-380)**:
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        // The @Valid annotation triggers validation
        // If validation fails, MethodArgumentNotValidException is thrown
        User savedUser = userService.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedUser);
    }
}

@Entity
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @NotBlank(message = "Name is required")
    private String name;
    
    @Email(message = "Email should be valid")
    @NotBlank(message = "Email is required")
    private String email;
    
    @Size(min = 8, message = "Password must be at least 8 characters long")
    private String password;
    
    // Getters and setters
}
```

### 45. Troubleshooting "Application Context Failed" Error

When facing "Application context is getting failed" errors in Spring Boot:

**1. Check Logs Carefully**:
- Look for specific error messages
- Check stack traces
- Look for "Caused by:" sections

**2. Common Causes & Solutions**:

a) **Bean Creation Failure**:
```
// Problem: Circular dependencies between beans
@Service
public class ServiceA {
    @Autowired
    private ServiceB serviceB;
}

@Service
public class ServiceB {
    @Autowired
    private ServiceA serviceA;
}

// Solution: Use setter injection or @Lazy annotation
@Service
public class ServiceA {
    private ServiceB serviceB;
    
    @Autowired
    public void setServiceB(ServiceB serviceB) {
        this.serviceB = serviceB;
    }
}
```

b) **Property Configuration Issues**:
```
// Problem: Missing required property
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
# Missing username and password

// Solution: Add missing properties
spring.datasource.username=root
spring.datasource.password=password
```

c) **Bean Not Found**:
```
// Problem: Required bean not available
@Autowired
private MissingService service;

// Solution: Create the bean or use conditional wiring
@Autowired(required = false)
private MissingService service;

// Or use conditional checks
@ConditionalOnClass(name = "com.example.MissingService")
@Bean
public MyBean myBean() {
    return new MyBean();
}
```

d) **Database Connection Issues**:
```
// Problem: Database connection fails
// Solution: Check connection parameters and database status
spring.datasource.url=jdbc:mysql://localhost:3306/correct_db_name
spring.datasource.username=correct_username
spring.datasource.password=correct_password

// Add connection validation
spring.datasource.hikari.connection-test-query=SELECT 1
```

e) **Port Already in Use**:
```
// Problem: Default port 8080 is already in use
// Solution: Change the port
server.port=8081
```

f) **Dependency Conflicts**:
- Use `mvn dependency:tree` to identify conflicts
- Exclude conflicting dependencies

**3. Debugging Strategies**:

a) **Enable debug logs**:
```properties
# In application.properties
logging.level.org.springframework=DEBUG
logging.level.com.example=TRACE
```

b) **Run with --debug flag**:
```bash
java -jar myapp.jar --debug
```

c) **Use Spring Boot Actuator**:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

d) **Check bean wiring**:
```properties
logging.level.org.springframework.beans.factory.support=DEBUG
```

e) **Step-by-step troubleshooting**:
1. Comment out parts of the configuration
2. Start with minimal configuration
3. Add components gradually
4. Test each step

**4. Common Error Patterns & Solutions**:

a) **NoSuchBeanDefinitionException**:
- Check component scanning configuration
- Verify bean name and type
- Check if conditional bean creation is failing

b) **BeanCreationException**:
- Check constructor arguments
- Verify autowired dependencies
- Check bean initialization code

c) **DataSourceAutoConfiguration failure**:
- Check database properties
- Ensure database is running
- Verify database user permissions

d) **Port binding failures**:
- Change server port
- Stop applications using the same port

e) **Missing class errors**:
- Check dependencies
- Ensure required classes are on classpath

### 46. Prototype Bean in Spring

A prototype bean is a bean with scope "prototype", meaning Spring creates a new instance every time the bean is requested.

**1. Bean Scopes in Spring**:
- **singleton**: Default scope; one instance per Spring container
- **prototype**: New instance created for each request
- **request**: New instance per HTTP request
- **session**: New instance per HTTP session
- **application**: One instance per ServletContext
- **websocket**: One instance per WebSocket

**2. Defining Prototype Beans**:

Using annotation:
```java
@Component
@Scope("prototype")
public class PrototypeBean {
    private String message;
    
    public PrototypeBean() {
        System.out.println("PrototypeBean instance created");
    }
    
    // Getters and setters
}
```

Using Java configuration:
```java
@Configuration
public class AppConfig {
    
    @Bean
    @Scope("prototype")
    public PrototypeBean prototypeBean() {
        return new PrototypeBean();
    }
}
```

Using constant:
```java
@Component
@Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE)
public class PrototypeBean {
    // Class implementation
}
```

**3. Usage and Behavior**:
```java
@Service
public class MyService {
    
    @Autowired
    private ApplicationContext context;
    
    public void demonstratePrototype() {
        // Each call gets a new instance
        PrototypeBean bean1 = context.getBean(PrototypeBean.class);
        PrototypeBean bean2 = context.getBean(PrototypeBean.class);
        
        System.out.println("bean1 == bean2: " + (bean1 == bean2)); // false
    }
}
```

**4. Prototype Bean in Singleton**:
```java
@Component
public class SingletonBean {
    
    @Autowired
    private PrototypeBean prototypeBean; // Always the same instance!
    
    public PrototypeBean getPrototypeBean() {
        return prototypeBean;
    }
}
```

**5. Solving the Prototype in Singleton Problem**:

Method 1: Using ApplicationContext:
```java
@Component
public class SingletonBean {
    
    @Autowired
    private ApplicationContext context;
    
    public PrototypeBean getPrototypeBean() {
        return context.getBean(PrototypeBean.class); // Always a new instance
    }
}
```

Method 2: Using Provider:
```java
@Component
public class SingletonBean {
    
    @Autowired
    private Provider<PrototypeBean> prototypeBeanProvider;
    
    public PrototypeBean getPrototypeBean() {
        return prototypeBeanProvider.get(); // Always a new instance
    }
}
```

Method 3: Using lookup method:
```java
@Component
public abstract class SingletonBean {
    
    @Lookup
    public abstract PrototypeBean getPrototypeBean(); // Spring provides implementation
}
```

Method 4: Using scoped proxy:
```java
@Component
@Scope(value = ConfigurableBeanFactory.SCOPE_PROTOTYPE, proxyMode = ScopedProxyMode.TARGET_CLASS)
public class PrototypeBean {
    // Implementation
}

@Component
public class SingletonBean {
    
    @Autowired
    private PrototypeBean prototypeBean; // Actually a proxy
    
    public PrototypeBean getPrototypeBean() {
        return prototypeBean; // New instance each time method is called
    }
}
```

**6. When to Use Prototype Beans**:
- Stateful objects where each caller needs its own instance
- Objects that are expensive to create and cannot be shared
- Objects with mutable state that should not be shared
- When thread safety is a concern

### 47. Configuration Properties Service in Spring Boot

**1. Add dependency**:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```

**2. Create configuration properties class**:
```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
public class AppProperties {
    
    @NotNull
    private String name;
    
    private String description;
    
    @Min(1)
    @Max(100)
    private int maxConnections = 10;
    
    private Map<String, String> features = new HashMap<>();
    
    private Security security = new Security();
    
    // Nested configuration class
    public static class Security {
        private boolean enabled = true;
        private String tokenSecret;
        private int tokenExpirationDays = 7;
        
        // Getters and setters
    }
    
    // Getters and setters
}
```

**3. Create configuration properties service**:
```java
@Service
public class ConfigurationPropertiesService {
    
    private final AppProperties appProperties;
    
    public ConfigurationPropertiesService(AppProperties appProperties) {
        this.appProperties = appProperties;
    }
    
    public String getAppName() {
        return appProperties.getName();
    }
    
    public String getAppDescription() {
        return appProperties.getDescription();
    }
    
    public int getMaxConnections() {
        return appProperties.getMaxConnections();
    }
    
    public Map<String, String> getFeatures() {
        return new HashMap<>(appProperties.getFeatures());
    }
    
    public boolean isSecurityEnabled() {
        return appProperties.getSecurity().isEnabled();
    }
    
    public String getTokenSecret() {
        return appProperties.getSecurity().getTokenSecret();
    }
    
    public int getTokenExpirationDays() {
        return appProperties.getSecurity().getTokenExpirationDays();
    }
}
```

**4. Configuration in application.properties**:
```properties
# App properties
app.name=My Spring Application
app.description=Configuration Properties Demo
app.max-connections=20

# Features map
app.features.feature1=enabled
app.features.feature2=disabled

# Security configuration
app.security.enabled=true
app.security.token-secret=my-secret-token-key
app.security.token-expiration-days=30
```

**5. Enable configuration properties**:
```java
@SpringBootApplication
@EnableConfigurationProperties(AppProperties.class)
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**6. Use in controller or service**:
```java
@RestController
@RequestMapping("/api/config")
public class ConfigController {
    
    private final ConfigurationPropertiesService configService;
    
    public ConfigController(ConfigurationPropertiesService configService) {
        this.configService = configService;
    }
    
    @GetMapping
    public Map<String, Object> getConfig() {
        Map<String, Object> config = new HashMap<>();
        config.put("name", configService.getAppName());
        config.put("description", configService.getAppDescription());
        config.put("maxConnections", configService.getMaxConnections());
        config.put("features", configService.getFeatures());
        config.put("securityEnabled", configService.isSecurityEnabled());
        
        return config;
    }
}
```

**7. Using environment-specific properties**:
```
# application-dev.properties
app.name=My Dev Application
app.max-connections=5

# application-prod.properties
app.name=My Production Application
app.max-connections=50
```

### 48. Circuit Breaker Design Pattern

The Circuit Breaker pattern is used to detect failures and prevent cascading failures in distributed systems.

**1. How it works**:
- **Closed State**: Normal operation; requests pass through
- **Open State**: Failure detected; requests fail fast without calling the service
- **Half-Open State**: After a timeout, allows limited requests to test if service is healthy

**2. Implementation with Spring Cloud Circuit Breaker** (Resilience4J):

Add dependencies:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
</dependency>
```

Configuration:
```java
@Configuration
public class CircuitBreakerConfig {
    
    @Bean
    public Customizer<Resilience4JCircuitBreakerFactory> defaultCustomizer() {
        return factory -> factory.configureDefault(id -> new Resilience4JConfigBuilder(id)
                .timeLimiterConfig(TimeLimiterConfig.custom().timeoutDuration(Duration.ofSeconds(3)).build())
                .circuitBreakerConfig(CircuitBreakerConfig.custom()
                        .failureRateThreshold(50)
                        .waitDurationInOpenState(Duration.ofSeconds(10))
                        .slidingWindowSize(5)
                        .permittedNumberOfCallsInHalfOpenState(3)
                        .build())
                .build());
    }
}
```

Usage in service:
```java
@Service
public class UserService {
    
    private final RestTemplate restTemplate;
    private final CircuitBreakerFactory circuitBreakerFactory;
    
    public UserService(RestTemplate restTemplate, CircuitBreakerFactory circuitBreakerFactory) {
        this.restTemplate = restTemplate;
        this.circuitBreakerFactory = circuitBreakerFactory;
    }
    
    public User getUserById(Long id) {
        CircuitBreaker circuitBreaker = circuitBreakerFactory.create("userService");
        
        return circuitBreaker.run(
            () -> restTemplate.getForObject("http://user-service/users/" + id, User.class),
            throwable -> getFallbackUser(id)
        );
    }
    
    private User getFallbackUser(Long id) {
        // Return default user or cached data
        return new User(id, "Fallback User", "N/A");
    }
}
```

**3. Using Resilience4J directly**:

```java
@Service
public class UserService {
    
    private final RestTemplate restTemplate;
    private final CircuitBreaker circuitBreaker;
    
    public UserService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
        
        // Create CircuitBreaker config
        CircuitBreakerConfig config = CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofSeconds(10))
            .slidingWindowSize(5)
            .permittedNumberOfCallsInHalfOpenState(3)
            .build();
        
        // Create CircuitBreaker registry
        CircuitBreakerRegistry registry = CircuitBreakerRegistry.of(config);
        
        // Get CircuitBreaker instance
        this.circuitBreaker = registry.circuitBreaker("userService");
    }
    
    public User getUserById(Long id) {
        Supplier<User> supplier = () -> restTemplate.getForObject(
            "http://user-service/users/" + id, User.class);
        
        Function<Throwable, User> fallbackFunction = throwable -> {
            System.err.println("Error calling user service: " + throwable.getMessage());
            return new User(id, "Fallback User", "N/A");
        };
        
        return Try.ofSupplier(CircuitBreaker.decorateSupplier(circuitBreaker, supplier))
            .recover(fallbackFunction)
            .get();
    }
}
```

**4. Using annotation-based Resilience4J**:

```java
@Configuration
@EnableCircuitBreaker
public class ResilienceConfig {
    
    @Bean
    public CircuitBreakerAspect circuitBreakerAspect() {
        return new CircuitBreakerAspect();
    }
}

@Service
public class UserService {
    
    private final RestTemplate restTemplate;
    
    public UserService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }
    
    @CircuitBreaker(name = "userService", fallbackMethod = "getFallbackUser")
    public User getUserById(Long id) {
        return restTemplate.getForObject("http://user-service/users/" + id, User.class);
    }
    
    public User getFallbackUser(Long id, Exception e) {
        System.err.println("Error calling user service: " + e.getMessage());
        return new User(id, "Fallback User", "N/A");
    }
}
```

### 49. Singleton Pattern Implementation

```java
// Basic Singleton (not thread-safe)
public class BasicSingleton {
    private static BasicSingleton instance;
    
    private BasicSingleton() {
        // Private constructor prevents instantiation
    }
    
    public static BasicSingleton getInstance() {
        if (instance == null) {
            instance = new BasicSingleton();
        }
        return instance;
    }
    
    public void someMethod() {
        System.out.println("Singleton method called");
    }
}

// Thread-safe Singleton with eager initialization
public class EagerSingleton {
    // Instance created at class loading time
    private static final EagerSingleton INSTANCE = new EagerSingleton();
    
    private EagerSingleton() {
        // Private constructor
    }
    
    public static EagerSingleton getInstance() {
        return INSTANCE;
    }
}

// Thread-safe Singleton with lazy initialization
public class LazyThreadSafeSingleton {
    private static volatile LazyThreadSafeSingleton instance;
    
    private LazyThreadSafeSingleton() {
        // Private constructor
    }
    
    // Synchronized method for thread safety
    public static synchronized LazyThreadSafeSingleton getInstance() {
        if (instance == null) {
            instance = new LazyThreadSafeSingleton();
        }
        return instance;
    }
}

// Double-checked locking Singleton (efficient thread-safe)
public class DoubleCheckedSingleton {
    private static volatile DoubleCheckedSingleton instance;
    
    private DoubleCheckedSingleton() {
        // Private constructor
    }
    
    public static DoubleCheckedSingleton getInstance() {
        // First check (no locking)
        if (instance == null) {
            // Lock only if instance is null
            synchronized (DoubleCheckedSingleton.class) {
                // Second check (with locking)
                if (instance == null) {
                    instance = new DoubleCheckedSingleton();
                }
            }
        }
        return instance;
    }
}

// Bill Pugh Singleton (thread-safe, lazy loading)
public class BillPughSingleton {
    private BillPughSingleton() {
        // Private constructor
    }
    
    // Static inner helper class
    private static class SingletonHelper {
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }
    
    public static BillPughSingleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}

// Enum Singleton (simplest and most effective)
public enum EnumSingleton {
    INSTANCE;
    
    public void someMethod() {
        System.out.println("Enum singleton method called");
    }
}
```

### 50. Spring Boot Application Deployment in Cloud

**1. Containerized Deployment with Docker**:

Create a Dockerfile:
```dockerfile
FROM openjdk:11-jre-slim
VOLUME /tmp
COPY target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

Build and push Docker image:
```bash
docker build -t myapp .
docker tag myapp username/myapp:latest
docker push username/myapp:latest
```

**2. Kubernetes Deployment**:

Create a deployment.yaml:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-boot-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: spring-boot-app
  template:
    metadata:
      labels:
        app: spring-boot-app
    spec:
      containers:
      - name: spring-boot-app
        image: username/myapp:latest
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "prod"
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db.host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db.password
```

Create a service.yaml:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: spring-boot-app
spec:
  selector:
    app: spring-boot-app
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

Deploy to Kubernetes:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

**3. AWS Elastic Beanstalk Deployment**:

Configure application.properties:
```properties
# For AWS RDS
spring.datasource.url=jdbc:mysql://${RDS_HOSTNAME}:${RDS_PORT}/${RDS_DB_NAME}
spring.datasource.username=${RDS_USERNAME}
spring.datasource.password=${RDS_PASSWORD}

# Port configuration for Elastic Beanstalk
server.port=5000
```

Package the application:
```bash
mvn clean package
```

Deploy to Elastic Beanstalk using AWS CLI:
```bash
eb init -p java my-spring-app
eb create prod-env
```

**4. Cloud Foundry Deployment**:

Create manifest.yml:
```yaml
applications:
- name: spring-boot-app
  memory: 1G
  instances: 2
  path: target/myapp-0.0.1-SNAPSHOT.jar
  env:
    SPRING_PROFILES_ACTIVE: cloud
    JBP_CONFIG_SPRING_AUTO_RECONFIGURATION: '{enabled: false}'
```

Deploy to Cloud Foundry:
```bash
cf push
```

**5. Azure App Service Deployment**:

Configure application for Azure:
```properties
# Azure App Service configuration
spring.datasource.url=jdbc:mysql://${AZURE_MYSQL_HOST}:3306/${AZURE_MYSQL_DB}
spring.datasource.username=${AZURE_MYSQL_USERNAME}
spring.datasource.password=${AZURE_MYSQL_PASSWORD}
```

Deploy using Azure CLI:
```bash
az login
az webapp up --name my-spring-app --resource-group my-resource-group --plan my-app-plan --sku F1
```

### 51. Microservice Architecture

**What is a Microservice?**
A microservice architecture is an architectural style that structures an application as a collection of loosely coupled, independently deployable services.

**Pros of Microservices**:
1. **Independent Development**: Teams can work on different services simultaneously
2. **Independent Deployment**: Services can be deployed without affecting the entire system
3. **Technology Diversity**: Each service can use different technologies
4. **Resilience**: Failure in one service doesn't bring down the entire system
5. **Scalability**: Individual services can be scaled independently based on demand
6. **Easier Maintenance**: Smaller codebases are easier to understand and maintain
7. **Focused Teams**: Teams can be organized around business capabilities

**Cons of Microservices**:
1. **Distributed System Complexity**: Managing distributed systems is challenging
2. **Network Latency**: Communication between services adds latency
3. **Data Consistency**: Maintaining data consistency across services is difficult
4. **Testing Complexity**: Integration testing becomes more complex
5. **Operational Overhead**: More services mean more operational work
6. **Development Environment**: Setting up a local development environment is challenging
7. **Monitoring Challenges**: Monitoring multiple services requires sophisticated tools

**Implementation Considerations**:

1. **Service Boundaries**:
   - Define boundaries based on business capabilities
   - Follow Domain-Driven Design principles
   - Keep services focused on a single responsibility

2. **Inter-Service Communication**:
   - REST APIs for synchronous communication
   - Message brokers (Kafka, RabbitMQ) for asynchronous communication
   - Consider gRPC for high-performance communication

3. **Data Management**:
   - Database per service
   - Event sourcing
   - CQRS (Command Query Responsibility Segregation)
   - Saga pattern for distributed transactions

4. **Service Discovery**:
   - Eureka
   - Consul
   - Kubernetes Service Discovery

5. **API Gateway**:
   - Single entry point for clients
   - Routing
   - Authentication/Authorization
   - Rate limiting

6. **Circuit Breaker**:
   - Prevent cascading failures
   - Implement fallback mechanisms
   - Resilience4j, Hystrix

7. **Monitoring & Observability**:
   - Centralized logging (ELK stack)
   - Distributed tracing (Zipkin, Jaeger)
   - Health monitoring
   - Application metrics

8. **Deployment**:
   - Containerization (Docker)
   - Orchestration (Kubernetes)
   - CI/CD pipelines

9. **Security**:
   - Service-to-service authentication
   - API security
   - OAuth2, JWT
   - Security monitoring

10. **Testing Strategy**:
    - Unit testing
    - Contract testing
    - Integration testing
    - End-to-end testing

### 52. Program to Reverse Elements in an Array

```java
public class ArrayReversal {
    
    // Reverse integer array in-place
    public static void reverseArray(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int start = 0;
        int end = arr.length - 1;
        
        while (start < end) {
            // Swap elements
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            
            // Move towards the middle
            start++;
            end--;
        }
    }
    
    // Generic method to reverse any type of array
    public static <T> void reverseArray(T[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int start = 0;
        int end = arr.length - 1;
        
        while (start < end) {
            // Swap elements
            T temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            
            // Move towards the middle
            start++;
            end--;
        }
    }
    
    // Using Java 8 Stream API (creates a new array)
    public static int[] reverseArrayStream(int[] arr) {
        return IntStream.rangeClosed(1, arr.length)
                       .map(i -> arr[arr.length - i])
                       .toArray();
    }
    
    // Using Collections.reverse() for List
    public static <T> List<T> reverseList(List<T> list) {
        List<T> reversedList = new ArrayList<>(list);
        Collections.reverse(reversedList);
        return reversedList;
    }
    
    public static void main(String[] args) {
        // Example 1: Integer array
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Original: " + Arrays.toString(numbers));
        
        reverseArray(numbers);
        System.out.println("Reversed: " + Arrays.toString(numbers));
        
        // Example 2: String array
        String[] words = {"apple", "banana", "cherry", "date"};
        System.out.println("Original: " + Arrays.toString(words));
        
        reverseArray(words);
        System.out.println("Reversed: " + Arrays.toString(words));
        
        // Example 3: Using Stream API
        int[] moreNumbers = {6, 7, 8, 9, 10};
        int[] reversedNumbers = reverseArrayStream(moreNumbers);
        System.out.println("Reversed with Stream: " + Arrays.toString(reversedNumbers));
        
        // Example 4: Using List
        List<Character> characters = Arrays.asList('a', 'b', 'c', 'd', 'e');
        List<Character> reversedChars = reverseList(characters);
        System.out.println("Reversed List: " + reversedChars);
    }
}
```

### 53. How Garbage Collector Works in Java

**Garbage Collection Process**:

1. **Object Lifecycle**:
   - Objects are created in heap memory
   - Objects become eligible for GC when they're no longer referenced
   - GC identifies and removes unreachable objects

2. **Heap Memory Structure**:
   - **Young Generation** (Eden + Survivor spaces)
   - **Old/Tenured Generation**
   - **Metaspace** (Java 8+) or **Permanent Generation** (before Java 8)

3. **GC Algorithms**:
   - **Serial GC**: Single-threaded, stop-the-world collections
   - **Parallel GC**: Multi-threaded young generation collection
   - **Concurrent Mark Sweep (CMS)**: Minimizes pause times
   - **G1 GC (Garbage First)**: Server-style collector, divides heap into regions
   - **ZGC**: Designed for low latency (Java 11+)
   - **Shenandoah**: Low-pause collector (JDK 12+)

4. **Collection Process**:
   - **Mark**: Identify live objects
   - **Sweep**: Remove dead objects
   - **Compact**: Reorganize memory (optional)

5. **Minor GC vs. Major GC**:
   - **Minor GC**: Collects young generation
   - **Major GC**: Collects tenured generation
   - **Full GC**: Collects entire heap

**GC Optimizations**:

1. **Generational Hypothesis**:
   - Most objects die young
   - Young generation is collected more frequently

2. **Memory Tuning Flags**:
   ```
   -Xms<size>  // Initial heap size
   -Xmx<size>  // Maximum heap size
   -XX:NewSize=<size>  // Young generation size
   -XX:SurvivorRatio=<ratio>  // Eden/Survivor space ratio
   ```

3. **GC Algorithm Selection**:
   ```
   -XX:+UseSerialGC  // Serial GC
   -XX:+UseParallelGC  // Parallel GC
   -XX:+UseConcMarkSweepGC  // CMS GC
   -XX:+UseG1GC  // G1 GC
   -XX:+UseZGC  // Z GC
   -XX:+UseShenandoahGC  // Shenandoah GC
   ```

4. **GC Logging**:
   ```
   -Xlog:gc*  // JDK 9+
   -XX:+PrintGCDetails -XX:+PrintGCTimeStamps  // Before JDK 9
   ```

**Best Practices**:

1. **Minimize Object Creation**:
   - Reuse objects when possible
   - Use object pools for expensive objects
   - Avoid unnecessary temporary objects

2. **Help the GC**:
   - Set object references to null when no longer needed
   - Use weak references for caches
   - Properly size collections

3. **Memory Leak Prevention**:
   - Be careful with static fields
   - Close resources properly
   - Watch for listener registration/deregistration

4. **Use Appropriate Data Structures**:
   - Choose space-efficient collections
   - Use primitive arrays when possible

### 54. SAX vs DOM Parsers

**DOM (Document Object Model) Parser**:

**Characteristics**:
- Loads entire XML document into memory
- Creates a tree structure of objects
- Allows random access to elements
- Allows navigation in all directions
- Allows document modification

**Advantages**:
- Easy to navigate and manipulate
- Can modify document
- Intuitive API for element access
- Better for smaller documents

**Disadvantages**:
- High memory usage for large documents
- Slower initial parsing
- Not suitable for very large files

**Example**:
```java
public void parseDOMExample() throws Exception {
    // Create parser
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    DocumentBuilder builder = factory.newDocumentBuilder();
    
    // Parse document
    Document document = builder.parse(new File("employees.xml"));
    
    // Normalize
    document.getDocumentElement().normalize();
    
    // Get root element
    Element root = document.getDocumentElement();
    System.out.println("Root element: " + root.getNodeName());
    
    // Get all employees
    NodeList employeeList = document.getElementsByTagName("employee");
    
    // Iterate through employees
    for (int i = 0; i < employeeList.getLength(); i++) {
        Node node = employeeList.item(i);
        
        if (node.getNodeType() == Node.ELEMENT_NODE) {
            Element element = (Element) node;
            
            String id = element.getAttribute("id");
            String name = element.getElementsByTagName("name").item(0).getTextContent();
            String department = element.getElementsByTagName("department").item(0).getTextContent();
            
            System.out.println("Employee ID: " + id);
            System.out.println("Name: " + name);
            System.out.println("Department: " + department);
        }
    }
}
```

**SAX (Simple API for XML) Parser**:

**Characteristics**:
- Event-based parser
- Processes XML sequentially
- Reads XML document and triggers events
- Does not load entire document in memory
- One-way, forward-only parsing

**Advantages**:
- Memory efficient for large documents
- Faster for large documents
- Suitable for streaming applications
- Good for search operations in large files

**Disadvantages**:
- More complex programming model
- No random access to elements
- Cannot modify document
- Cannot navigate backward

**Example**:
```java
public void parseSAXExample() throws Exception {
    // Create handler
    DefaultHandler handler = new DefaultHandler() {
        boolean inName = false;
        boolean inDepartment = false;
        String currentId = "";
        
        @Override
        public void startElement(String uri, String localName, String qName, 
                Attributes attributes) throws SAXException {
            if (qName.equalsIgnoreCase("employee")) {
                currentId = attributes.getValue("id");
                System.out.println("Employee ID: " + currentId);
            } else if (qName.equalsIgnoreCase("name")) {
                inName = true;
            } else if (qName.equalsIgnoreCase("department")) {
                inDepartment = true;
            }
        }
        
        @Override
        public void endElement(String uri, String localName, 
                String qName) throws SAXException {
            if (qName.equalsIgnoreCase("name")) {
                inName = false;
            } else if (qName.equalsIgnoreCase("department")) {
                inDepartment = false;
            }
        }
        
        @Override
        public void characters(char ch[], int start, int length) throws SAXException {
            if (inName) {
                System.out.println("Name: " + new String(ch, start, length));
            } else if (inDepartment) {
                System.out.println("Department: " + new String(ch, start, length));
            }
        }
    };
    
    // Create parser
    SAXParserFactory factory = SAXParserFactory.newInstance();
    SAXParser saxParser = factory.newSAXParser();
    
    // Parse document
    saxParser.parse(new File("employees.xml"), handler);
}
```

**Comparison Summary**:

| Feature | DOM | SAX |
|---------|-----|-----|
| Memory Usage | High (entire document) | Low (event-based) |
| Access Pattern | Random access | Sequential |
| Direction | Bi-directional | Forward only |
| Modification | Supports changes | Read-only |
| Speed | Slower for large documents | Faster for large documents |
| Ease of Use | Easier, more intuitive | More complex |
| Use Case | Smaller documents, complex navigation, modifications | Large documents, streaming, search operations |

### 55. Converting EDI/XML/CSV to JSON

**1. Using Spring Boot for Converting Files**:

```java
@Service
public class FileConversionService {
    
    // XML to JSON conversion
    public String convertXmlToJson(String xml) {
        try {
            // Using Jackson for XML to JSON conversion
            XmlMapper xmlMapper = new XmlMapper();
            JsonMapper jsonMapper = new JsonMapper();
            
            // Convert XML to JsonNode
            JsonNode node = xmlMapper.readTree(xml.getBytes());
            
            // Convert JsonNode to JSON string
            return jsonMapper.writeValueAsString(node);
        } catch (Exception e) {
            throw new RuntimeException("Error converting XML to JSON", e);
        }
    }
    
    // CSV to JSON conversion
    public String convertCsvToJson(String csv) {
        try {
            // Using Jackson CSV module
            CsvSchema csvSchema = CsvSchema.emptySchema().withHeader();
            CsvMapper csvMapper = new CsvMapper();
            
            // Convert CSV to JsonNode
            List<Object> readAll = csvMapper.readerFor(Map.class)
                .with(csvSchema)
                .readValues(csv)
                .readAll();
            
            // Convert list to JSON
            ObjectMapper jsonMapper = new ObjectMapper();
            return jsonMapper.writeValueAsString(readAll);
        } catch (Exception e) {
            throw new RuntimeException("Error converting CSV to JSON", e);
        }
    }
    
    // EDI to JSON conversion (requires additional libraries)
    public String convertEdiToJson(String edi) {
        try {
            // This is a simplified approach
            // Real-world EDI parsing usually requires specialized libraries
            // like Smooks, OpenEDI, etc.
            
            // Convert EDI to intermediate format
            Map<String, Object> ediData = parseEdi(edi);
            
            // Convert to JSON
            ObjectMapper jsonMapper = new ObjectMapper();
            return jsonMapper.writeValueAsString(ediData);
        } catch (Exception e) {
            throw new RuntimeException("Error converting EDI to JSON", e);
        }
    }
    
    // Helper method for EDI parsing (simplified)
    private Map<String, Object> parseEdi(String edi) {
        // This is a placeholder for actual EDI parsing
        // In a real application, you would use a proper EDI parser
        Map<String, Object> result = new HashMap<>();
        // Parse EDI content into the map
        // ...
        return result;
    }
}
```

**2. Dependencies for File Conversion**:

For XML to JSON:
```xml
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-xml</artifactId>
</dependency>
```

For CSV to JSON:
```xml
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-csv</artifactId>
</dependency>
```

For EDI to JSON (using Smooks):
```xml
<dependency>
    <groupId>org.smooks</groupId>
    <artifactId>smooks-all</artifactId>
    <version>1.7.1</version>
</dependency>
```

**3. Controller for File Conversion**:
```java
@RestController
@RequestMapping("/api/convert")
public class ConversionController {
    
    @Autowired
    private FileConversionService conversionService;
    
    @PostMapping("/xml-to-json")
    public ResponseEntity<String> convertXmlToJson(@RequestBody String xml) {
        String json = conversionService.convertXmlToJson(xml);
        return ResponseEntity.ok()
            .contentType(MediaType.APPLICATION_JSON)
            .body(json);
    }
    
    @PostMapping("/csv-to-json")
    public ResponseEntity<String> convertCsvToJson(@RequestBody String csv) {
        String json = conversionService.convertCsvToJson(csv);
        return ResponseEntity.ok()
            .contentType(MediaType.APPLICATION_JSON)
            .body(json);
    }
    
    @PostMapping("/edi-to-json")
    public ResponseEntity<String> convertEdiToJson(@RequestBody String edi) {
        String json = conversionService.convertEdiToJson(edi);
        return ResponseEntity.ok()
            .contentType(MediaType.APPLICATION_JSON)
            .body(json);
    }
    
    @PostMapping(value = "/file-to-json", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<String> convertFileToJson(@RequestParam("file") MultipartFile file) {
        try {
            String content = new String(file.getBytes(), StandardCharsets.UTF_8);
            String filename = file.getOriginalFilename();
            
            if (filename.endsWith(".xml")) {
                return convertXmlToJson(content);
            } else if (filename.endsWith(".csv")) {
                return convertCsvToJson(content);
            } else if (filename.endsWith(".edi")) {
                return convertEdiToJson(content);
            } else {
                return ResponseEntity.badRequest()
                    .body("Unsupported file format");
            }
        } catch (IOException e) {
            return ResponseEntity.badRequest()
                .body("Error reading file: " + e.getMessage());
        }
    }
}
```

### 56. Enabling Debug Logs in Spring Boot

**1. Using application.properties**:
```properties
# Enable debug mode
debug=true

# Set specific logging levels
logging.level.root=INFO
logging.level.org.springframework=DEBUG
logging.level.com.example.myapp=DEBUG

# Log file configuration
logging.file.name=app.log
logging.file.path=/var/logs

# Log pattern
logging.pattern.console=%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n
logging.pattern.file=%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n
```

**2. Using application.yml**:
```yml
debug: true

logging:
  level:
    root: INFO
    org.springframework: DEBUG
    com.example.myapp: DEBUG
  file:
    name: app.log
    path: /var/logs
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
```

**3. Programmatically**:
```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class MyApplication {
    
    private static final Log logger = LogFactory.getLog(MyApplication.class);
    
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
    
    @Bean
    public CommandLineRunner logLevels() {
        return args -> {
            logger.debug("This is a debug message");
            logger.info("This is an info message");
            logger.warn("This is a warning message");
            logger.error("This is an error message");
        };
    }
}
```

**4. Using logback.xml**:
```xml
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/app.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/app-%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- Application loggers -->
    <logger name="com.example.myapp" level="DEBUG" />
    
    <!-- Spring Framework loggers -->
    <logger name="org.springframework" level="DEBUG" />
    
    <!-- Root logger -->
    <root level="INFO">
        <appender-ref ref="CONSOLE" />
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

**5. Command-line arguments**:
```bash
java -jar myapp.jar --debug
```

### 57. Resolving Performance Issues in Applications

**Common Performance Issues and Solutions**:

1. **Database-Related Issues**:
   - **Problem**: Slow queries or excessive database calls
   - **Solutions**:
     - Add proper indexes
     - Use query optimization
     - Implement caching (Redis, Ehcache)
     - Use database connection pooling
     - Optimize JPA/Hibernate (batch operations, fetch strategies)
     ```java
     // Add caching
     @EnableCaching
     @Configuration
     public class CacheConfig {
         @Bean
         public CacheManager cacheManager() {
             return new ConcurrentMapCacheManager("users", "products");
         }
     }
     
     @Service
     public class UserService {
         @Cacheable(value = "users", key = "#id")
         public User findById(Long id) {
             // Database query only executed if not in cache
             return userRepository.findById(id).orElse(null);
         }
     }
     ```

2. **Memory Leaks**:
   - **Problem**: Increasing memory usage, OutOfMemoryError
   - **Solutions**:
     - Use memory profilers (JProfiler, VisualVM)
     - Check for unclosed resources
     - Review collection usage
     - Analyze JVM heap dumps
     ```java
     // Ensure resources are closed properly
     try (Connection conn = dataSource.getConnection();
          PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users");
          ResultSet rs = stmt.executeQuery()) {
         // Process results
     } catch (SQLException e) {
         log.error("Database error", e);
     }
     ```

3. **High CPU Usage**:
   - **Problem**: Application consumes too much CPU
   - **Solutions**:
     - Identify CPU-intensive operations
     - Use async processing for heavy tasks
     - Implement thread pooling
     - Consider algorithmic improvements
     ```java
     @Service
     public class ReportService {
         @Autowired
         private TaskExecutor taskExecutor;
         
         public CompletableFuture<Report> generateReportAsync(Long id) {
             return CompletableFuture.supplyAsync(() -> {
                 // CPU-intensive operation
                 return generateReport(id);
             }, taskExecutor);
         }
     }
     ```

4. **Slow API Responses**:
   - **Problem**: High latency in API calls
   - **Solutions**:
     - Enable Spring Boot Actuator for metrics
     - Use gzip compression
     - Implement response caching
     - Consider pagination for large datasets
     ```java
     // Enable compression
     server.compression.enabled=true
     server.compression.mime-types=application/json,application/xml,text/html
     server.compression.min-response-size=2048
     
     // Pagination
     @GetMapping("/users")
     public Page<User> getUsers(
             @RequestParam(defaultValue = "0") int page,
             @RequestParam(defaultValue = "20") int size) {
         return userRepository.findAll(PageRequest.of(page, size));
     }
     ```

5. **Concurrency Issues**:
   - **Problem**: Race conditions, deadlocks
   - **Solutions**:
     - Use thread-safe collections
     - Implement proper synchronization
     - Use atomic operations
     - Consider using higher-level concurrency utilities
     ```java
     // Thread-safe counter
     private final AtomicInteger counter = new AtomicInteger(0);
     
     public void increment() {
         counter.incrementAndGet();
     }
     
     // Using locks for more complex scenarios
     private final Lock lock = new ReentrantLock();
     
     public void complexOperation() {
         lock.lock();
         try {
             // Critical section
         } finally {
             lock.unlock();
         }
     }
     ```

6. **Connection Pool Exhaustion**:
   - **Problem**: Database or HTTP connection pools depleted
   - **Solutions**:
     - Increase pool size
     - Implement timeouts
     - Close connections properly
     - Monitor connection usage
     ```java
     // HikariCP configuration
     spring.datasource.hikari.maximum-pool-size=10
     spring.datasource.hikari.connection-timeout=30000
     spring.datasource.hikari.idle-timeout=600000
     spring.datasource.hikari.max-lifetime=1800000
     ```

7. **Network-Related Issues**:
   - **Problem**: Slow network calls, timeouts
   - **Solutions**:
     - Implement circuit breaker
     - Set appropriate timeouts
     - Use connection pooling
     - Consider async calls
     ```java
     // RestTemplate with timeout
     @Bean
     public RestTemplate restTemplate() {
         HttpComponentsClientHttpRequestFactory factory = new HttpComponentsClientHttpRequestFactory();
         factory.setConnectTimeout(3000);
         factory.setReadTimeout(3000);
         return new RestTemplate(factory);
     }
     ```

8. **JVM Tuning**:
   - **Problem**: Inefficient garbage collection, memory allocation
   - **Solutions**:
     - Adjust heap size (-Xms, -Xmx)
     - Select appropriate GC algorithm
     - Tune GC parameters
     - Monitor GC activity
     ```bash
     # JVM flags for GC tuning
     java -Xms2G -Xmx2G -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -jar app.jar
     ```

### 58. Making Parallel Service Calls in Spring Boot

**1. Using CompletableFuture**:
```java
@Service
public class ParallelService {
    
    @Autowired
    private RestTemplate restTemplate;
    
    @Async
    public CompletableFuture<UserData> getUserData(Long userId) {
        String url = "http://user-service/users/" + userId;
        UserData userData = restTemplate.getForObject(url, UserData.class);
        return CompletableFuture.completedFuture(userData);
    }
    
    @Async
    public CompletableFuture<OrderData> getOrderData(Long userId) {
        String url = "http://order-service/orders/user/" + userId;
        OrderData orderData = restTemplate.getForObject(url, OrderData.class);
        return CompletableFuture.completedFuture(orderData);
    }
    
    public CombinedData getCombinedData(Long userId) throws Exception {
        CompletableFuture<UserData> userFuture = getUserData(userId);
        CompletableFuture<OrderData> orderFuture = getOrderData(userId);
        
        // Wait for both futures to complete
        CompletableFuture.allOf(userFuture, orderFuture).join();
        
        // Get results
        UserData userData = userFuture.get();
        OrderData orderData = orderFuture.get();
        
        // Combine data
        return new CombinedData(userData, orderData);
    }
}
```

**2. Configuration for Async Execution**:
```java
@Configuration
@EnableAsync
public class AsyncConfig {
    
    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(25);
        executor.setThreadNamePrefix("async-");
        executor.initialize();
        return executor;
    }
}
```

**3. Using WebClient (Reactive Approach)**:
```java
@Service
public class ReactiveParallelService {
    
    private final WebClient webClient;
    
    public ReactiveParallelService(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.build();
    }
    
    public Mono<UserData> getUserData(Long userId) {
        return webClient.get()
            .uri("http://user-service/users/{id}", userId)
            .retrieve()
            .bodyToMono(UserData.class);
    }
    
    public Mono<OrderData> getOrderData(Long userId) {
        return webClient.get()
            .uri("http://order-service/orders/user/{id}", userId)
            .retrieve()
            .bodyToMono(OrderData.class);
    }
    
    public Mono<CombinedData> getCombinedData(Long userId) {
        Mono<UserData> userMono = getUserData(userId);
        Mono<OrderData> orderMono = getOrderData(userId);
        
        return Mono.zip(userMono, orderMono)
            .map(tuple -> new CombinedData(tuple.getT1(), tuple.getT2()));
    }
}
```

**4. Using ParallelFlux (for collections)**:
```java
@Service
public class ParallelFluxService {
    
    private final WebClient webClient;
    
    public ParallelFluxService(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.build();
    }
    
    public Flux<UserData> getMultipleUsers(List<Long> userIds) {
        return Flux.fromIterable(userIds)
            .parallel()
            .runOn(Schedulers.boundedElastic())
            .flatMap(this::getUserData)
            .sequential();
    }
    
    private Mono<UserData> getUserData(Long userId) {
        return webClient.get()
            .uri("http://user-service/users/{id}", userId)
            .retrieve()
            .bodyToMono(UserData.class);
    }
}
```

**5. Using Parallel Streams (Java 8+)**:
```java
@Service
public class ParallelStreamService {
    
    @Autowired
    private RestTemplate restTemplate;
    
    public List<UserData> getMultipleUsers(List<Long> userIds) {
        return userIds.parallelStream()
            .map(this::getUserData)
            .collect(Collectors.toList());
    }
    
    private UserData getUserData(Long userId) {
        String url = "http://user-service/users/" + userId;
        return restTemplate.getForObject(url, UserData.class);
    }
}
```

**6. Using CountDownLatch (low-level approach)**:
```java
@Service
public class CountDownLatchService {
    
    @Autowired
    private RestTemplate restTemplate;
    
    @Autowired
    private TaskExecutor taskExecutor;
    
    public CombinedData getCombinedData(Long userId) throws InterruptedException {
        final CountDownLatch latch = new CountDownLatch(2);
        final AtomicReference<UserData> userRef = new AtomicReference<>();
        final AtomicReference<OrderData> orderRef = new AtomicReference<>();
        
        taskExecutor.execute(() -> {
            try {
                String url = "http://user-service/users/" + userId;
                userRef.set(restTemplate.getForObject(url, UserData.class));
            } finally {
                latch.countDown();
            }
        });
        
        taskExecutor.execute(() -> {
            try {
                String url = "http://order-service/orders/user/" + userId;
                orderRef.set(restTemplate.getForObject(url, OrderData.class));
            } finally {
                latch.countDown();
            }
        });
        
        // Wait for both tasks to complete
        latch.await();
        
        return new CombinedData(userRef.get(), orderRef.get());
    }
}
```

## Core Java Additional Questions

### 1. How HashMap is Implemented

**Core Concepts**:
1. **Data Structure**: Array of linked lists (or trees in Java 8+)
2. **Hash Function**: Uses `hashCode()` of the key
3. **Index Calculation**: `index = hash(key) & (capacity - 1)`
4. **Collision Handling**: Separate chaining with linked lists/trees

**Implementation Details**:
- Default initial capacity: 16
- Default load factor: 0.75
- Rehashing occurs when size > capacity * load factor
- Uses linked lists for buckets with few entries
- Converts to balanced tree when bucket size > 8 (Java 8+)
- Converts back to linked list when bucket size < 6

**Key Operations**:
```java
// Put operation (simplified)
public V put(K key, V value) {
    if (key == null) {
        return putForNullKey(value);
    }
    int hash = hash(key.hashCode());
    int i = indexFor(hash, table.length);
    for (Entry<K,V> e = table[i]; e != null; e = e.next) {
        if (e.hash == hash && (key == e.key || key.equals(e.key))) {
            V oldValue = e.value;
            e.value = value;
            return oldValue;
        }
    }
    addEntry(hash, key, value, i);
    return null;
}

// Get operation (simplified)
public V get(Object key) {
    if (key == null) {
        return getForNullKey();
    }
    int hash = hash(key.hashCode());
    for (Entry<K,V> e = table[indexFor(hash, table.length)];
         e != null;
         e = e.next) {
        Object k = e.key;
        if (e.hash == hash && (key == k || key.equals(k))) {
            return e.value;
        }
    }
    return null;
}
```

### 2. Relationship Between hashCode() and equals()

**Contract**:
1. If two objects are equal according to `equals()`, they MUST have the same `hashCode()` value
2. If two objects have the same `hashCode()`, they are NOT required to be equal according to `equals()`
3. Consistently equal objects must consistently return the same `hashCode()` value

**Implementation Rules**:
- Always override `hashCode()` when overriding `equals()`
- Use the same fields in both methods for consistency
- If `equals()` uses mutable fields, `hashCode()` will change when those fields change

**Proper Implementation Example**:
```java
public class Person {
    private final String firstName;
    private final String lastName;
    private final int age;
    
    // Constructor and getters
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age &&
               Objects.equals(firstName, person.firstName) &&
               Objects.equals(lastName, person.lastName);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(firstName, lastName, age);
    }
}
```

**Consequences of Violation**:
- If `equals()` is overridden without `hashCode()`: Objects may be equal but have different hash codes
- This causes problems with hash-based collections (HashMap, HashSet)
- Equal objects might be stored in different buckets
- `contains()` may return false even if an equal object exists in the collection

### 3. Immutable Class and Immutable Object

**Immutable Class**: A class whose instances cannot be modified after creation.

**Rules for Creating Immutable Classes**:
1. Make the class final (prevents inheritance)
2. Make all fields private and final
3. No setter methods
4. Return defensive copies of mutable fields in getter methods
5. Perform defensive copies of mutable parameters in constructors

**Example of Immutable Class**:
```java
public final class ImmutablePerson {
    private final String name;
    private final int age;
    private final Date birthDate;
    private final List<String> hobbies;
    
    public ImmutablePerson(String name, int age, Date birthDate, List<String> hobbies) {
        this.name = name;
        this.age = age;
        // Defensive copy of mutable objects
        this.birthDate = birthDate != null ? new Date(birthDate.getTime()) : null;
        this.hobbies = new ArrayList<>(hobbies);
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public Date getBirthDate() {
        // Return defensive copy
        return birthDate != null ? new Date(birthDate.getTime()) : null;
    }
    
    public List<String> getHobbies() {
        // Return defensive copy
        return new ArrayList<>(hobbies);
    }
}
```

**Benefits of Immutability**:
1. Thread-safety without synchronization
2. Simplifies concurrent programming
3. Object state won't change unexpectedly
4. Safe for use as keys in maps or elements in sets
5. Cacheable and hashable

**Immutable Objects in Java Standard Library**:
- String
- Integer, Long, Double, etc.
- LocalDate, LocalTime (Java 8+)
- BigInteger, BigDecimal

### 4. Serialization and Transient Modifier

**Serialization**: Process of converting an object into a byte stream for storage or transmission.

**How to Achieve Serialization**:
1. Implement `Serializable` interface
2. Use `ObjectOutputStream` to write the object
3. Use `ObjectInputStream` to read the object

```java
// Serializable class
public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String name;
    private int age;
    private transient String password; // Will not be serialized
    
    // Constructor, getters, setters
}

// Serialization
try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("employee.ser"))) {
    Employee emp = new Employee("John", 30, "secret123");
    out.writeObject(emp);
}

// Deserialization
try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("employee.ser"))) {
    Employee emp = (Employee) in.readObject();
}
```

**Transient Modifier**:
- Marks fields that should be excluded from serialization
- Used for:
  - Security-sensitive data (passwords, keys)
  - Non-serializable fields
  - Redundant or derivable fields
  - Connection objects

**Relationship to Serialization**:
- Transient fields are not written to the byte stream during serialization
- During deserialization, transient fields receive default values (null for objects, 0 for numbers, etc.)
- Can be used to handle non-serializable fields in an otherwise serializable class

**Additional Serialization Considerations**:
1. `serialVersionUID`: Controls version compatibility
2. `readObject()` and `writeObject()`: Custom serialization
3. `readResolve()`: Control instance creation during deserialization
4. `writeReplace()`: Replace object during serialization

```java
public class CustomSerialization implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient List<String> derivedData;
    
    // Custom serialization
    private void writeObject(ObjectOutputStream out) throws IOException {
        out.defaultWriteObject(); // Write non-transient fields
        // Write any additional data
        out.writeInt(derivedData.size());
    }
    
    private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
        in.defaultReadObject(); // Read non-transient fields
        // Read additional data
        int size = in.readInt();
        derivedData = new ArrayList<>(size);
        // Reconstruct transient fields
    }
}
```

### 5. Cloning: Deep vs. Shallow

**Cloning**: Creating a copy of an object.

**Shallow Clone**:
- Creates a new object
- Copies primitive field values
- Copies references to mutable objects (not the objects themselves)
- Implementation via `Cloneable` interface and `clone()` method

```java
public class Employee implements Cloneable {
    private String name;
    private Department department; // Reference type
    
    @Override
    public Employee clone() throws CloneNotSupportedException {
        return (Employee) super.clone(); // Shallow copy
    }
}
```

**Deep Clone**:
- Creates a new object
- Copies primitive field values
- Creates new copies of mutable objects (recursively)
- Requires custom implementation

```java
public class Employee implements Cloneable {
    private String name;
    private Department department; // Reference type
    
    @Override
    public Employee clone() throws CloneNotSupportedException {
        Employee cloned = (Employee) super.clone();
        // Deep copy: create new Department object
        cloned.department = department.clone();
        return cloned;
    }
}
```

**Alternative Deep Cloning Methods**:
1. **Serialization**:
```java
public static <T> T deepClone(T obj) throws Exception {
    ByteArrayOutputStream bos = new ByteArrayOutputStream();
    ObjectOutputStream out = new ObjectOutputStream(bos);
    out.writeObject(obj);
    
    ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
    ObjectInputStream in = new ObjectInputStream(bis);
    return (T) in.readObject();
}
```

2. **Copy Constructor**:
```java
public class Employee {
    private String name;
    private Department department;
    
    // Copy constructor for deep cloning
    public Employee(Employee source) {
        this.name = source.name;
        this.department = new Department(source.department);
    }
}
```

**Comparison**:

| Aspect | Shallow Clone | Deep Clone |
|--------|---------------|------------|
| Object References | Shared | Independent copies |
| Implementation | Easy (via `super.clone()`) | Complex (custom implementation) |
| Mutability Concerns | Changes to nested objects affect both copies | Objects are completely independent |
| Performance | Faster | Slower, more memory intensive |
| Use Case | Simple objects with primitives or immutable fields | Objects with mutable nested references |

### 6. Heap vs. Stack Memory

**Stack Memory**:
- Stores local variables and method call information
- LIFO (Last In, First Out) structure
- Thread-specific (each thread has its own stack)
- Fixed size (can cause StackOverflowError)
- Automatic allocation/deallocation
- Faster access
- Stores:
  - Primitive values
  - References to objects
  - Method frames

**Heap Memory**:
- Stores objects and arrays
- Shared across all threads
- Dynamic size
- Managed by Garbage Collector
- Can cause OutOfMemoryError
- Slower access than stack
- Stores:
  - Object data
  - Instance variables
  - Arrays
  - Static variables

**Example**:
```java
public void exampleMethod() {
    int stackVar = 5;  // Stored in stack
    Person person = new Person("John");  // 'person' reference in stack, Person object in heap
    
    // When method completes, stackVar and person reference are removed from stack
    // Person object remains in heap until garbage collected
}
```

**Memory Implications**:
1. Method recursion affects stack, not heap
2. Object creation affects heap, reference affects stack
3. Thread creation allocates new stack, shares heap
4. Long-lived objects stay in heap, can cause memory leaks

### 7. Factory Pattern and Polymorphism

**Factory Pattern**: Creational pattern that uses factory methods to create objects without specifying the exact class.

**Key Components**:
1. **Factory**: Class with method(s) to create and return objects
2. **Product Interface/Abstract Class**: Common type for created objects
3. **Concrete Products**: Implementations of the interface/abstract class

**Implementation**:
```java
// Product interface (common type)
public interface Vehicle {
    void drive();
}

// Concrete products
public class Car implements Vehicle {
    @Override
    public void drive() {
        System.out.println("Driving a car");
    }
}

public class Truck implements Vehicle {
    @Override
    public void drive() {
        System.out.println("Driving a truck");
    }
}

// Factory
public class VehicleFactory {
    public static Vehicle createVehicle(String type) {
        if ("car".equalsIgnoreCase(type)) {
            return new Car();
        } else if ("truck".equalsIgnoreCase(type)) {
            return new Truck();
        }
        throw new IllegalArgumentException("Unknown vehicle type: " + type);
    }
}

// Client code
Vehicle vehicle = VehicleFactory.createVehicle("car");
vehicle.drive(); // Polymorphic call
```

**Relationship to Polymorphism**:
- Factory pattern leverages polymorphism by returning different object types that share a common interface
- Client code works with abstract type (interface/superclass)
- Runtime polymorphism determines which concrete implementation is used
- Factory decouples object creation from usage
- Enables "programming to an interface, not an implementation"

**Benefits**:
1. Encapsulates object creation logic
2. Allows adding new types without changing client code
3. Promotes loose coupling
4. Simplifies complex creation logic

**Factory Pattern Variations**:
1. **Simple Factory**: Single factory method creating objects (example above)
2. **Factory Method**: Subclasses decide which class to instantiate
3. **Abstract Factory**: Creates families of related objects

### 8. Preferable Datatype for Map Keys

**Ideal Characteristics for Map Keys**:
1. **Immutable**: Should not change after insertion
2. **Proper hashCode() implementation**: Consistent and well-distributed
3. **Proper equals() implementation**: Reflects logical equality
4. **Serializable**: If the Map needs to be serialized

**Best Key Types**:

1. **String**:
   - Immutable
   - Well-implemented hashCode() and equals()
   - Most common key type
   ```java
   Map<String, Value> map = new HashMap<>();
   map.put("key1", value1);
   ```

2. **Primitive Wrappers** (Integer, Long, etc.):
   - Immutable
   - Well-implemented hashCode() and equals()
   - Autoboxing makes them convenient
   ```java
   Map<Integer, Value> map = new HashMap<>();
   map.put(1, value1);
   ```

3. **Enum**:
   - Immutable
   - Perfect hashCode() (based on ordinal)
   - Type-safe
   - Limited set of possible values
   ```java
   enum Day { MONDAY, TUESDAY, WEDNESDAY /* etc */ }
   Map<Day, Value> map = new EnumMap<>(Day.class); // EnumMap for efficiency
   map.put(Day.MONDAY, value1);
   ```

4. **Custom Immutable Classes**:
   - Must override equals() and hashCode() properly
   - All fields should be final
   ```java
   public final class CompositeKey {
       private final String part1;
       private final int part2;
       
       // Constructor
       
       @Override
       public boolean equals(Object o) {
           // Proper implementation
       }
       
       @Override
       public int hashCode() {
           return Objects.hash(part1, part2);
       }
   }
   
   Map<CompositeKey, Value> map = new HashMap<>();
   ```

**Types to Avoid as Keys**:

1. **Mutable Objects**:
   - Arrays (their hashCode changes based on content)
   - ArrayList, HashMap, and other mutable collections
   - Custom mutable classes
   
2. **Objects with Poor hashCode() Distribution**:
   - Objects that frequently produce the same hash code
   - Can degrade HashMap to O(n) performance

3. **Large Objects**:
   - Complex objects that are expensive to compute hashCode()
   - Consider using an ID or smaller representation

**Special Case: Using Objects as Keys**:
```java
// If using a mutable object as key (not recommended)
public class MutableKey {
    private String value;
    
    // Constructor, getters, setters
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        MutableKey that = (MutableKey) o;
        return Objects.equals(value, that.value);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(value);
    }
}

// DANGER: If you modify the key after insertion, you may not be able to retrieve the value
MutableKey key = new MutableKey("original");
map.put(key, "value");
key.setValue("modified"); // Now the key's hash has changed
String value = map.get(key); // Will likely return null!
```

### 9. Iterating and Updating Collections Simultaneously

**Problem**: Modifying a collection while iterating often causes `ConcurrentModificationException`.

**Incorrect Approach**:
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
for (String item : list) {
    if ("B".equals(item)) {
        list.remove(item); // Will throw ConcurrentModificationException
    }
}
```

**Safe Approaches**:

1. **Using Iterator's remove() method**:
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String item = iterator.next();
    if ("B".equals(item)) {
        iterator.remove(); // Safe way to remove current element
    }
}
```

2. **Using removeIf() (Java 8+)**:
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
list.removeIf(item -> "B".equals(item)); // Internally handles iteration and removal
```

3. **Using CopyOnWriteArrayList**:
```java
List<String> list = new CopyOnWriteArrayList<>(Arrays.asList("A", "B", "C", "D"));
for (String item : list) {
    if ("B".equals(item)) {
        list.remove(item); // Safe but creates a new array copy each time
    }
}
```

4. **Using a temporary collection for removal**:
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
List<String> toRemove = new ArrayList<>();

for (String item : list) {
    if ("B".equals(item)) {
        toRemove.add(item);
    }
}

list.removeAll(toRemove); // Remove after iteration is complete
```

5. **Iterating backward with for-loop** (for List only):
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
for (int i = list.size() - 1; i >= 0; i--) {
    if ("B".equals(list.get(i))) {
        list.remove(i); // Safe since we're going backward
    }
}
```

6. **Creating a defensive copy**:
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
List<String> copy = new ArrayList<>(list);

for (String item : copy) {
    if ("B".equals(item)) {
        list.remove(item); // Modifying original but iterating through copy
    }
}
```

**Collection-Specific Notes**:

1. **ArrayList**: Use Iterator.remove() or removeIf()
2. **LinkedList**: Iterator.remove() is efficient
3. **HashSet/HashMap**: Must use Iterator.remove() or removeIf()
4. **ConcurrentHashMap**: Allows concurrent modification
5. **CopyOnWriteArrayList/Set**: Designed for concurrent iteration and modification

### 10. Functional Interface and Lambda Expression

**Functional Interface**: An interface with exactly one abstract method.

**Characteristics**:
- Can have default and static methods
- Has exactly one abstract method
- Can be annotated with `@FunctionalInterface`

**Standard Functional Interfaces** (java.util.function):
1. **Predicate<T>**: Takes T, returns boolean
2. **Consumer<T>**: Takes T, returns void
3. **Function<T,R>**: Takes T, returns R
4. **Supplier<T>**: Takes nothing, returns T
5. **UnaryOperator<T>**: Takes T, returns T
6. **BinaryOperator<T>**: Takes two T, returns T

**Example Functional Interfaces**:
```java
@FunctionalInterface
public interface Calculator {
    int calculate(int a, int b);
    
    // Can have default methods
    default void printInfo() {
        System.out.println("Calculator interface");
    }
    
    // Can have static methods
    static Calculator add() {
        return (a, b) -> a + b;
    }
}

// Runnable is a built-in functional interface
@FunctionalInterface
public interface Runnable {
    void run();
}
```

**Lambda Expressions**: Compact representation of anonymous functions that can be passed around.

**Lambda Syntax**:
```java
// Basic syntax: (parameters) -> expression
// Or: (parameters) -> { statements; }

// No parameters
Runnable r = () -> System.out.println("Hello");

// One parameter (parentheses optional)
Consumer<String> c = s -> System.out.println(s);

// Multiple parameters
Calculator calc = (a, b) -> a + b;

// Block with multiple statements
Calculator complexCalc = (a, b) -> {
    int result = a * b;
    result += a + b;
    return result;
};
```

**Common Lambda Uses**:

1. **Collection Operations**:
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// Filtering
List<String> filtered = names.stream()
    .filter(name -> name.startsWith("A"))
    .collect(Collectors.toList());

// Mapping
List<Integer> lengths = names.stream()
    .map(String::length)
    .collect(Collectors.toList());

// Sorting
names.sort((a, b) -> a.compareTo(b));
```

2. **Event Handling**:
```java
button.addActionListener(e -> System.out.println("Button clicked"));
```

3. **Concurrent Execution**:
```java
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.submit(() -> {
    System.out.println("Task executed on thread: " + Thread.currentThread().getName());
});
```

4. **Optional Handling**:
```java
Optional<String> optional = Optional.of("value");
optional.ifPresent(val -> System.out.println("Value: " + val));
```

5. **Creating Functional Interface Instances**:
```java
Comparator<String> comparator = (s1, s2) -> s1.length() - s2.length();
```

**Method References**:

Method references are shorthand for certain lambda expressions:
```java
// Static method reference
Consumer<String> printer = System.out::println;

// Instance method reference
String str = "Hello";
Supplier<Integer> lengthSupplier = str::length;

// Constructor reference
Supplier<List<String>> listSupplier = ArrayList::new;
```

### 11. Pass-by-Reference vs. Pass-by-Value

**In Java, everything is pass-by-value.**

**For Primitive Types**:
- The actual value is copied and passed to methods
- Changes to the parameter inside the method don't affect the original variable

```java
public void modifyValue(int x) {
    x = 10; // Only modifies local copy
}

int num = 5;
modifyValue(num);
System.out.println(num); // Still 5
```

**For Reference Types**:
- The value of the reference (memory address) is copied
- Not the actual object itself
- Can modify the object's state but can't change which object is referenced

```java
public void modifyObject(Person person) {
    person.setName("Jane"); // Modifies the referenced object
    person = new Person("Bob"); // Only changes local reference
}

Person p = new Person("John");
modifyObject(p);
System.out.println(p.getName()); // "Jane" - object was modified
```

**Visual Explanation**:
```
Pass-by-value for primitives:
Original variable: [5]
↓ copy value
Method parameter: [5] (separate memory location)

Pass-by-value for references:
Original variable: [reference to → Person("John")]
↓ copy reference value
Method parameter: [reference to → Person("John")] (same memory location)
```

**Common Misconception**:
- Many think Java uses pass-by-reference for objects
- The confusion arises because you can modify object state
- But you cannot reassign the original reference

**Example Demonstrating the Difference**:
```java
public class PassingExample {
    
    // Inner class
    static class Holder {
        public int value;
        public Holder(int value) { this.value = value; }
    }
    
    public static void main(String[] args) {
        // Primitive example
        int primitive = 5;
        modifyPrimitive(primitive);
        System.out.println("Primitive: " + primitive); // 5 - unchanged
        
        // Object example 1 - modify state
        Holder holder1 = new Holder(5);
        modifyHolderValue(holder1);
        System.out.println("Holder1 value: " + holder1.value); // 10 - changed
        
        // Object example 2 - reassign reference
        Holder holder2 = new Holder(5);
        modifyHolderReference(holder2);
        System.out.println("Holder2 value: " + holder2.value); // 5 - unchanged
    }
    
    static void modifyPrimitive(int value) {
        value = 10; // Only changes local copy
    }
    
    static void modifyHolderValue(Holder holder) {
        holder.value = 10; // Modifies the object state
    }
    
    static void modifyHolderReference(Holder holder) {
        holder = new Holder(10); // Only changes local reference
    }
}
```

**If Java Had Pass-by-Reference**:
```java
// Hypothetical pass-by-reference (not valid Java)
static void hypotheticalPassByReference(int &value) {
    value = 10; // Would change the original variable
}

int num = 5;
hypotheticalPassByReference(num);
System.out.println(num); // Would be 10 if Java had pass-by-reference
```

### 12. Exception Types and Custom Exceptions

**Exception Types in Java**:

1. **Checked Exceptions**:
   - Subclasses of Exception (excluding RuntimeException)
   - Must be either caught or declared in method signature
   - Represent recoverable conditions
   - Examples: IOException, SQLException, ClassNotFoundException

2. **Unchecked Exceptions (Runtime Exceptions)**:
   - Subclasses of RuntimeException
   - Don't need to be caught or declared
   - Represent programming errors
   - Examples: NullPointerException, ArrayIndexOutOfBoundsException, IllegalArgumentException

3. **Errors**:
   - Subclasses of Error
   - Represent unrecoverable conditions
   - Not meant to be caught or handled
   - Examples: OutOfMemoryError, StackOverflowError, VirtualMachineError

**Exception Hierarchy**:
```
Throwable
├── Error
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── ...
└── Exception
    ├── IOException
    ├── SQLException
    ├── ClassNotFoundException
    ├── ...
    └── RuntimeException
        ├── NullPointerException
        ├── IllegalArgumentException
        ├── ArithmeticException
        └── ...
```

**Creating Custom Exceptions**:

1. **Custom Checked Exception**:
```java
public class InsufficientFundsException extends Exception {
    private final double amount;
    
    public InsufficientFundsException(String message, double amount) {
        super(message);
        this.amount = amount;
    }
    
    public double getAmount() {
        return amount;
    }
}

// Usage:
public void withdraw(double amount) throws InsufficientFundsException {
    if (balance < amount) {
        throw new InsufficientFundsException(
            "Insufficient funds. Need $" + (amount - balance) + " more.", amount);
    }
    balance -= amount;
}
```

2. **Custom Unchecked Exception**:
```java
public class UserNotFoundException extends RuntimeException {
    private final String userId;
    
    public UserNotFoundException(String message, String userId) {
        super(message);
        this.userId = userId;
    }
    
    public String getUserId() {
        return userId;
    }
}

// Usage:
public User findUser(String userId) {
    User user = userRepository.findById(userId);
    if (user == null) {
        throw new UserNotFoundException("User not found with ID: " + userId, userId);
    }
    return user;
}
```

**Best Practices for Custom Exceptions**:

1. **Choose Checked vs. Unchecked Appropriately**:
   - Use checked exceptions for recoverable conditions
   - Use unchecked exceptions for programming errors

2. **Provide Constructors**:
   - Default constructor
   - Constructor with message
   - Constructor with message and cause
   - Constructor with additional data

3. **Add Useful Context**:
   - Include relevant information in the exception
   - Provide getters for additional data

4. **Follow Naming Conventions**:
   - End class name with "Exception"
   - Name should describe the error condition

5. **Consider Exception Chaining**:
   - Preserve original cause with initCause() or cause constructor

6. **Exception Pattern Examples**:
```java
// Complete Custom Exception
public class CustomException extends Exception {
    private final String errorCode;
    
    // Default constructor
    public CustomException() {
        super();
        this.errorCode = "UNKNOWN";
    }
    
    // Constructor with message
    public CustomException(String message) {
        super(message);
        this.errorCode = "UNKNOWN";
    }
    
    // Constructor with message and cause
    public CustomException(String message, Throwable cause) {
        super(message, cause);
        this.errorCode = "UNKNOWN";
    }
    
    // Constructor with message and additional data
    public CustomException(String message, String errorCode) {
        super(message);
        this.errorCode = errorCode;
    }
    
    // Constructor with all data
    public CustomException(String message, Throwable cause, String errorCode) {
        super(message, cause);
        this.errorCode = errorCode;
    }
    
    public String getErrorCode() {
        return errorCode;
    }
}
```

## Spring Framework Additional Questions

### 1. Auto-wiring in Spring

**Auto-wiring**: Spring's mechanism for automatically resolving dependencies between beans.

**Ways to Implement Auto-wiring**:

1. **@Autowired Annotation**:
```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    
    // Constructor, methods, etc.
}
```

2. **Constructor Injection**:
```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    // Methods, etc.
}
```

3. **Setter Injection**:
```java
@Service
public class UserService {
    private UserRepository userRepository;
    
    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    // Constructor, methods, etc.
}
```

4. **Field Injection with @Resource** (Java EE annotation):
```java
@Service
public class UserService {
    @Resource
    private UserRepository userRepository;
    
    // Constructor, methods, etc.
}
```

5. **XML Configuration**:
```xml
<bean id="userService" class="com.example.service.UserServiceImpl" autowire="byType">
    <!-- Properties defined here -->
</bean>
```

**Auto-wiring by Type vs. by Name**:
- **byType**: Default mode, matches by type
- **byName**: Matches beans by property name

**@Qualifier Annotation** (for disambiguation):
```java
@Service
public class UserService {
    @Autowired
    @Qualifier("jpaUserRepository")
    private UserRepository userRepository;
    
    // Constructor, methods, etc.
}
```

**@Primary Annotation** (for preferred beans):
```java
@Repository
@Primary
public class JpaUserRepository implements UserRepository {
    // Implementation
}
```

### 2. Constructor Injection vs. Setter Injection

**Constructor Injection**:
```java
@Service
public class UserService {
    private final UserRepository userRepository;
    private final EmailService emailService;
    
    @Autowired
    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }
    
    // Methods
}
```

**Setter Injection**:
```java
@Service
public class UserService {
    private UserRepository userRepository;
    private EmailService emailService;
    
    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Autowired
    public void setEmailService(EmailService emailService) {
        this.emailService = emailService;
    }
    
    // Constructor, methods, etc.
}
```

**Comparison**:

| Aspect | Constructor Injection | Setter Injection |
|--------|----------------------|------------------|
| Object State | Immutable | Mutable |
| Mandatory Dependencies | Enforced | Optional |
| Circular Dependencies | Not supported | Supported |
| Code Clarity | Dependencies clearly identified | Dependencies may be scattered |
| Testability | Better for mock injection | Easier for optional dependencies |
| Object Creation | All dependencies at once | Dependencies can be added later |

**Which to Prefer**:
- **Constructor Injection** (generally preferred):
  - For mandatory dependencies
  - For immutable objects
  - For clearer dependency identification
  - For better testability

- **Setter Injection**:
  - For optional dependencies
  - When circular dependencies exist
  - For reconfigurable dependencies
  - For complex inheritance scenarios

**Spring's Recommendation**: Constructor injection for required dependencies, setter injection for optional dependencies.

### 3. Aspect Oriented Programming in Spring

**Aspect-Oriented Programming (AOP)**: Programming paradigm that increases modularity by allowing separation of cross-cutting concerns.

**Key Concepts**:
- **Aspect**: Module encapsulating cross-cutting concern
- **Join Point**: Point in program execution (method execution, exception handling, etc.)
- **Advice**: Action taken at a join point
- **Pointcut**: Expression that matches join points
- **Introduction**: Declaring additional methods/fields on behalf of a type
- **Target Object**: Object being advised
- **Weaving**: Process of linking aspects with objects

**Types of Advice**:
1. **Before**: Runs before the join point
2. **After**: Runs after the join point (regardless of outcome)
3. **After-returning**: Runs after successful completion
4. **After-throwing**: Runs if method throws exception
5. **Around**: Surrounds join point execution, can control if/how it executes

**AOP Implementation in Spring**:

1. **Enable AOP**:
```java
@Configuration
@EnableAspectJAutoProxy
public class AppConfig {
    // Configuration
}
```

2. **Create an Aspect**:
```java
@Aspect
@Component
public class LoggingAspect {
    
    // Pointcut definition
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}
    
    // Before advice
    @Before("serviceMethods()")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println("Before executing: " + joinPoint.getSignature().getName());
    }
    
    // After advice
    @After("serviceMethods()")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("After executing: " + joinPoint.getSignature().getName());
    }
    
    // AfterReturning advice
    @AfterReturning(pointcut = "serviceMethods()", returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        System.out.println("Returned value: " + result);
    }
    
    // AfterThrowing advice
    @AfterThrowing(pointcut = "serviceMethods()", throwing = "error")
    public void logAfterThrowing(JoinPoint joinPoint, Throwable error) {
        System.out.println("Exception: " + error.getMessage());
    }
    
    // Around advice
    @Around("serviceMethods()")
    public Object logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        
        try {
            Object result = joinPoint.proceed();
            long executionTime = System.currentTimeMillis() - start;
            
            System.out.println(joinPoint.getSignature() + " executed in " + executionTime + "ms");
            return result;
        } catch (Exception e) {
            System.out.println("Exception in " + joinPoint.getSignature());
            throw e;
        }
    }
}
```

**Common AOP Use Cases**:
1. **Logging**: Track method calls and execution times
2. **Security**: Authorization checks before method execution
3. **Transactions**: Begin/commit/rollback around methods
4. **Caching**: Cache method results
5. **Exception Handling**: Centralized exception handling
6. **Performance Monitoring**: Track execution times
7. **Retry Logic**: Retry failed operations

**Pointcut Expression Examples**:
```java
// All methods in service package
@Pointcut("execution(* com.example.service.*.*(..))")

// All methods with @Transactional annotation
@Pointcut("@annotation(org.springframework.transaction.annotation.Transactional)")

// All methods in classes with @Service annotation
@Pointcut("within(@org.springframework.stereotype.Service *)")

// Methods with specific parameter types
@Pointcut("execution(* *(com.example.model.User))")

// Combining pointcuts
@Pointcut("serviceMethods() && @annotation(org.springframework.transaction.annotation.Transactional)")
```

### 4. Spring Annotations

**Core Annotations**:

1. **Component Annotations**:
   - `@Component`: Generic Spring-managed component
   - `@Service`: Business service layer
   - `@Repository`: Data access layer
   - `@Controller`: Web controller
   - `@RestController`: REST API controller

2. **Configuration Annotations**:
   - `@Configuration`: Class with bean definitions
   - `@Bean`: Method-level annotation for creating beans
   - `@ComponentScan`: Auto-detect Spring components
   - `@PropertySource`: Load properties files
   - `@Import`: Import other configuration classes

3. **Dependency Injection**:
   - `@Autowired`: Inject dependencies
   - `@Qualifier`: Specify which bean to inject
   - `@Value`: Inject property values
   - `@Resource`: Java EE resource injection
   - `@Inject`: Java EE standard injection

4. **Spring MVC**:
   - `@RequestMapping`: Map web requests
   - `@GetMapping`, `@PostMapping`, etc.: HTTP method-specific mapping
   - `@RequestParam`: Extract query parameters
   - `@PathVariable`: Extract URI template variables
   - `@RequestBody`: Parse request body
   - `@ResponseBody`: Serialize return value to response
   - `@ResponseStatus`: Set HTTP status code

5. **Spring Boot**:
   - `@SpringBootApplication`: Enable auto-config, component scan
   - `@EnableAutoConfiguration`: Enable auto-configuration
   - `@ConfigurationProperties`: Bind properties to POJO
   - `@Profile`: Activate beans for specific profiles
   - `@ConditionalOn...`: Conditional bean creation

6. **Data & Transactions**:
   - `@Transactional`: Declare transactional boundaries
   - `@Query`: Custom JPQL/SQL queries
   - `@Repository`: Exception translation for data access
   - `@Entity`, `@Table`, `@Column`: JPA annotations
   - `@Id`, `@GeneratedValue`: Define primary keys

7. **Aspect-Oriented Programming**:
   - `@Aspect`: Declare aspect class
   - `@Pointcut`: Define pointcut expressions
   - `@Before`, `@After`, `@Around`: Define advice
   - `@EnableAspectJAutoProxy`: Enable AOP

8. **Testing**:
   - `@SpringBootTest`: Integration test with Spring Boot
   - `@WebMvcTest`: Test MVC controllers
   - `@DataJpaTest`: Test JPA repositories
   - `@MockBean`: Create and inject mock
   - `@SpyBean`: Create and inject spy
   - `@ActiveProfiles`: Set active profiles for test

**Examples**:

```java
// Component annotation with qualifier
@Service("userService")
public class UserServiceImpl implements UserService {
    // Implementation
}

// Configuration class
@Configuration
@ComponentScan("com.example")
public class AppConfig {
    
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}

// Controller with request mapping
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        // Implementation
    }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public User createUser(@Valid @RequestBody User user) {
        // Implementation
    }
}

// Property value injection
@Component
public class AppProperties {
    
    @Value("${app.name}")
    private String appName;
    
    @Value("${app.description:Default description}")
    private String description;
    
    @Value("${app.servers}")
    private List<String> servers;
    
    // Getters
}

// Configuration properties binding
@Configuration
@ConfigurationProperties(prefix = "mail")
public class MailProperties {
    
    private String host;
    private int port;
    private String username;
    private String password;
    
    // Getters and setters
}
```

### 5. @SpringBootApplication, @Configuration, @ComponentScan

**@SpringBootApplication**:
- Convenience annotation that combines:
  - `@Configuration`
  - `@EnableAutoConfiguration`
  - `@ComponentScan`
- Entry point for Spring Boot applications
- Enables auto-configuration and component scanning

```java
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**@Configuration**:
- Indicates that a class contains Spring bean definitions
- Alternative to XML configuration
- Methods annotated with `@Bean` provide bean definitions
- Processed during application context initialization

```java
@Configuration
public class AppConfig {
    
    @Bean
    public UserService userService() {
        return new UserServiceImpl();
    }
    
    @Bean
    public EmailService emailService() {
        return new EmailServiceImpl();
    }
}
```

**@ComponentScan**:
- Enables component scanning in specified packages
- Automatically detects and registers Spring beans
- Scans for classes annotated with `@Component`, `@Service`, `@Repository`, `@Controller`, etc.
- Default scope is the package of the annotated class

```java
// Basic usage - scans current package and sub-packages
@ComponentScan
public class AppConfig { /* ... */ }

// Specify base packages
@ComponentScan(basePackages = {"com.example.service", "com.example.repository"})
public class AppConfig { /* ... */ }

// Use marker classes to define scan packages
@ComponentScan(basePackageClasses = {ServiceMarker.class, RepositoryMarker.class})
public class AppConfig { /* ... */ }

// Include/exclude filters
@ComponentScan(
    includeFilters = @Filter(type = FilterType.REGEX, pattern = ".*Service"),
    excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = Deprecated.class)
)
public class AppConfig { /* ... */ }
```

**Relationship Between These Annotations**:
- `@SpringBootApplication` is a convenience annotation that includes the functionality of `@Configuration` and `@ComponentScan`
- `@Configuration` defines the class as a source of bean definitions
- `@ComponentScan` enables auto-detection of components
- Together, they define how the Spring application context is configured and populated

### 6. Spring Boot vs. Spring MVC

**Spring MVC** (Model-View-Controller):
- Web framework for building web applications
- Part of core Spring Framework
- Follows MVC design pattern
- Requires explicit configuration for many components
- Needs external web server (Tomcat, Jetty, etc.)

**Spring Boot**:
- Opinionated framework for creating stand-alone applications
- Built on top of Spring Framework (including Spring MVC)
- Aims to simplify development with convention over configuration
- Provides auto-configuration
- Includes embedded web server
- Offers production-ready features out of the box

**Key Differences**:

1. **Configuration**:
   - **Spring MVC**: Requires explicit XML or Java configuration
   - **Spring Boot**: Provides auto-configuration based on classpath

   ```java
   // Spring MVC Configuration
   @Configuration
   @EnableWebMvc
   public class WebConfig implements WebMvcConfigurer {
       @Override
       public void configureViewResolvers(ViewResolverRegistry registry) {
           registry.jsp("/WEB-INF/views/", ".jsp");
       }
       
       // More configuration...
   }
   
   // Spring Boot - No explicit configuration needed
   @SpringBootApplication
   public class Application {
       public static void main(String[] args) {
           SpringApplication.run(Application.class, args);
       }
   }
   ```

2. **Deployment**:
   - **Spring MVC**: Requires WAR packaging and external servlet container
   - **Spring Boot**: Supports standalone JAR with embedded server or traditional WAR

   ```java
   // Spring Boot standalone application
   @SpringBootApplication
   public class Application {
       public static void main(String[] args) {
           SpringApplication.run(Application.class, args);
       }
   }
   
   // Spring Boot deployable WAR
   @SpringBootApplication
   public class Application extends SpringBootServletInitializer {
       @Override
       protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
           return application.sources(Application.class);
       }
       
       public static void main(String[] args) {
           SpringApplication.run(Application.class, args);
       }
   }
   ```

3. **Dependency Management**:
   - **Spring MVC**: Manual dependency management
   - **Spring Boot**: Starter dependencies simplify dependency management

   ```xml
   <!-- Spring MVC dependencies -->
   <dependencies>
       <dependency>
           <groupId>org.springframework</groupId>
           <artifactId>spring-webmvc</artifactId>
           <version>5.3.9</version>
       </dependency>
       <dependency>
           <groupId>org.springframework</groupId>
           <artifactId>spring-context</artifactId>
           <version>5.3.9</version>
       </dependency>
       <!-- Many more dependencies... -->
   </dependencies>
   
   <!-- Spring Boot - single starter -->
   <dependencies>
       <dependency>
           <groupId>org.springframework.boot</groupId>
           <artifactId>spring-boot-starter-web</artifactId>
       </dependency>
   </dependencies>
   ```

4. **Application Properties**:
   - **Spring MVC**: XML or Java configuration for properties
   - **Spring Boot**: Simple application.properties/yml configuration

   ```properties
   # Spring Boot application.properties
   spring.datasource.url=jdbc:mysql://localhost/db
   spring.datasource.username=user
   spring.datasource.password=password
   server.port=8080
   ```

5. **Production Features**:
   - **Spring MVC**: Requires additional configuration for metrics, health checks, etc.
   - **Spring Boot**: Built-in Actuator provides production-ready features

   ```java
   // Spring Boot Actuator
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-actuator</artifactId>
   </dependency>
   ```

6. **REST API Development**:
   - **Spring MVC**: Requires additional configuration
   - **Spring Boot**: Simplified with auto-configuration

   ```java
   // Spring MVC REST controller
   @Controller
   public class UserController {
       @RequestMapping(value = "/users", method = RequestMethod.GET, 
                       produces = MediaType.APPLICATION_JSON_VALUE)
       @ResponseBody
       public List<User> getUsers() {
           // Implementation
       }
   }
   
   // Spring Boot REST controller
   @RestController
   public class UserController {
       @GetMapping("/users")
       public List<User> getUsers() {
           // Implementation
       }
   }
   ```

### 7. Spring Boot Auto-Configuration

Spring Boot auto-configuration automatically configures a Spring application based on the dependencies on the classpath.

**How Auto-Configuration Works**:
1. Spring Boot detects classes on the classpath
2. Automatically creates and configures beans when needed
3. Can be overridden with explicit configuration
4. Uses conditional configuration based on:
   - Presence of specific classes
   - Properties settings
   - Bean definitions

**Key Components**:

1. **@EnableAutoConfiguration**:
   - Enables Spring Boot's auto-configuration mechanism
   - Part of @SpringBootApplication

   ```java
   @EnableAutoConfiguration
   public class MyApplication {
       // ...
   }
   ```

2. **Auto-configuration Classes**:
   - Located in spring-boot-autoconfigure.jar
   - Named with `*AutoConfiguration` suffix
   - Annotated with `@Configuration`
   - Use conditional annotations

   ```java
   @Configuration
   @ConditionalOnClass(DataSource.class)
   @EnableConfigurationProperties(DataSourceProperties.class)
   public class DataSourceAutoConfiguration {
       
       @Bean
       @ConditionalOnMissingBean
       public DataSource dataSource() {
           // Create and configure DataSource
       }
   }
   ```

3. **Conditional Annotations**:
   - `@ConditionalOnClass`: When specified classes are present
   - `@ConditionalOnMissingClass`: When specified classes are not present
   - `@ConditionalOnBean`: When specified beans exist
   - `@ConditionalOnMissingBean`: When specified beans don't exist
   - `@ConditionalOnProperty`: When specified properties have certain values
   - `@ConditionalOnWebApplication`: When application is a web application
   - `@ConditionalOnExpression`: Based on SpEL expression

   ```java
   @Bean
   @ConditionalOnMissingBean
   @ConditionalOnProperty(prefix = "spring.datasource", name = "url")
   public DataSource dataSource(DataSourceProperties properties) {
       // Create DataSource only if not already defined and URL property exists
   }
   ```

4. **Auto-Configuration Ordering**:
   - `@AutoConfigureBefore`: Run before specific auto-configuration
   - `@AutoConfigureAfter`: Run after specific auto-configuration
   - `@AutoConfigureOrder`: Specify auto-configuration order

   ```java
   @Configuration
   @AutoConfigureAfter(DataSourceAutoConfiguration.class)
   public class JpaRepositoriesAutoConfiguration {
       // Runs after DataSourceAutoConfiguration
   }
   ```

**Customizing Auto-Configuration**:

1. **Explicitly define beans**:
   ```java
   @Configuration
   public class MyConfiguration {
       @Bean
       public DataSource dataSource() {
           // Custom DataSource - takes precedence over auto-configuration
       }
   }
   ```

2. **Application properties**:
   ```properties
   # Disable specific auto-configuration
   spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration
   
   # Configure existing auto-configuration
   spring.datasource.url=jdbc:mysql://localhost/test
   spring.datasource.username=user
   spring.datasource.password=password
   ```

3. **Exclude auto-configuration classes**:
   ```java
   @SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
   public class MyApplication {
       // ...
   }
   ```

4. **Create your own auto-configuration**:
   ```java
   @Configuration
   @ConditionalOnClass(MyService.class)
   @EnableConfigurationProperties(MyProperties.class)
   public class MyAutoConfiguration {
       
       @Bean
       @ConditionalOnMissingBean
       public MyService myService(MyProperties properties) {
           return new MyServiceImpl(properties.getConfig());
       }
   }
   ```
   
   Then register in `META-INF/spring.factories`:
   ```
   org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
   com.example.MyAutoConfiguration
   ```

### 8. Spring Boot Actuator and Its Features

Spring Boot Actuator provides production-ready features to help monitor and manage your application.

**Key Features**:

1. **Health Checks**:
   - Shows application health information
   - Can be customized with `HealthIndicator` implementations
   - Integrates with monitoring systems

   ```java
   // Custom HealthIndicator
   @Component
   public class CustomHealthIndicator implements HealthIndicator {
       @Override
       public Health health() {
           boolean healthy = checkHealth();
           
           if (healthy) {
               return Health.up()
                   .withDetail("service", "running")
                   .build();
           } else {
               return Health.down()
                   .withDetail("service", "not available")
                   .build();
           }
       }
   }
   ```

2. **Metrics**:
   - Measures application metrics
   - Integrates with monitoring systems (Prometheus, Graphite, etc.)
   - Collects JVM, system, and custom metrics

   ```java
   // Custom metrics with Micrometer
   @Component
   public class OrderService {
       private final MeterRegistry meterRegistry;
       
       public OrderService(MeterRegistry meterRegistry) {
           this.meterRegistry = meterRegistry;
           // Register a counter
           Counter orderCounter = meterRegistry.counter("orders.created");
       }
       
       public void createOrder() {
           // Business logic
           meterRegistry.counter("orders.created").increment();
       }
   }
   ```

3. **Auditing**:
   - Tracks audit events
   - Can be stored and analyzed

   ```java
   @Component
   public class AuditService {
       private final ApplicationEventPublisher publisher;
       
       public AuditService(ApplicationEventPublisher publisher) {
           this.publisher = publisher;
       }
       
       public void auditEvent(String principal, String type, Map<String, Object> data) {
           publisher.publishEvent(new AuditApplicationEvent(principal, type, data));
       }
   }
   ```

4. **HTTP Tracing**:
   - Records HTTP requests and responses
   - Useful for debugging

   ```properties
   # Enable HTTP tracing
   management.endpoints.web.exposure.include=httptrace
   ```

5. **Thread Dump**:
   - Shows current thread activity
   - Helps diagnose blocking issues

6. **Heap Dump**:
   - Creates heap dump files
   - Useful for memory leak analysis

7. **Environment Properties**:
   - Shows configuration properties
   - Helps verify configuration

8. **Loggers**:
   - Views and modifies log levels at runtime
   - No application restart needed

   ```java
   // Changing log level via actuator endpoint
   // POST /actuator/loggers/com.example
   // {"configuredLevel": "DEBUG"}
   ```

**Configuration**:

1. **Basic Setup**:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-actuator</artifactId>
   </dependency>
   ```

2. **Endpoint Configuration**:
   ```properties
   # Enable all endpoints
   management.endpoints.web.exposure.include=*
   
   # Or specific endpoints
   management.endpoints.web.exposure.include=health,info,metrics,loggers
   
   # Exclude specific endpoints
   management.endpoints.web.exposure.exclude=env,beans
   
   # Change base path (default is /actuator)
   management.endpoints.web.base-path=/management
   
   # Enable specific endpoint
   management.endpoint.health.enabled=true
   
   # Show health details
   management.endpoint.health.show-details=always
   ```

3. **Security Configuration**:
   ```java
   @Configuration
   public class ActuatorSecurityConfig extends WebSecurityConfigurerAdapter {
       @Override
       protected void configure(HttpSecurity http) throws Exception {
           http.requestMatcher(EndpointRequest.toAnyEndpoint())
               .authorizeRequests()
               .requestMatchers(EndpointRequest.to("health", "info")).permitAll()
               .anyRequest().hasRole("ADMIN")
               .and()
               .httpBasic();
       }
   }
   ```

4. **Custom Info Endpoint Data**:
   ```properties
   # application.properties
   info.app.name=My Application
   info.app.description=Demo application
   info.app.version=1.0.0
   ```

   ```java
   // Custom InfoContributor
   @Component
   public class CustomInfoContributor implements InfoContributor {
       @Override
       public void contribute(Builder builder) {
           builder.withDetail("custom", 
               Collections.singletonMap("key", "value"));
       }
   }
   ```

5. **Custom Endpoint**:
   ```java
   @Component
   @Endpoint(id = "features")
   public class FeaturesEndpoint {
       
       @ReadOperation
       public Map<String, Object> features() {
           Map<String, Object> features = new HashMap<>();
           features.put("feature1", true);
           features.put("feature2", false);
           return features;
       }
       
       @ReadOperation
       public String feature(@Selector String name) {
           return "Feature " + name;
       }
       
       @WriteOperation
       public void configureFeature(@Selector String name, Boolean enabled) {
           // Toggle feature state
       }
   }
   ```

### 9. Using Jetty Instead of Tomcat in Spring Boot

Spring Boot uses Tomcat as its default embedded server, but you can switch to Jetty or other alternatives.

**Steps to Use Jetty**:

1. **Exclude Tomcat and Add Jetty Dependency**:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
       <exclusions>
           <exclusion>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-tomcat</artifactId>
           </exclusion>
       </exclusions>
   </dependency>
   
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-jetty</artifactId>
   </dependency>
   ```

2. **Alternatively, Using Gradle**:
   ```gradle
   dependencies {
       implementation('org.springframework.boot:spring-boot-starter-web') {
           exclude group: 'org.springframework.boot', module: 'spring-boot-starter-tomcat'
       }
       implementation 'org.springframework.boot:spring-boot-starter-jetty'
   }
   ```

3. **Customize Jetty Configuration**:
   ```java
   @Bean
   public JettyServletWebServerFactory jettyServletWebServerFactory() {
       JettyServletWebServerFactory factory = new JettyServletWebServerFactory();
       factory.setPort(9000);
       factory.addServerCustomizers(server -> {
           // Configure Jetty server
           ThreadPool threadPool = server.getThreadPool();
           if (threadPool instanceof QueuedThreadPool) {
               QueuedThreadPool queuedThreadPool = (QueuedThreadPool) threadPool;
               queuedThreadPool.setMaxThreads(100);
               queuedThreadPool.setMinThreads(20);
           }
       });
       return factory;
   }
   ```

4. **Or Use Properties**:
   ```properties
   # Server port
   server.port=9000
   
   # Jetty specific configuration
   server.jetty.accesslog.enabled=true
   server.jetty.accesslog.filename=jetty-access.log
   server.jetty.max-http-form-post-size=10MB
   server.jetty.threads.max=200
   server.jetty.threads.min=20
   server.jetty.threads.idle-timeout=60000
   ```

5. **Advanced Customization with WebServerFactoryCustomizer**:
   ```java
   @Component
   public class JettyCustomizer implements WebServerFactoryCustomizer<JettyServletWebServerFactory> {
       
       @Override
       public void customize(JettyServletWebServerFactory factory) {
           factory.addServerCustomizers(server -> {
               // Access and customize Jetty server
               HttpConfiguration httpConfig = new HttpConfiguration();
               httpConfig.setSendServerVersion(false);
               
               ServerConnector connector = new ServerConnector(server, 
                   new HttpConnectionFactory(httpConfig));
               connector.setPort(9000);
               connector.setIdleTimeout(30000);
               
               server.addConnector(connector);
           });
       }
   }
   ```

**Advantages of Using Jetty**:
1. **Lighter Memory Footprint**: Uses less memory than Tomcat
2. **Better for High-Concurrency**: Handles many simultaneous connections well
3. **Asynchronous Support**: Good for asynchronous processing
4. **Highly Customizable**: Extensive configuration options
5. **Suitable for Microservices**: Lower overhead for small services

**Disadvantages**:
1. **Less Common**: Not as widely used as Tomcat
2. **Different JSP Support**: If using JSP, may require additional configuration
3. **Feature Differences**: Some servlet container features work differently

### 10. @SpringBootTest vs @WebMvcTest

**@SpringBootTest**:
- Loads the entire application context
- Suitable for integration tests spanning multiple layers
- Can be used with an actual or mocked web environment
- More comprehensive but slower tests

```java
@SpringBootTest
@AutoConfigureMockMvc
public class UserControllerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    public void testGetUser() throws Exception {
        // Save a test user
        User user = new User("testuser", "Test User");
        userRepository.save(user);
        
        // Test the controller
        mockMvc.perform(get("/api/users/{username}", "testuser"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("Test User"));
    }
}
```

**@WebMvcTest**:
- Loads only the web layer (controllers, filters, etc.)
- Faster than @SpringBootTest
- Services and repositories must be mocked
- Focuses on testing controller behavior in isolation

```java
@WebMvcTest(UserController.class)
public class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    public void testGetUser() throws Exception {
        // Mock service behavior
        User mockUser = new User("testuser", "Test User");
        when(userService.findByUsername("testuser")).thenReturn(mockUser);
        
        // Test the controller
        mockMvc.perform(get("/api/users/{username}", "testuser"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("Test User"));
    }
}
```

**Comparison**:

| Aspect | @SpringBootTest | @WebMvcTest |
|--------|----------------|-------------|
| Context Loading | Full application context | Only web layer |
| Test Scope | Integration tests | Controller unit tests |
| Dependencies | Auto-wired real components | Dependencies must be mocked |
| Performance | Slower | Faster |
| Configuration | More complex | Simpler |
| Use Case | End-to-end testing | Controller-focused testing |

**When to Use Each**:

**Use @SpringBootTest when**:
- Testing interaction between multiple components
- Need to test with actual database or external services
- End-to-end testing of business workflows
- Testing application configuration

**Use @WebMvcTest when**:
- Testing controller request/response handling
- Testing controller-specific logic
- Validating URL mappings and HTTP status codes
- Testing input validation
- Focusing on web layer in isolation

**Other Test Slice Annotations**:
- `@DataJpaTest`: Test JPA repositories
- `@JsonTest`: Test JSON serialization/deserialization
- `@RestClientTest`: Test REST clients
- `@DataMongoTest`: Test MongoDB repositories
- `@JdbcTest`: Test JDBC components

## Use Case Based Questions

### 1. Out of Memory Error Resolution

When encountering an OutOfMemoryError:

**Step 1: Identify the Type of OutOfMemoryError**:
- `java.lang.OutOfMemoryError: Java heap space`: Insufficient heap memory
- `java.lang.OutOfMemoryError: PermGen space` (in older JVMs): Class metadata space exhausted
- `java.lang.OutOfMemoryError: Metaspace` (in newer JVMs): Class metadata space exhausted
- `java.lang.OutOfMemoryError: GC overhead limit exceeded`: GC taking too much time
- `java.lang.OutOfMemoryError: unable to create new native thread`: Thread limit reached

**Step 2: Generate and Analyze Heap Dump**:
```bash
# Enable automatic heap dump on OOM
java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/path/to/dump.hprof -jar application.jar

# Manual heap dump using jmap
jmap -dump:format=b,file=heap_dump.hprof <pid>
```

Analyze the heap dump using tools like:
- Eclipse Memory Analyzer (MAT)
- VisualVM
- JProfiler
- YourKit

**Step 3: Check Memory Usage Patterns**:
```bash
# View memory usage with jstat
jstat -gcutil <pid> 1000

# View detailed GC logs
java -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Xloggc:gc.log -jar application.jar
```

**Step 4: Common Solutions**:

1. **For Java Heap Space**:
   - Increase heap size
   ```bash
   java -Xms1g -Xmx2g -jar application.jar
   ```
   
   - Fix memory leaks (common causes):
     - Unclosed resources (streams, connections)
     - Improper caching
     - Long-lived objects with references
     - Collection growing indefinitely
   
   - Memory optimization:
   ```java
   // Use primitive arrays instead of collections
   int[] array = new int[1000]; // More efficient than ArrayList<Integer>
   
   // Use appropriate collection implementations
   // HashMap for general use, EnumMap for enum keys, etc.
   
   // Implement object pooling for expensive objects
   public class ObjectPool<T> {
       private ConcurrentLinkedQueue<T> pool;
       private Supplier<T> objectFactory;
       
       public ObjectPool(Supplier<T> objectFactory) {
           this.objectFactory = objectFactory;
           this.pool = new ConcurrentLinkedQueue<>();
       }
       
       public T borrow() {
           T object = pool.poll();
           return object != null ? object : objectFactory.get();
       }
       
       public void returnToPool(T object) {
           pool.offer(object);
       }
   }
   ```

2. **For Metaspace/PermGen**:
   - Increase Metaspace size
   ```bash
   java -XX:MaxMetaspaceSize=256m -jar application.jar
   ```
   
   - Check for class loader leaks
   - Reduce dynamic class generation
   - Use fewer classloaders
   
3. **For GC Overhead Limit**:
   - Tune GC parameters
   ```bash
   java -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -jar application.jar
   ```
   
   - Reduce object allocation rate
   - Optimize object lifecycle

4. **For Unable to Create New Native Thread**:
   - Reduce thread creation
   - Use thread pools properly
   ```java
   // Thread pool with sensible limits
   ExecutorService executor = new ThreadPoolExecutor(
       10, // Core pool size
       50, // Max pool size
       60L, // Keep alive time
       TimeUnit.SECONDS,
       new LinkedBlockingQueue<>(100), // Queue capacity
       new ThreadPoolExecutor.CallerRunsPolicy() // Rejection policy
   );
   ```
   
   - Increase OS thread limits (Linux)
   ```bash
   ulimit -u 4096 # Increase user process limit
   ```

**Step 5: Implement Memory-Efficient Coding Practices**:
```java
// 1. Use try-with-resources for auto-closing
try (InputStream is = new FileInputStream("file.txt")) {
    // Use the resource
}

// 2. Use weak references for caching
Map<Key, WeakReference<Value>> cache = new HashMap<>();

// 3. Buffer streams for large data
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    // Read line by line
}

// 4. Implement pagination for large data sets
public List<User> getUsers(int page, int pageSize) {
    return userRepository.findAll(PageRequest.of(page, pageSize));
}

// 5. Stream large collections instead of loading into memory
Files.lines(Paths.get("large-file.txt"))
     .filter(line -> line.contains("important"))
     .forEach(System.out::println);
```

### 2. Resolving Production Performance Issues

When all requests are timing out in production:

**Step 1: Initial Assessment**:
- Check system monitoring dashboards (CPU, memory, disk, network)
- Look at recent deployments or changes
- Check for error logs
- Verify dependencies (databases, external services)

**Step 2: Gather Diagnostic Information**:
```bash
# Check system load
top -c
vmstat 1

# Check for memory issues
free -m

# Check disk space and I/O
df -h
iostat -x 1

# Check network
netstat -anp | grep java
```

**Step 3: Application-Specific Diagnostics**:
```bash
# Thread dump (multiple to spot stuck threads)
jstack <pid> > thread_dump_$(date +%s).txt

# Heap dump if memory issue suspected
jmap -dump:format=b,file=heap_dump.hprof <pid>

# JVM monitoring
jstat -gcutil <pid> 1000
```

**Step 4: Common Causes and Solutions**:

1. **Database Connection Issues**:
   - Connection pool exhaustion
   ```java
   // Increase pool size temporarily
   spring.datasource.hikari.maximum-pool-size=20
   
   // Add connection timeout
   spring.datasource.hikari.connection-timeout=30000
   
   // Add statement timeout
   spring.datasource.hikari.connection-timeout=30000
   ```
   
   - Slow queries
   ```sql
   -- Find slow queries in MySQL
   SHOW FULL PROCESSLIST;
   
   -- Optimize with proper indexes
   CREATE INDEX idx_user_email ON users(email);
   ```

2. **External Service Dependency Issues**:
   - Implement circuit breaker
   ```java
   @Bean
   public CircuitBreakerFactory circuitBreakerFactory() {
       CircuitBreakerConfig config = CircuitBreakerConfig.custom()
           .failureRateThreshold(50)
           .waitDurationInOpenState(Duration.ofSeconds(10))
           .build();
       
       return new Resilience4JCircuitBreakerFactory(config);
   }
   ```
   
   - Set appropriate timeouts
   ```java
   @Bean
   public RestTemplate restTemplate() {
       HttpComponentsClientHttpRequestFactory factory = new HttpComponentsClientHttpRequestFactory();
       factory.setConnectTimeout(5000);
       factory.setReadTimeout(5000);
       return new RestTemplate(factory);
   }
   ```

3. **Resource Contention**:
   - Thread deadlocks or contention
   ```java
   // Improve synchronization
   private final ReentrantLock lock = new ReentrantLock();
   
   public void processData() {
       if (lock.tryLock(5, TimeUnit.SECONDS)) {
           try {
               // Critical section
           } finally {
               lock.unlock();
           }
       } else {
           // Handle timeout
       }
   }
   ```
   
   - CPU-intensive operations
   ```java
   // Move to async processing
   @Async
   public CompletableFuture<Result> processDataAsync() {
       // CPU-intensive work
       return CompletableFuture.completedFuture(result);
   }
   ```

4. **Memory Issues**:
   - Increase heap temporarily
   ```bash
   java -Xmx2g -jar application.jar
   ```
   
   - Tune garbage collection
   ```bash
   java -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -jar application.jar
   ```

5. **Thread Pool Exhaustion**:
   - Adjust thread pool parameters
   ```java
   @Bean
   public Executor taskExecutor() {
       ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
       executor.setCorePoolSize(10);
       executor.setMaxPoolSize(50);
       executor.setQueueCapacity(100);
       executor.setThreadNamePrefix("Async-");
       return executor;
   }
   ```

**Step 5: Short-Term Resolution**:
- Implement request throttling
```java
@Bean
public FilterRegistrationBean<Filter> rateLimiterFilter() {
    FilterRegistrationBean<Filter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new RateLimiterFilter(100)); // 100 requests per second
    registrationBean.addUrlPatterns("/*");
    return registrationBean;
}
```

- Add circuit breakers for degraded functionality
- Increase timeouts temporarily
- Scale horizontally if possible
- Consider service restart if severe

**Step 6: Long-Term Improvements**:
- Add comprehensive monitoring
```java
@Bean
public TimedAspect timedAspect(MeterRegistry registry) {
    return new TimedAspect(registry);
}

@Service
public class ProductService {
    @Timed("product.fetch") // Measures method execution time
    public Product getProduct(Long id) {
        // Implementation
    }
}
```

- Implement caching
```java
@Configuration
@EnableCaching
public class CacheConfig {
    @Bean
    public CacheManager cacheManager() {
        return new ConcurrentMapCacheManager("products", "categories");
    }
}

@Service
public class ProductService {
    @Cacheable("products")
    public Product getProduct(Long id) {
        // Implementation, only executed on cache miss
    }
}
```

- Database optimization
- Load testing and profiling
- Auto-scaling strategies

### 3. Inheritance ('is-a') vs. Composition ('has-a')

**Inheritance ('is-a' relationship)**:
- Represents a subclass extending a superclass
- Creates a strong relationship where subclass is a specialized version of superclass
- Achieved using `extends` keyword

```java
// Inheritance example
public class Vehicle {
    private String make;
    private String model;
    
    public void start() {
        System.out.println("Vehicle starting");
    }
    
    // Getters and setters
}

public class Car extends Vehicle {
    private int numberOfDoors;
    
    @Override
    public void start() {
        System.out.println("Car starting with key");
    }
    
    public void drive() {
        System.out.println("Car driving");
    }
    
    // Getters and setters
}
```

**Composition ('has-a' relationship)**:
- Represents a class containing instances of other classes as members
- Creates a relationship where one class "has" or "uses" another
- Achieved by defining member variables

```java
// Composition example
public class Engine {
    private int horsepower;
    
    public void start() {
        System.out.println("Engine starting");
    }
    
    // Getters and setters
}

public class Car {
    private Engine engine; // Car "has-a" Engine
    private String make;
    private String model;
    
    public Car(Engine engine) {
        this.engine = engine;
    }
    
    public void start() {
        System.out.println("Car starting");
        engine.start();
    }
    
    public void drive() {
        System.out.println("Car driving");
    }
    
    // Getters and setters
}
```

**Comparison**:

| Aspect | Inheritance | Composition |
|--------|-------------|-------------|
| Relationship | "is-a" (Car is a Vehicle) | "has-a" (Car has an Engine) |
| Coupling | Tighter coupling | Looser coupling |
| Flexibility | Less flexible | More flexible |
| Code Reuse | Through class extension | Through object composition |
| Runtime Behavior | Fixed at compile time | Can change at runtime |
| Access to Internal State | Subclass can access protected members | Only through public interface |
| Design Approach | Implementation inheritance | Interface implementation + delegation |

**Difference between Composition and Aggregation**:

**Aggregation**:
- Special form of association
- "Has-a" relationship but with independent lifecycle
- Container doesn't "own" the component
- Component can exist without the container

```java
// Aggregation example
public class University {
    private List<Department> departments;
    
    public void addDepartment(Department department) {
        departments.add(department);
    }
    
    // Departments can exist without university
}

public class Department {
    private String name;
    
    // Department can exist independently
}
```

**Composition**:
- Stronger form of aggregation
- "Has-a" relationship with dependent lifecycle
- Container "owns" the component
- Component cannot exist without the container

```java
// Composition example
public class Car {
    private Engine engine; // Engine cannot exist without the car
    
    public Car() {
        this.engine = new Engine(); // Engine created with Car
    }
    
    // When Car is destroyed, Engine is also destroyed
}

public class Engine {
    // Engine depends on Car
}
```

**Best Practices**:
- "Favor composition over inheritance" - Design principle
- Use inheritance for true "is-a" relationships
- Use composition for "has-a" relationships
- Consider interfaces + composition instead of deep inheritance hierarchies
- Avoid inheriting from concrete classes; prefer abstract classes or interfaces

### 4. Design Pattern Implementation

**Singleton Pattern**:
```java
public class DatabaseConnection {
    private static volatile DatabaseConnection instance;
    private Connection connection;
    
    private DatabaseConnection() {
        // Private constructor
        try {
            String url = "jdbc:mysql://localhost:3306/mydb";
            connection = DriverManager.getConnection(url, "user", "password");
        } catch (SQLException e) {
            throw new RuntimeException("Failed to create connection", e);
        }
    }
    
    public static DatabaseConnection getInstance() {
        if (instance == null) {
            synchronized (DatabaseConnection.class) {
                if (instance == null) {
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }
    
    public Connection getConnection() {
        return connection;
    }
}

// Usage
Connection conn = DatabaseConnection.getInstance().getConnection();
```

**Factory Pattern**:
```java
// Product interface
public interface PaymentProcessor {
    void processPayment(double amount);
}

// Concrete products
public class CreditCardProcessor implements PaymentProcessor {
    @Override
    public void processPayment(double amount) {
        System.out.println("Processing credit card payment of $" + amount);
    }
}

public class PayPalProcessor implements PaymentProcessor {
    @Override
    public void processPayment(double amount) {
        System.out.println("Processing PayPal payment of $" + amount);
    }
}

// Factory
public class PaymentProcessorFactory {
    public static PaymentProcessor createProcessor(String type) {
        if ("credit".equalsIgnoreCase(type)) {
            return new CreditCardProcessor();
        } else if ("paypal".equalsIgnoreCase(type)) {
            return new PayPalProcessor();
        } else {
            throw new IllegalArgumentException("Unknown payment type: " + type);
        }
    }
}

// Usage
PaymentProcessor processor = PaymentProcessorFactory.createProcessor("credit");
processor.processPayment(100.0);
```

**Builder Pattern**:
```java
public class User {
    // All final attributes
    private final String firstName; // required
    private final String lastName; // required
    private final int age; // optional
    private final String phone; // optional
    private final String address; // optional
    
    private User(UserBuilder builder) {
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.age = builder.age;
        this.phone = builder.phone;
        this.address = builder.address;
    }
    
    // Getters, no setters to make immutable
    
    // Builder class
    public static class UserBuilder {
        private final String firstName;
        private final String lastName;
        private int age;
        private String phone;
        private String address;
        
        public UserBuilder(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }
        
        public UserBuilder age(int age) {
            this.age = age;
            return this;
        }
        
        public UserBuilder phone(String phone) {
            this.phone = phone;
            return this;
        }
        
        public UserBuilder address(String address) {
            this.address = address;
            return this;
        }
        
        public User build() {
            return new User(this);
        }
    }
}

// Usage
User user = new User.UserBuilder("John", "Doe")
                    .age(30)
                    .phone("1234567890")
                    .address("123 Street, City")
                    .build();
```

**Strategy Pattern**:
```java
// Strategy interface
public interface SortingStrategy {
    <T extends Comparable<T>> void sort(List<T> list);
}

// Concrete strategies
public class QuickSort implements SortingStrategy {
    @Override
    public <T extends Comparable<T>> void sort(List<T> list) {
        System.out.println("Sorting using quick sort");
        // Implementation
    }
}

public class MergeSort implements SortingStrategy {
    @Override
    public <T extends Comparable<T>> void sort(List<T> list) {
        System.out.println("Sorting using merge sort");
        // Implementation
    }
}

// Context class
public class Sorter {
    private SortingStrategy strategy;
    
    public Sorter(SortingStrategy strategy) {
        this.strategy = strategy;
    }
    
    public void setStrategy(SortingStrategy strategy) {
        this.strategy = strategy;
    }
    
    public <T extends Comparable<T>> void sort(List<T> list) {
        strategy.sort(list);
    }
}

// Usage
List<Integer> numbers = Arrays.asList(3, 1, 4, 1, 5, 9);
Sorter sorter = new Sorter(new QuickSort());
sorter.sort(numbers);

// Change strategy at runtime
sorter.setStrategy(new MergeSort());
sorter.sort(numbers);
```

**Observer Pattern**:
```java
// Observer interface
public interface Observer {
    void update(String message);
}

// Concrete observer
public class EmailNotifier implements Observer {
    private String email;
    
    public EmailNotifier(String email) {
        this.email = email;
    }
    
    @Override
    public void update(String message) {
        System.out.println("Sending email to " + email + ": " + message);
    }
}

// Subject (Observable)
public class NewsPublisher {
    private List<Observer> observers = new ArrayList<>();
    
    public void subscribe(Observer observer) {
        observers.add(observer);
    }
    
    public void unsubscribe(Observer observer) {
        observers.remove(observer);
    }
    
    public void notifyObservers(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }
    
    public void publishNews(String news) {
        System.out.println("Publishing news: " + news);
        notifyObservers(news);
    }
}

// Usage
NewsPublisher publisher = new NewsPublisher();
publisher.subscribe(new EmailNotifier("user1@example.com"));
publisher.subscribe(new EmailNotifier("user2@example.com"));
publisher.publishNews("Breaking news: Java 17 released!");
```

**Decorator Pattern**:
```java
// Component interface
public interface Beverage {
    String getDescription();
    double getCost();
}

// Concrete component
public class Coffee implements Beverage {
    @Override
    public String getDescription() {
        return "Coffee";
    }
    
    @Override
    public double getCost() {
        return 3.0;
    }
}

// Decorator base class
public abstract class BeverageDecorator implements Beverage {
    protected Beverage beverage;
    
    public BeverageDecorator(Beverage beverage) {
        this.beverage = beverage;
    }
}

// Concrete decorators
public class MilkDecorator extends BeverageDecorator {
    public MilkDecorator(Beverage beverage) {
        super(beverage);
    }
    
    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Milk";
    }
    
    @Override
    public double getCost() {
        return beverage.getCost() + 0.5;
    }
}

public class SugarDecorator extends BeverageDecorator {
    public SugarDecorator(Beverage beverage) {
        super(beverage);
    }
    
    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Sugar";
    }
    
    @Override
    public double getCost() {
        return beverage.getCost() + 0.2;
    }
}

// Usage
Beverage coffee = new Coffee();
coffee = new MilkDecorator(coffee);
coffee = new SugarDecorator(coffee);
System.out.println("Order: " + coffee.getDescription());
System.out.println("Cost: $" + coffee.getCost());
```