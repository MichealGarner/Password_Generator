#!/usr/bin/env python3

''' NOTE: Just another password generator.
    This program was written by Micheal Garner from examples taken across the
    internet. '''

import string
from random import *

# This creates the type of characters used in the password.
characters = string.ascii_letters + string.punctuation  + string.digits
# This creates the password.
password =  "".join(choice(characters) for x in range(randint(16, 18)))
# adjust passowrd length by varying randint (shortest, longest)

print (password)
