guest_list = []

def main():
    while True:
        invitation = input('Who do you want to invite?').strip().title()
        if invitation.lower() == 'done':
            break
        guest_list.append(invitation)
    for guest in guest_list:
        print(write_letter(guest, 'Princess Pear'))        

    
def write_letter(receiver, sender):
    return f"""
    ______________________
    Dear, { receiver }
    You are invited to a ball to my castle at 7pm
    Sincerely, { sender }
    ______________________
    """
    
main()