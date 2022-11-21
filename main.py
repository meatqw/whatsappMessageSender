import pywhatkit


def send(number, msg, hour, minute):
    # Send a WhatsApp Message to a Contact at
    pywhatkit.sendwhatmsg(number, msg, hour, minute)

# def read_phone_list():
#     with open('phone.txt', 'r') as phone_txt:
#         phones = phone_txt.read().split('\n')
#         print(phones)

# send('1', 3, 4)
# read_phone_list()
