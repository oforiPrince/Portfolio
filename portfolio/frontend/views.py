from multiprocessing import context
from django.shortcuts import render
from django.views import View
from backend.models import *
from accounts.models import User

class indexView(View):
   def get(self, request):
      template_name = 'website/index.html'
      user = User.objects.all().first()
      resumes = Resume.objects.all()
      certificates = Certificate.objects.all()
      knowledges = Knowledge.objects.all()
      context = {
         'user': user,
         'resumes': resumes,
         'certificates': certificates,
         'knowledges': knowledges
      }
      return render(request, template_name,context)
