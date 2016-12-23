from django.shortcuts import render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from upload.forms import ImageUploadForm
from upload.models import Photos, Thumbnail

class UploadPic(View):
    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = Photos()
            img.photo = form.cleaned_data['image']
            img.save()
            return HttpResponse('image upload success')

class Home(View):
    def get(self, request):
        return render_to_response('home.html')
