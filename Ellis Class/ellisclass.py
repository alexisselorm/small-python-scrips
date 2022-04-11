def add(x, y):
    c = x+y
    print(c)


# add(344, 566)
# add(412, 655)
# add(4, 86)
# add(4, 5)


def month_days(month):
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
        print(31)
    elif month == "September" or month == "April" or month == "June" or month == "November":
        print(30)
    elif month == "February":
        print(28)
    else:
        print("no answer")


month_days("January")
month_days("February")
month_days("March")
month_days("April")
month_days("May")
month_days("June")
month_days("July")
month_days("August")
month_days("September")
month_days("October")
month_days("November")
month_days("December")
month_days("Ocansey")


# Lists and Dictionaries
countries = ["Ghana", "Mali", "Togo"]
print(countries)
# Adding to a list
countries.append("Rwanda")
countries.append("Seychelles")
countries.append("Nigeria")
print(countries)

countries = ["Ghana", "Mali", "Togo"]
for country in countries:
    print(country)
i = 2
while i > 0:
    print(countries[i])
    i -= 1


hunnid_list = []
for hunnid in range(0, 101):
    hunnid_list.append(hunnid)
    hunnid += 1

print(hunnid_list)


country_capitals = {"Ghana": "Accra", "Togo": "Lome", "USA": "Washington DC",
                    "Canada": "Ottawa", "Sweden": "Stockholm", "Nigeria": "Abuja"}
print(country_capitals)
country_capitals["England"] = "London"
for key, value in country_capitals.items():
    print(f"The capital of {key} is {value}")

odd_hunnid_list = []
for hunnid in range(1, 101, 2):
    odd_hunnid_list.append(hunnid)
    hunnid += 1

print(odd_hunnid_list)


def add_list():
    len_list = int(input("How long is the list: "))
    empty = []
    for number in range(len_list):
        numbers = int(input("Please enter a number: "))
        empty.append(numbers)
    print("The sum of the list is ", sum(empty))


add_list()
