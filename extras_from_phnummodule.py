import phonenumbers

z = phonenumbers.parse("+120012301", None)
print(z)
# Country Code: 1 National Number: 20012301 Leading Zero: False
phonenumbers.is_possible_number(z)  # too few digits for USA
# False
phonenumbers.is_valid_number(z)
# False
z = phonenumbers.parse("+12001230101", None)
print(z)
# Country Code: 1 National Number: 2001230101 Leading Zero: False
phonenumbers.is_possible_number(z)
# True
phonenumbers.is_valid_number(z)  # NPA 200 not used
# False

z = phonenumbers.parse("02081234567", None)  # no region, no + => unparseable
# Traceback (most recent call last):
# File "phonenumbers/phonenumberutil.py", line 2350, in parse
    # "Missing or invalid default region.")
phonenumbers.phonenumberutil.NumberParseException: #(0) Missing or invalid default region.
z = phonenumbers.parse("gibberish", None)
# Traceback (most recent call last):
#   File "phonenumbers/phonenumberutil.py", line 2344, in parse
    # "The string supplied did not seem to be a phone number.")

phonenumbers.phonenumberutil.NumberParseException: #(1) The string supplied did not seem to be a phone number.


# formatting numbers
phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
# '020 8366 1177'
phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
# '+44 20 8366 1177'
phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
# '+442083661177'


