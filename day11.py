#1. Create a class called "EmailClient" with attributes "username" and "password". Implement a method called "send_email" that takes in the recipient's email address and the message content as parameters, and prints out a message stating that the email has been sent successfully. Create an instance of the class with a sample username and password. Test the "send_email" method by calling it with a recipient's email address and a message content.

class EmailClient:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    
    def send_email(self, recipients_email_address, message_content):
        # print('The message has been sent succenfully')
        print(f"The message has been sent succenfully from the recipient '{recipients_email_address}' and the message content was '{message_content}'")

xyzCleint = EmailClient('Arsalan Ahmed', 'password@123')
print(xyzCleint.username)
print(xyzCleint.password)

xyzCleint.send_email('arsalan@gamil.com', 'I am a good boy')
