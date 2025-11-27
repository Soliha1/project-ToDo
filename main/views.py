from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        statuses=Task.Statuschoices.choices
        tasks=Task.objects.filter(user=request.user).order_by('-status', 'deadline')
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
            status=request.POST['status'],
            user=request.user
        )
        return redirect('home')


class TaskEditView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        task=get_object_or_404(Task, pk=pk, user=request.user)
        context={
            'task':task,
        }
        return render(request, 'edit.html', context)
    def post(self, request, pk):
        task=get_object_or_404(Task, pk=pk, user=request.user)
        task.title=request.POST['title']
        task.details = request.POST['details']
        task.status = request.POST['status']
        task.deadline=request.POST['deadline']  if request.POST['deadline'] else None
        task.save()
        return redirect('home')


class TaskDeleteView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, ):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        return render(request, 'delete_confirm.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return redirect('home')