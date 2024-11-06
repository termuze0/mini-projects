class BrowserHistorySimulator:
    def __init__(self):
        self.back_stack = []  # Stack to hold back history
        self.forward_stack = []  # Stack to hold forward history
        self.current_page = None  # Tracks the current page

    def visit(self, url):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)  # Save the current page to the back stack
        self.current_page = url  # Set the current page to the new URL
        self.forward_stack.clear()  # Clear the forward history since we're visiting a new page
        print(f"Visiting: {self.current_page}")

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_page)  # Push the current page to the forward stack
            self.current_page = self.back_stack.pop()  # Pop the previous page from the back stack
            print(f"Going back to: {self.current_page}")
        else:
            print("No more pages to go back to.")

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_page)  # Push the current page to the back stack
            self.current_page = self.forward_stack.pop()  # Pop the next page from the forward stack
            print(f"Going forward to: {self.current_page}")
        else:
            print("No more pages to go forward to.")

    def get_current_page(self):
        return self.current_page

# Example usage:
browser = BrowserHistorySimulator()

browser.visit("www.google.com")
browser.visit("www.youtube.com")
browser.visit("www.github.com")

browser.back()  # Should go back to "www.youtube.com"
browser.back()  # Should go back to "www.google.com"
browser.forward()  # Should go forward to "www.youtube.com"
browser.visit("www.stackoverflow.com")  # Should visit a new page
browser.back()  # Should go back to "www.youtube.com"
browser.forward()  # Should go forward to "www.stackoverflow.com"

