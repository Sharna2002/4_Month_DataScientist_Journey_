# Create @admin_required. If global user != "admin", raise PermissionError
user = "admin"

def admin_required(func):
    def wrapper():
        if user != "admin":
            raise PermissionError
        return func()
    return wrapper

@admin_required
def author():
    print("Admin panel")

author()
