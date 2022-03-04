
from faker import Faker

fake = Faker(locale='en_CA')
adshop_url = 'https://advantageonlineshopping.com/#/'
my_account_url = 'https://advantageonlineshopping.com/#/myAccount'
new_username = fake.user_name()
if len(new_username) > 15:
    new_username = new_username[0:14]
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
country = fake.country()
address = fake.street_address()
phone = fake.phone_number()
province = fake.province_abbr()
postal_code = fake.postcode()
description = fake.sentence(nb_words=100)




