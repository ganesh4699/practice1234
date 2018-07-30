from django.shortcuts import render
from django.http import HttpResponse
from final_application.models import Topic,Webpage,AccessRecord
from . import forms
# Create your views here.
#def index(request):
#    Webpages_list=AccessRecord.objects.order_by('date')
#    date_dict={'accessrecord':Webpages_list}
#   return render(request,'first_template/index.html',context=date_dict)

def index(request):
    return render(request,'first_template/index.html')

def form_name_view(request):
    form=forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("Hey this is successfully validation")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return render(request,'first_template/form_page.html',{'form':form})