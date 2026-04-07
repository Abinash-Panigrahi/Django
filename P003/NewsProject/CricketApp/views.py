from django.shortcuts import render,HttpResponse

# Create your views here.

def Cricket_view(request):
        return HttpResponse('<h2><b>Cricket</b> is a bat-and-ball game that is played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps. Two players from the batting team (the striker and nonstriker) stand in front of either wicket, with one player from the fielding team (the bowler) bowling the ball towards the strikers wicket from the opposite end of the pitch. The strikers goal is to hit the bowled ball and then switch places with the nonstriker, with the batting team scoring one run for each exchange. Runs are also scored when the ball reaches or crosses the boundary of the field or when the ball is bowled illegally.</h2>')

def God_of_crciket(request):
        return HttpResponse('<h2><b>Sachin Tendulkar</b>,born 24 April 1973) is an Indian former international cricketer who captained the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket.Hailed as the worlds most prolific batsman of all time, he is the all-time highest run-scorer in both ODI and Test cricket with more than 18,000 runs and 15,000 runs, respectively.He also holds the record for receiving the most player of the match awards in international cricket.Tendulkar was a Member of Parliament, Rajya Sabha by nomination from 2012 to 2018.</h2>')