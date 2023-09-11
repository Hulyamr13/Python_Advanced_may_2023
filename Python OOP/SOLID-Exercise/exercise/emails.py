class IContent:
    def format(self):
        pass


class MyContent(IContent):
    def __init__(self, text):
        self.text = text

    def format(self):
        return f"<MyML>{self.text}</MyML>"


class Email:
    def __init__(self, platform):
        self.platform = platform
        self.sender = None
        self.receiver = None
        self.content = None

    def set_sender(self, sender):
        self.sender = sender

    def set_receiver(self, receiver):
        self.receiver = receiver

    def set_content(self, content):
        self.content = content

    def __str__(self):
        return f"Sender: I'm {self.sender}\nReceiver: I'm {self.receiver}\nContent:\n{self.content.format()}"


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
