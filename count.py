def count_upc(word):
    return sum([1 for letter in word if letter.isupper()])
    
assert count_upc("") == 0, 'Empty string'
assert count_upc("A") == 1, 'One upper case'
assert count_upc("AA") == 2, 'Two upper case'
assert count_upc("a") == 0, 'One lower case'
assert count_upc("A$#dwTr") == 2, 'Two upper case'
assert count_upc("$%#@%") == 0, 'Special characters'
assert count_upc("AbcDeF") != len("AbcDeF") , '3 upper case'

print("All tests passed!")