from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *



class HomeView(View):
    def get(self, request):
        statuses=Task.Statuschoices.choices
        tasks=Task.objects.order_by('-status', 'deadline')
        context={
            'statuses':statuses,
            'tasks':tasks
        }

        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            details=request.POST['details'],
            deadline=request.POST['deadline'] if request.POST['deadline'] else None,
            status=request.POST['status']
        )
        return redirect('home')


class TaskEditView(View):
    def get(self, request, pk):
        task=get_object_or_404(Task, pk=pk)
        context={
            'task':task,
        }
        return render(request, 'edit.html', context)
    def post(self, request, pk):
        task=get_object_or_404(Task, pk=pk)
        task.title=request.POST['title']
        task.details = request.POST['details']
        task.status = request.POST['status']
        task.deadline=request.POST['deadline']  if request.POST['deadline'] else None
        task.save()
        return redirect('home')


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'delete_confirm.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('home')