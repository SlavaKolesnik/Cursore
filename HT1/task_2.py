# 2. Сlass Profile:
#  """
# Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age,
#  sex    Override a printable string representation of Profile class and return: list of the params mentioned above """


class Profile:
    def __init__(self, first_name, last_name, phone_number, address, e_mail, birthday, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = e_mail
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name: {self.first_name}, Last Name: {self.last_name}, Phone Number: {self.phone_number}, " \
               f"Address: {self.address}, Email: {self.email}, Birthday: {self.birthday}, Age: {self.age}," \
               f" Sex: {self.sex}"


profile = Profile('Slava', 'Kolesnik', '+380960436190', 'Chercassy 18000', 'slava1995kolesnik2@ukr.net', '20.11', '27',
                  'man')

print(profile)

