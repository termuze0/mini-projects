import time

def speed_checker(func, *args, **kwargs):
    .

    :param func: Function to measure.
    :param args: Positional arguments for the function.
    :param kwargs: Keyword arguments for the function.
    :return: Result of the function and the execution time.
    """
    start_time = time.perf_counter()  # Start the timer
    result = func(*args, **kwargs)   # Execute the function
    end_time = time.perf_counter()   # End the timer
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.6f} seconds")
    return result, execution_time

# Example Usage
def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Check speed of sample_function with n=10_000_000
result, exec_time = speed_checker(sample_function, 10_000_000)
print(f"Result: {result}")