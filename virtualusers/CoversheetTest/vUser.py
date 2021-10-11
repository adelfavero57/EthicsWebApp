import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run_user(self):
        string = "python3 " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Coversheet tests
# Virtual test for filling the questions in coversheet page
test1 = vUser(dir_path + "/coversheet1.py")
# Virtual test for navigation bar to switch between coversheet and ethics questionnaire
test2 = vUser(dir_path + "/coversheet2.py")


# List of virtual user tests
Users = []

# Add all tests to list
Users.append(test1)
Users.append(test2)


# Run tests
for i in Users:
    i.run_user()
