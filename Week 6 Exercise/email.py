# Create class Email. The __init__ method should receive sender, receiver and a content.
# It should also have a default set to False attribute called is_sent.
# The class should have two additional methods:
#     • send() - sets the is_sent attribute to True
#     • get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver, and the third one – the content. On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
# Call the send() method for the given indices of emails. For each email, call the get_info() method.
# Note: submit all of your code, including the class


class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails_list = []


while True:
    input_data = input()
    if input_data == 'Stop':
        break
    input_data = input_data.split()
    sender, receiver, content = input_data[0], input_data[1], input_data[2]
    email = Email(sender, receiver, content)
    emails_list.append(email)

sent_indexes = [int(x) for x in input().split(', ')]

for index in sent_indexes:
    emails_list[index].is_sent = True

for email in emails_list:
    print(email.get_info())