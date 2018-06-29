import pytz
import datetime

country = "Europe/Moscow"

tz = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz)

print("The time in {} is {}".format(country, local_time))
print("UTC is {}.".format(datetime.datetime.utcnow()))

# # list out every timezone
# for i in pytz.all_timezones:
#     print(i)
#
# # sorted country codes and full names
# for i in sorted(pytz.country_names):
#     print(i + ": " + pytz.country_names[i])

# # country codes, full name, timezone
# for i in sorted(pytz.country_names):
#     # using .get() will return none if country code doesn't have tz info
#     # otherwise would crash
#     print("{}: {}: {}".format(i, pytz.country_names[i], pytz.country_timezones.get(i)))

for i in sorted(pytz.country_names):
    print("{} ({})".format(i, pytz.country_names[i]), end=": ")
    if i in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[i]):
            tz = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo TZ defined.")
