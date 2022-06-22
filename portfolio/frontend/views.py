from django.shortcuts import render
from django.views import View


class indexView(View):
   def get(self, request):
      template_name = 'website/index.html'
      return render(request, template_name)
