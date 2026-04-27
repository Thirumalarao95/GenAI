#Task 1
from package.math_utils import *
print(add(4,5))
print(substract(10,2))
print(square(5))

# Task 2
from package.string_utils import *
text = 'Hi hello this is teja how are you'
print(capitalize_words(text))
print(revesre_string(text))
print(word_count(text))

# Task 3

from Shop_package.billing import *
print(apply_tax(500))
print(calculate_total([100,200,300]))

# Task 4:
import Shop_package.discount as disc
from Shop_package.billing import calculate_total 
print(disc.apply_discount(1000,10))
print(calculate_total([100,200,300,500]))
print(apply_tax(2500))
print(disc.flat_discount(500))
