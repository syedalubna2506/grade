def calculate_gradie(marks): 
   if marks >= 90: 
       return "A" 
   elif marks >= 70: 
       return "B" 
   elif marks >= 60: 
       return "C" 
   else: 
       return "F" 
 
print(calculate_grade(85))
