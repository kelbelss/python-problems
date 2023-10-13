mult_5 = 0
list_5 = []

while mult_5 < 995:
    mult_5 += 5 
    list_5.append(mult_5)

# print(list_5)



mult_3 = 0
list_3 = []

while mult_3 < 999:
  mult_3 += 3
  if mult_3 != list:
     list_3.append(mult_3)



filtered_list = []
for x in list_3:
  if (x % 5 != 0):
    filtered_list.append(x)

# filtered_list = [x for x in numbers if x % 5 != 0]

# print(filtered_list)
  


answ1 = sum(list_5)
answ2 = sum(filtered_list)

final_answer = answ1 + answ2
print(final_answer)