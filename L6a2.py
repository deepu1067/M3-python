import random
import datetime

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2026, 12, 31)

days = (end_date - start_date).days

random_date = start_date + datetime.timedelta(
    days=random.randint(0, days)
)

print("Random Date:", random_date)