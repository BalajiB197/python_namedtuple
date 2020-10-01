from faker import Faker
from collections import namedtuple
from time import perf_counter
from datetime import date 
from pyfaker import Fake
import random 

def dict_approach():
    '''
    method runs for 10k iteration for different fake profiles
    and returns the most common bloodgroup, mean current location, oldest person age
    and the average age.
    This method is executed using dictionary approach.
    '''
    fake = Faker()
    counts, dict1 = dict(), dict()
    mean_loc1, mean_loc2 = 0, 0
    new_age, sum_age = 0, 0

    for i in range(1,10001):
        value = fake.profile()

        blood_group = value['blood_group']
        current_location = value['current_location']
        mean_loc1 = mean_loc1 + current_location[0]
        mean_loc2 = mean_loc2 + current_location[1]
        counts['mean_loc1'], counts['mean_loc2'] = mean_loc1/i, mean_loc2/i
        birthdate = value['birthdate']
        age = date.today().year - birthdate.year
        counts['oldest_age'] = age if age >= new_age else new_age
        sum_age = sum_age + age
        counts['avg_age'] = sum_age/i
        dict1[blood_group] = dict1[blood_group] + 1 if blood_group in dict1 else 1
    counts['blood_group'] = max(dict1)
    return counts

def named_tuple():
    '''
    method runs for 10k iteration for different fake profiles
    and returns the most common bloodgroup, mean current location, oldest person age
    and the average age.
    This method is executed using namedtuple approach.
    '''
    fake = Faker()
    counts = dict()
    
    sum_age, mean_loc1, mean_loc2 = 0, 0, 0
    new_age = 0
    Details = namedtuple('Details', 'blood_group mean_loc1 mean_loc2 oldest_age avg_age')
    
    for i in range(1,10001):
        value = fake.profile()

        blood_group = value['blood_group']
        current_location = value['current_location']
        mean_loc1 = mean_loc1 + current_location[0]
        mean_loc2 = mean_loc2 + current_location[1]
        birthdate = value['birthdate']
        age = date.today().year - birthdate.year
        oldest_age = age if age >= new_age else new_age
        sum_age = sum_age + age
        counts[blood_group] = counts[blood_group] + 1 if blood_group in counts else 1

    dt = Details(max(counts),mean_loc1/i, mean_loc2/i,oldest_age,sum_age/i)
    return dt

def stock_price():
    '''
    generate 100 companies from pyfake library and create a random dataset
    for high, close and open of stock value.
    return - max-high stock price, open-stock price and close-stock price.
    '''
    weights = []
    for _ in range(100):
        weights.append(random.uniform(0.1, 1.0))
    
    fake = Fake(lang_code='en')
    Cmp_Details = namedtuple('Cmp_Details', 'name, symbol, open1, high, close')
    normalised_weights = [i/sum(weights) for i in weights]
    high_cmp = 0

    for i in range(0,100):
        fake_data = fake.Company.bs()
        open1 = random.randrange(300, 1001, 4) * normalised_weights[i]
        high = open1  * random.uniform(1.2, 1.6)
        close = open1 * random.uniform(0.8, 1.0)

        dt = Cmp_Details(fake_data, fake_data[-3:].upper(),open1, high, close)

        if dt.high > high_cmp:
            high_cmp = dt.high
        if i==0:
            open_cmp = dt.open1

    dt = Cmp_Details(fake_data, fake_data[-3:].upper(),open_cmp, high_cmp, dt.close)
    return dt.open1, dt.high, dt.close

# def stock_price():
#     fake = Fake(lang_code='en')
#     weights, open1 =[], []
#     Cmp_Details = namedtuple('Cmp_Details', 'name, symbol, open, high, close')
#     for i in range(1,11):
#         fake_data = fake.Name.name()
#         weights.append(random.uniform(0.1, 1.0))
#         open1.append(random.randrange(0, 1001, 4))
#     normalised_weights = [i/sum(weights) for i in weights]
#     high = [open1[i]*normalised_weights[i]*random.uniform(1.0, 1.4) for i in range(len(open1))]
#     close = [open1[i]*normalised_weights[i]*random.uniform(0.8, 1.0) for i in range(len(open1))]
#     cont_stock = [open1[i]*normalised_weights[i] for i in range(len(normalised_weights))]

#     dt = Cmp_Details(fake_data, fake_data[:3].upper(),int(sum(cont_stock)), int(sum(high)), int(sum(close)))
#     print(type(dt.symbol))
#     return dt