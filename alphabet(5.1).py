def count_characters(text):
 
  char_counts = {}
  for char in text:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

 
  sorted_char_counts = dict(sorted(char_counts.items()))  
  return sorted_char_counts
my_string = "My laba 5!"
result = count_characters(my_string)

for char, count in result.items():
  print(f"'{char}': {count}")


empty_string = ""
result_empty = count_characters(empty_string)
print(result_empty) 