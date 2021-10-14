import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run(self):
        string = "python3 " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Login tests
test1 = vUser(dir_path + "/register1.py")

# List of virtual user tests
Users = []

# Add all tests to list
Users.append(test1)

# Run tests
for i in Users:
    i.run()
