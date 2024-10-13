from collections import deque

class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)
        print(f"Order added: {order}")

    def serve_order(self):
        if self.queue:
            served_order = self.queue.popleft()
            print(f"Order served: {served_order}")
        else:
            print("No pending orders!")

    def view_orders(self):
        if self.queue:
            print("Pending Orders:")
            for idx, order in enumerate(self.queue, 1):
                print(f"{idx}. {order}")
        else:
            print("No orders in the queue.")

    def clear_orders(self):
        self.queue.clear()
        print("All orders cleared!")

def main():
    queue = OrderQueue()
    while True:
        print("\n--- Restaurant Order System ---")
        print("1. Add Order")
        print("2. Serve Order")
        print("3. View Orders")
        print("4. Clear Orders")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            order = input("Enter the order details: ")
            queue.add_order(order)
        elif choice == '2':
            queue.serve_order()
        elif choice == '3':
            queue.view_orders()
        elif choice == '4':
            queue.clear_orders()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
