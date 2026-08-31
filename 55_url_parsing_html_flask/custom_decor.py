
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticated_decor(func):
    def wrapper(*args):
        expected_user = args[0]
        if expected_user.is_logged_in:
            func(expected_user)
        else:
            print(f"{expected_user.name} is not logged in.")
    return wrapper

@is_authenticated_decor
def create_blog_post(an_user):
    print(f"This is the first blog post of {an_user.name}")

soham = User("Soham")

create_blog_post(soham)
