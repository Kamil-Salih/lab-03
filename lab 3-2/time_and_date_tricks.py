import time, datetime

print(time.time())  # current Unix timestamp

print(datetime.datetime.now())
print(datetime.datetime(2025, 10, 12, 14, 45, 2))
print(datetime.datetime.fromtimestamp(1700000000))
print(datetime.datetime(2023, 11, 14, 22, 13, 20))

print("\n")

'''
Exercise:
Convert your birthday to a Unix timestamp.

Convert 1700000000 back to a readable date.

'''

birthday= datetime.datetime(2006, 6, 11, 0, 0, 0)
print(birthday.timestamp())

print(datetime.datetime.fromtimestamp(1700000000))