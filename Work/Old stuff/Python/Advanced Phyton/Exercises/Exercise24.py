def analiza_string(word):
   rechnik={"soglaski": 0, "samoglaski": 0, "cifri": 0, "karakteri": 0}
   samoglaski = ['a', 'e', 'i', 'o', 'u']
   for z in word:
       if z.isalpha():
           if z in samoglaski:
               rechnik["samoglaski"] += 1
           else:
               rechnik["soglaski"] += 1
       elif z.isdigit():
           rechnik["cifri"] += 1
       else:
           rechnik["karakteri"] += 1
   return rechnik
print(analiza_string("1234asdfg!"))
print(analiza_string("aaaa!"))
print(analiza_string("12"))
print(analiza_string("tsjkl"))


