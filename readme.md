# Mutex Implementation with Python

## Project Overview

This project demonstrates a custom implementation of a **Mutex (Mutual Exclusion)** in Python using the `threading` module. A Mutex ensures that only one thread can access a critical section of the code at a time, preventing race conditions. The example provided uses this custom Mutex to safely increment a shared resource across multiple threads.

---

## Features

- Custom `Mutex` class with `acquire()` and `release()` methods for thread synchronization.
- Demonstrates thread-safe modification of a shared resource.
- Uses Python's `threading.Condition` for efficient thread waiting and notification.
- Simple and clear structure for learning about locks and synchronization.

---

## Prerequisites

- Python 3.x installed on your system.

---

## How It Works

1. **Custom Mutex Implementation**:
   - The `Mutex` class uses a `Condition` to wait for the lock to be available.
   - Threads acquire the lock before entering the critical section and release it afterward.

2. **Shared Resource**:
   - The `shared_resource` variable is incremented by 10 threads, ensuring no two threads modify it simultaneously.

3. **Thread Management**:
   - Threads are started and joined to ensure proper synchronization and program flow.

---

## Installation and Usage

1. Clone or download the project files.

2. Run the script using Python:
   ```bash
   python script_name.py
   ```

3. The output will display incremental updates to the shared resource and the final result:
   ```
    Incremented: 1
    Incremented: 2
    Incremented: 3
    Incremented: 4
    Incremented: 5
    Incremented: 6
    Incremented: 7
    Incremented: 8
    Incremented: 9
    Incremented: 10
    Final Result: 10
   ```

---

## Code Highlights

- **Mutex Class**:
   ```python
   class Mutex:
       def __init__(self):
           self.locked = False
           self.condition = threading.Condition()

       def acquire(self):
           with self.condition:
               while self.locked:
                   self.condition.wait()
               self.locked = True

       def release(self):
           with self.condition:
               self.locked = False
               self.condition.notify_all()
   ```

- **Critical Section Protection**:
   ```python
   def increment():
       global shared_resource
       lock.acquire()
       try:
           shared_resource += 1
           print("Incremented:", shared_resource)
       finally:
           lock.release()
   ```

---

## Learning Objectives

By exploring this project, you will:
- Understand the basics of thread synchronization in Python.
- Learn how to implement a custom Mutex using `threading.Condition`.
- See practical examples of how to avoid race conditions in multithreaded programs.

---

## Contributing

If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

---

## License

This project is released under the MIT License. You are free to use, modify, and distribute this code. See the `LICENSE` file for details.