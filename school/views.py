from django.shortcuts import render

# Create your views here.
from . import models
from .permission import check_permission
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
@check_permission
def students(request):
    students_obj = models.Student.objects.all()
    username = request.user.username
    return render(request, 'students_list.html', {'students_obj':students_obj,'username':username})