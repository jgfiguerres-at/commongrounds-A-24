from django.shortcuts import render

def project_list(request):
    return render(request, 'diyprojects/projects_list.html')

def project_detail(request, id):
    return render(request, 'diyprojects/project_detail.html')
