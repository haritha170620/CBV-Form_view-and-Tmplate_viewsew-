from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class TempDataRender(TemplateView):
    template_name='TempDataRender.html'
    def get_content_data(self,**kwargs):
        ECDO=super().get_content_data(**kwargs)
        ECDO['name']='haritha'
        return ECDO


class TempInsertData(TemplateView):
    template_name='TempInsertData.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('TempInsertData')

class StudentFormViewInsert(FormView):
    template_name='StudentFormViewInsert.html'
    form_class=StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('StudentFormViewInsert')