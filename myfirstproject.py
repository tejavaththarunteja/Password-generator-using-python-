import string
import random
def generate_password(length=12):
    # out character pool
    chars=string.ascii_letters+string.digits+string.punctuation

    # pick random characters length time
    password=''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password(16))
