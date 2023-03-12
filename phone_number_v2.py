import phonenumbers
from phonenumbers import geocoder

# take phone number input from user
input_number = input("Enter phone number with country code: ")

# parse phone number
pn = phonenumbers.parse(input_number)

# print the country name
print("Country: ", phonenumbers.geocoder.description_for_number(pn, 'en'))

# format phone number in international format
print("International format: ", phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.INTERNATIONAL))

# format phone number in national format
print("National format: ", phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.NATIONAL))

# format phone number in E.164 format
print("E.164 format: ", phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164))

# format phone number in RFC3966 format
print("RFC3966 format: ", phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.RFC3966))
