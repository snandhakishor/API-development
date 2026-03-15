import bcrypt


def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# verifying password

def verify_password(raw_password, hashed_password):
    return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))