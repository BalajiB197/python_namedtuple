from faker import Faker
from time import perf_counter
from datetime import date 

fake = Faker()
counts = dict()
start = perf_counter()
sum_age, mean_loc1, mean_loc2 = 0, 0, 0
new_age = 0

for i in range(1,11):
    value = fake.profile()

    blood_group = value['blood_group']
    current_location = value['current_location']
    mean_loc1 = mean_loc1 + current_location[0]
    mean_loc2 = mean_loc2 + current_location[1]
    mean_loc1, mean_loc2 = mean_loc1/i, mean_loc2/i
    birthdate = value['birthdate']
    age = date.today().year - birthdate.year
    oldest_age = age if age >= new_age else new_age
    sum_age = sum_age + age
    avg_age = sum_age/i
    counts[blood_group] = counts[blood_group] + 1 if blood_group in counts else 1

end = perf_counter()
elapsed = end - start
print('Run time: {0:.6f}s'.format(elapsed))
print(counts)
print('Avg age:', avg_age)
print('Oldest age:', oldest_age)
print('Mean location:', mean_loc1, mean_loc2)