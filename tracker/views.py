from django.shortcuts import render

# Create your views here.
def index(request):
    # projects = Project.get_all_projects()
    # locations = Location.objects.all()
    title = 'O_world'
    return render(request, 'index.html', )
