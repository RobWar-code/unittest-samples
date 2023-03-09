from datetime import date, timedelta
import requests


class Student:
    """ A base class for demonstrating testing """

    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return self._firstname + " " + self._lastname

    @property
    def email(self):
        return f"{self._firstname.lower()}.{self._lastname.lower()}@email.com"

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/\
            {self._lastname}/{self._firstname}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with our request"
