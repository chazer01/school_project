from django.shortcuts import render, redirect, get_object_or_404
from .models import Groups


def home(request):
    return render(request, 'index.html')


def group_list(request):
    group = Groups.objects.all()
    ctx = {'group': group}
    return render(request, 'school/groups-list.html', ctx)


def group_create(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_type = request.POST.get('group_type')
        if (group_name
                and group_type):
            Groups.objects.create(
                group_name=group_name,
                group_type=group_type,
            )
            return redirect('groups:list')
    return render(request, 'school/groups-form.html')


def group_detail(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    ctx = {'group': group}
    return render(request, 'school/groups-detail.html', ctx)


def group_delete(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    group.delete()
    return redirect('groups:list')

