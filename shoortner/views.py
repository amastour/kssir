from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import *

from shoortner.forms import *
from shoortner.models import *
from analytics.models import *


# Create your views here.

'''def kssir_redirect_view(request,shortcode=None, *args, **kwargs): # function base view FBV
    #print(request.user)
    #print(request.user.is_authenticated())
    print(shortcode)

    obj = get_object_or_404(KssirURL,shortcode__exact=shortcode)
    return redirect("{shortcode}".format(shortcode=obj.url))'''


class HomeView(View):
    def get(self,request, *args, **kwargs):
        form = URLForm()
        bg_image = "https://upload.wikimedia.org/wikipedia/commons/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg"
        return render(request,"index.html",{"form":form,"title":"Kss.ir","bg_image":bg_image})
    
    def post(self,request, *args, **kwargs):
        form = URLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_url = form.cleaned_data.get("url")
            obj,created = KssirURL.objects.get_or_create(url=new_url)
            new = {
                "object":obj,
                "created":created,
            }
            if created:
                return render(request,"success.html",new)
            else :
                return render(request,"already_exists.html",new)

        return render(request,"index.html",{"form":form,"title":"Kss.ir"})



class URLRedirectView(View): # Class Base View
    def get(self,request,shortcode, *args, **kwargs):
        print(shortcode)
        obj = get_object_or_404(KssirURL,shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return redirect(u"{shortcode}".format(shortcode=obj.url))
