import time


# Decorator to calculate the execution time of a function
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        try:
            result = func(*args, **kwargs)
        except KeyboardInterrupt:
            end_time = time.time()  # End time when interrupted
            total_time = end_time - start_time
            print(f"\nTotal time taken before interruption: {total_time} seconds")
            raise  # Re-raise the exception so the program exits cleanly
        return result

    return wrapper


# Function that contains the infinite loop
@time_decorator
def my_loop():
    while True:
        print(1)
        time.sleep(1)  # Adding sleep to avoid overwhelming the console


# Call the function
my_loop()
