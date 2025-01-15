def simple_compiler():
    print("Simple Python Compiler")
    print("Type your Python code below. Type 'exit' to quit.")
    while True:
        try:
            # Input code from the user
            code = input(">>> ")
            if code.lower() == 'exit':  # Exit condition
                print("Exiting compiler. Goodbye!")
                break
            # Execute the code dynamically
            exec(code)
        except Exception as e:
            # Handle and display any runtime errors
            print(f"Error: {e}")

# Run the simple compiler
simple_compiler()