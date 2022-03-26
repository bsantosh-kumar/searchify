from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import *

import pytesseract    # ======= > Add
from PIL import Image


def index(request) :
    return HttpResponse("Hello, world. You're at the index.")

def extractWordsFromImage(image) :
    txt = pytesseract.image_to_string(Image.open(image))
    return txt

def split_string(txt) :
    import re
    txt = txt.lower()
    txt = re.sub(r'[^\w\s]',' ',txt)
    txt = re.sub(r'\s+',' ',txt)
    return txt.split()
    
class HomeView(FormView):
    form_class = UploadForm
    template_name = 'app/index.html'
    success_url = '/'
    
    def form_valid(self, form):
        upload = self.request.FILES['file']
        print("upload = ",upload)
        file_type = upload.content_type
        print("file_type = ",file_type)
        
        words = []

        if(file_type.endswith(('jpeg','png'))):
            # txt = extractWordsFromImage(upload)
            # words = split_string(txt)
            # print(words)
            print('image')
        else :
            print("not image")
        # if(file_type == 'image/jpeg' or file_type == 'image/png' or file_type == 'image/jpg'):
        #     txt = extractWordsFromImage(upload)
        #     words = split_string(txt)
        #     print(words)
        # else :
        #     print("not image")

        # remove all stop words after extracting from any kind of file
        
        return super().form_valid(form)
