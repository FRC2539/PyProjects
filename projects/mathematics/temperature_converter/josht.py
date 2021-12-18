def convert(celcius):
   if type(celcius) != int:
       return
   
   
   farenheit = celcius * 9/5 + 32
   return farenheit
   
   
print(convert(-40))
