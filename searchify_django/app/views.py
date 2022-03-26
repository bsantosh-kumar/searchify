from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import *

import pytesseract    # ======= > Add
try:
    from PIL import Image
except:
    import Image


def index(request) :
    return HttpResponse("Hello, world. You're at the index.")

class HomeView(FormView):
    form_class = UploadForm
    template_name = 'app/index.html'
    success_url = '/'

    # def form_valid(self, form):
    #     upload = self.request.FILES['file']
    #     return super().form_valid(form)
    
    def form_valid(self, form):
        upload = self.request.FILES['file']
        txt = pytesseract.image_to_string(Image.open(upload))
        print("upload = ",upload)
        print(type(txt), txt) # =====> add line
        return super().form_valid(form)
