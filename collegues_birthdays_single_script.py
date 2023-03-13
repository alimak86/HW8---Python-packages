import sys
from datetime import datetime, date, timedelta
import random
import time

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

ONE_WEEK = 1


def current():
    return datetime.now()


def current_day():
    return current().day


def current_weekend():
    delta = SATURDAY - current().weekday()
    if delta < 0:
        delta = 0
    return current() + timedelta(days=delta)


def next(day1):
    current_day = datetime(
        year=current().year,
        month=current().month,
        day=current().day + day1 - current().weekday()
    )  # current day
    next_day = current_day + timedelta(weeks=ONE_WEEK)
    return next_day


JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

names = ["Alisa", "Kolia", "Viktor", "Ruslan", "Nikita", "Vladimir",
         "Katia", "Irina", "Vladislav", "Rostislav", "Miroslav", "Olga", "Daria"]

days = {JANUARY: 31, FEBRUARY: 28, MARCH: 31, APRIL: 30, MAY: 31, JUNE: 30,
        JULY: 31, AUGUST: 31, SEPTEMBER: 30, OCTOBER: 31, NOVEMBER: 30, DECEMBER: 31}

YEAR = 1985  # will generate random dates for the 1985 year - just for testing


def get_day(month):  # return random day for the month
    min_day = 1  # minimum days in the month
    max_day = days[month]  # maximum days in the month
    return random.randint(min_day, max_day)


def get_month():  # return random month number
    return random.randint(MARCH, MARCH)  # only for testing


def get_date():  # returns random date in 2023 year
    mois = get_month()  # get month
    jour = get_day(mois)  # get day
    date = datetime(year=YEAR, month=mois, day=jour)  # generate the date
    return date


def list_generator(number):  # generates a dictionary of the users and their birthdays
    # 3print("generator: ",number)
    users = {}  # empty dictionary
    for i in range(number):
        random.shuffle(names)
        name = random.randint(0, len(names)-1)  # get name randomly
        # print(names[name])
        birthday = get_date()  # generate random date
        users[names[name]] = birthday
    return users


MAX_EXPECTED = 100

WEEK = {MONDAY: "Monday", TUESDAY: "Tuesday", WEDNESDAY: "Wednesday",
        THURSDAY: "Thursday", FRIDAY: "Friday", SATURDAY: "Saturday", SUNDAY: "Sunday"}


def in_range(date, datetime1, datetime2):
    return date.day >= datetime1.day and date.day <= datetime2.day and \
        date.month >= datetime1.month and date.month <= datetime2.month


def congrats(users):
    congratulations = {}
    for i in range(len(WEEK)):
        congratulations[i] = []

    for user in users:
        if in_range(users[user], current_weekend(), next(FRIDAY)):
            if users[user].weekday() == SATURDAY or users[user].weekday() == SUNDAY:
                congratulations[MONDAY].append(user)
            else:
                congratulations[users[user].weekday()].append(user)
    return congratulations


def listtstr(list):
    out = ""
    for a in list:
        out += str(a) + " "
    return out


def print_congrats(list):
    for day in list:
        if len(list[day]) > 0:
            print(WEEK[day] + " : " + listtstr(list[day]))
    return 0


def get_birthdays_per_week(users):
    print_congrats(congrats(users))
    return 0


if __name__ == "__main__":

    # default values
    number = MAX_EXPECTED  # just default
    filename = "output.txt"
    debug = False

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-n":
            try:
                number = sys.argv[i+1]  # read number of users
            except IndexError:
                print("there is no number written assume number: 100")
        if sys.argv[i] == "-f":
            try:
                filename = sys.argv[i+1]  # read filename
            except IndexError:
                print("there is no filename indicated use: output.txt")
        if sys.argv[i] == "-debug":
            debug = True

    if debug:
        users = list_generator(int(number))  # generate users
        # list of users may conatin less amount than demanded - dictionary limitation
        # for the proper list of users should be generated in other way - not dictionary as name: birthday
        # in this case it is impossible to have two collegues with the similar names but different birth days
        print("#######################################################################################")
        print("###                       RANDOMLY GENERATED LIST                                  ####")
        print("#######################################################################################")
        for val in users:
            print(val + ":" + users[val].date().strftime("%A %d %B %Y"))
        print("#######################################################################################")

        # print(current_weekend().date())
        # print(next(FRIDAY).date())
        # print(congrats(users))
        print("Today is " + str(date.today()))
        print("Next week birthdays have:")
        get_birthdays_per_week(users)

    else:
        print("use -debug flag to try test example")
