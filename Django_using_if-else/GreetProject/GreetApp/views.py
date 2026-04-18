from django.shortcuts import render
from datetime import datetime

# Create your views here.

def Greet_views(request):
    current_Time=datetime.now()
    hour=int(current_Time.strftime('%H'))
    if hour>=4 and hour<12:
        wish='Good Morning,'
    elif hour>=12 and hour<16:
        wish='Good After Noon,'
    elif hour>=16 and hour<20:
        wish='Good Evening,'
    else:
        wish='Good Night,'
    d={'wish': wish,'greet': hour}
    return render(request,'GreetApp/greet.html',d)

