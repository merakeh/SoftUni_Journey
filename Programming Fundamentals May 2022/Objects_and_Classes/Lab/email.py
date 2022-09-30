
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

command = input()
while command != "Stop":
    info = command.split(' ')
    sender_new = info[0]
    receiver_new = info[1]
    content_new = info[2]
    email = Email(sender_new, receiver_new, content_new)
    emails.append(email)
    command = input()

sent_emails = list(map(lambda x: int(x), input().split(', ')))
for x in sent_emails:
    emails[x].send()

for e_mail in emails:
    print(e_mail.get_info())

