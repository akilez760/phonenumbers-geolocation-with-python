import phonenumbers

# phone number with country code
pn = phonenumbers.parse('+923211234567')

# format phone number in international format
print(phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.INTERNATIONAL))

# format phone number in national format
print(phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.NATIONAL))

# format phone number in E.164 format
print(phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164))

# format phone number in RFC3966 format
print(phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.RFC3966))
