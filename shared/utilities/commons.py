import uuid


def generate_public_id():
    """
    Generate a 12 charachter unique string for public ids
    """
    return uuid.uuid4().hex[:12]
