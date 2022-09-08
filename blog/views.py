def post_list(request):
    return render(request, 'blog/post_list.html', {})
from django.shortcuts import render

def display(request):
    return render(request, 'template.tmpl', {'obj':models.Book.objects.all()})
