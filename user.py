class User:
  def __init__(self, first_name, last_name, email):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email

  def name(self):
    print(self.first_name, self.last_name)

users = [
  User("Kira", "Katze", "Kira@Katze.com"),
  User("Hugo", "Hase", "Hugo@Hase.com"),
  User("Ingo", "Igel", "Ingo@Igel.com")
]
map user in users:
  "Hallo " + user.name()
