import keyword
import re
from typing import Counter
# What is the most frequent word in the following paragraph?

paragraph = " I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
reg_ex = r"\w+"
resultado = re.findall(reg_ex, paragraph.lower())
counter = Counter(resultado)
resultado_final = sorted(((counter, resultado) for resultado, counter in counter.items()), reverse=True)
print(resultado_final)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
# Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
points_str = " ".join(points) 
extracted_numbers = list(map(int, re.findall(r"-?\d+",points_str))) 
distance =  max(extracted_numbers) - min(extracted_numbers)
print(distance)
# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(variable):
    return bool(re.fullmatch(r"^[A-Za-z_][A-Za-z0-9_]*$", variable) and variable not in keyword.kwlist)

print(is_valid_variable("pass"))    # False, es palabra reservada
print(is_valid_variable("my_var"))  # True
print(is_valid_variable("_hidden")) # True
print(is_valid_variable("2bad"))    #False

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r"[%#@$&;]", "", text)


print(clean_text(sentence));

def most_frequent_words(text, n=3):
    sentencia_limpia = clean_text(text).split()
    counter = Counter(sentencia_limpia)
    return counter.most_common(n)

# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(sentence, 3)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]