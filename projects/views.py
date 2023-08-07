from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import search_projects, paginate_projects
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from .models import Project


def projects(request):
    projects, search_query = search_projects(request)

    custom_range, projects = paginate_projects(request, projects, 6)

    context = {'projects': projects, 'search_query': search_query,
    'custom_range': custom_range}

    return render(request, 'projects.html', context)

def project(request, index):
    project = Project.objects.get(id=index)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()

            project.get_vote_count

            messages.success(request, 'Your review was Successfully Sent.')

    tags = project.tags.all()
    context = {'project': project, 'tags': tags, 'form': form}
    return render(request, 'single-project.html', context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, "project_form.html", context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk) 
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'project_form.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
        
    context = {'object': project}
    return render(request, 'delete_template.html', context)