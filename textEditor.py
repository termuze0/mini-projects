class TextEditor:
    def __init__(self):
        self.text=""
        self.history=[]
    def add_text(self,newText):
        self.history.append(newText)
        self.text+=newText
    def undo(self):
        if self.history:
            self.text = self.history.pop()
    def current_text(self):
        return self.text