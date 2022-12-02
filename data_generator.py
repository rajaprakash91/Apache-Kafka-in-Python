import random 
import string 


user_ids = list(range(11))
recipient_ids = list(range(1, 101))
names = ['Raja', 'Jade', 'Nalan', 'Kicha', 'Appa', 'Amma', 'Sudars', 'Subas', 'Ronaldo', 'Messi', 'BruceLee']
locations = ['chennai', 'mumbai', 'bangalore'
    , 'hyderabad', 'bali', 'meghalaya', 'leh', 'sikkim', 'gangtok', 'himachal', 'paris'
    , 'us', 'belgium', 'monta', 'lasVegas', 'japan', 'singapore', 'goa'
    , 'maldives', 'croatia', 'malaysia', 'dubai', 'qatar']

partitions = [0,1]

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)

    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()

    # Random Name
    nm = names[random_user_id]

    # Random location
    loc = random.choice(locations)

    # Random parititons
    part = random.choice(partitions)

    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    # Generate a random message
    message = {
        'value': ''.join(random.choice(string.ascii_letters) for i in range(32)),
        'partition' : part
    }

    return {
        'user_id': random_user_id,
        'user_name' : nm,
        'current_location' : loc,
        'recipient_id': random_recipient_id,
        'message': message
    }
