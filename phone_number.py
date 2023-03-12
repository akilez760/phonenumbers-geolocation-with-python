import phonenumbers
from phonenumbers import geocoder

# phone number with country code
pn1 = phonenumbers.parse('+12136574429')
pn2 = phonenumbers.parse('+917294536271')
pn3 = phonenumbers.parse('+862234567890')
pn4 = phonenumbers.parse('+201234567890')
pn5 = phonenumbers.parse('+923214296518')

# print the country name
print(geocoder.description_for_number(pn1, 'en'))
print(geocoder.description_for_number(pn2, 'en'))
print(geocoder.description_for_number(pn3, 'en'))
print(geocoder.description_for_number(pn4, 'en'))
print(geocoder.description_for_number(pn5, 'en'))