import time
Hour = int(time.strftime('%H'))
if(5<=Hour<12):
 print("Good Morning")
elif(12<=Hour<17):
 print("Good Afternoon")
elif(17<=Hour<21):
 print("Good Evening")
else:
 print("Good Night")
 