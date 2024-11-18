import threading

# Define a custom Mutex class to manage mutual exclusion
class Mutex:
    def __init__(self):
        self.locked = False  # Indicates whether the lock is acquired
        self.condition = threading.Condition()  # Condition variable for synchronization

    def acquire(self):
        # Attempt to acquire the lock
        with self.condition:  # Ensure thread-safe access
            while self.locked:  # If the lock is already acquired, wait
                self.condition.wait()  # Block until the lock is released
            self.locked = True  # Lock acquired

    def release(self):
        # Release the lock
        with self.condition:  # Ensure thread-safe access
            self.locked = False  # Unlock
            self.condition.notify_all()  # Notify all waiting threads

# Create a shared lock instance
lock = Mutex()
shared_resource = 0  # Shared resource to be incremented by threads

# Function to increment the shared resource
def increment():
    global shared_resource
    lock.acquire()  # Acquire the lock before modifying the shared resource
    try:
        shared_resource += 1  # Increment the shared resource
        print("Incremented:", shared_resource)  # Log the current value
    finally:
        lock.release()  # Always release the lock

# Create a list to hold thread objects
threads = []

# Launch 10 threads that increment the shared resource
for _ in range(10):
    thread = threading.Thread(target=increment)  # Create a new thread
    threads.append(thread)  # Add the thread to the list
    thread.start()  # Start the thread

# Wait for all threads to complete
for thread in threads:
    thread.join()  # Block until the thread finishes

# Print the final value of the shared resource
print(f"Final Result: {shared_resource}")
