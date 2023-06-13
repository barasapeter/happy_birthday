import random
import faker, shelve
from datetime import datetime, timedelta

fake = faker.Faker()

def generate_sms(num_messages) -> dict:
    sms_data = {}
    current_time = datetime.now()

    for _ in range(num_messages):
        sender = fake.phone_number()
        recipient = fake.phone_number()
        message_content = fake.text(max_nb_chars=160)
        timestamp = current_time - timedelta(minutes=random.randint(1, 60))
        attachments = []

        # Simulate attachments
        num_attachments = random.randint(0, 15)
        for _ in range(num_attachments):
            file_name = fake.file_name(extension=random.choice(['jpg', 'png', 'mp3']))
            attachments.append(file_name)
        
        sms = {
            'sender': sender,
            'recipient': recipient,
            'timestamp': timestamp,
            'message': message_content,
            'attachments': attachments
        }
        sms_data[_] = sms
    
    return sms_data

# Generate 5 sample SMS messages with attachments
sms_data = generate_sms(500)

# Save the sms in the database
# with shelve.open('./sms database/sms-database') as database:
#     for key in sms_data:
#         database[str(key)] = sms_data[key]
#     for key in database.keys():
#         print(database[key])

if __name__ == '__main__':
# Print the generated SMS data
    for sms in sms_data:
        print(f"Sender: {sms_data[sms]['sender']}")
        print(f"Recipient: {sms_data[sms]['recipient']}")
        print(f"Timestamp: {sms_data[sms]['timestamp']}")
        print(f"Message: {sms_data[sms]['message']}")
        
        if sms_data[sms]['attachments']:
            print("Attachments:")
            for attachment in sms_data[sms]['attachments']:
                print(attachment)
        
        print("-" * 30)

        

