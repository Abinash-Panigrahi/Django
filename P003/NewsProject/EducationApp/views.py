from django.shortcuts import render,HttpResponse

# Create your views here.

def Education_view(request):
     return HttpResponse('<h1><b>Education</b> is the transmission of knowledge, skills, and character traits and manifests in various forms. Formal education occurs within a structured institutional framework, such as public schools, following a curriculum. Non-formal education also follows a structured approach but occurs outside the formal schooling system, while informal education entails unstructured learning through daily experiences.</h1>')

def Now_a_days_Education_system(request):
     return HttpResponse('<h2>Rooted in the ancient learnings of Vedas and Puranas, the <b>Indian education system</b> has come a long way from the old-school Gurukuls to the new-age hi-tech academic institutions. Though the constitution of India primarily gave the authority of the educational apparatus of the country to the state, the introduction of a constitutional amendment in 1976 added the role of the national government for suggesting school education policies and programmes with the state still having some freedom over the implementation of programs.</h2>')

