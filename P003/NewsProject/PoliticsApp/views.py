from django.shortcuts import render,HttpResponse

# Create your views here.

def Politics_view(request):
    return HttpResponse('<h3><b>Politics</b> (from Ancient Greek πολιτικά (politiká) affairs of the cities) is the set of activities that are associated with making decisions in groups, or other forms of power relations among individuals, such as the distribution of resources or status. The branch of social science that studies politics and government is referred to as political science.</h3>')

def CM(request):
    return HttpResponse('<h2><b>Naveen Patnaik</b>,born 16 October 1946) is an Indian statesman, politician and writer serving as the current and 15th Chief Minister of Odisha representing the Hinjili Assembly constituency since 2000. He is the longest-serving chief minister of Odisha and as of 2024, the 2nd longest-serving chief minister of any Indian state, holding the post for over two decades, and only the second Indian chief Minister after Pawan Chamling to win five consecutive terms as Chief Minister of an Indian state.[1][2] He is the first president of the Biju Janata Dal since 1997.[3] He served as the Union Minister of Steel and Mines from 1998 to 2000 and a member of the Lok Sabha from Aska from 1997 to 2000.</h2>')

def PM(request):
    return HttpResponse('<h2><b>Narendra Damodardas Modi</b> (Gujarati:born 17 September 1950)[b] is an Indian politician who has served as the 14th prime minister of India since May 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister from outside the Indian National Congress.</h2>')