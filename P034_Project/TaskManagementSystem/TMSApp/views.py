from django.shortcuts import render,redirect,get_object_or_404
from .models import TMSModels
from datetime import datetime


# Create your views here.


def home_view(request):
    incomplete_task=TMSModels.objects.filter(task_status=False)
    complete_task=TMSModels.objects.filter(task_status=True)
    len_incomplete_task=len(incomplete_task) 
    len_completed_task=len(complete_task)
    current_datetime = datetime.now()

    progress_bar=TMSModels.objects.all().count()
    if progress_bar > 0:
        progress=(len_completed_task/progress_bar)*100
    else:
        progress=0
    context={
        'incomplete_task':incomplete_task,
        'complete_task':complete_task,
        'len_incomplete_task':len_incomplete_task,
        'len_completed_task':len_completed_task,
        'current_datetime':current_datetime,
        'progress':progress
    }
    return render(request,'TMSApp/home.html',context)


def add_task_view(request):
    task_name=request.POST['add_task']
    TMSModels.objects.create(task_name=task_name)
    return redirect('home')


def done_task_view(request,id):
    task_name=get_object_or_404(TMSModels,id=id)
    task_name.task_status=True
    task_name.save()
    return redirect('home')


def delete_task_view(request,id):
    task_name=get_object_or_404(TMSModels,id=id)
    task_name.delete()
    return redirect('home')


def undo_task_view(request,id):
    task_name=get_object_or_404(TMSModels,id=id)
    task_name.task_status=False
    task_name.save()
    return redirect('home')


# def undo_all_complete_task(request):
#     complete_task =TMSModels.objects.filter(task_status=False) 
#     complete_task.update(task_status=True)
#     complete_task.save()
#     return redirect('home')


def delete_all_incomplete_task(request):
    incomplete_task=TMSModels.objects.filter(task_status=False)
    incomplete_task.delete()
    return redirect('home')


def clear_all_complete_task(request):
    incomplete_task =TMSModels.objects.filter(task_status=True) 
    incomplete_task.delete() 
    return redirect('home')


def clear_total_records_view(request):
    all_records=TMSModels.objects.all()
    all_records.delete()
    return redirect('home')


def update_task_view(request,id):
    if request.method=='POST':
        updated_task=request.POST['update_task']
        record=get_object_or_404(TMSModels,id=id)
        record.task_name=updated_task
        record.save()
        return redirect('home')
    else:
        record=get_object_or_404(TMSModels,id=id)
        context={
            'record':record
        }
        return render(request,'TMSApp/update.html',context)