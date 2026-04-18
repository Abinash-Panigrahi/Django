from django.shortcuts import render, redirect
from .forms import ResumeFormPart1, ResumeFormPart2
from .models import Resume

def create_resume_part1(request):
    if request.method == 'POST':
        form = ResumeFormPart1(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            request.session['resume_id'] = resume.id
            return redirect('resume_part2')
    else:
        form = ResumeFormPart1()
    return render(request, 'ORBApp/resume_part1.html', {'form': form})

def create_resume_part2(request):
    resume_id = request.session.get('resume_id')
    if not resume_id:
        return redirect('resume_part1')
    resume = Resume.objects.get(id=resume_id)
    if request.method == 'POST':
        form = ResumeFormPart2(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_done', resume_id=resume.id)
    else:
        form = ResumeFormPart2(instance=resume)
    return render(request, 'ORBApp/resume_part2.html', {'form': form})

def resume_done(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'ORBApp/resume_done.html', {'resume': resume})
