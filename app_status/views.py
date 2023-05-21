# import re
import os
from django.forms.models import BaseModelForm
from django.http import HttpResponse
import qrcode
import hashlib

from time import gmtime, strftime
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls.base import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.utils.translation import gettext as _

from app_site.models import User
from .models import *
from .forms import *
from .utils import *



class StatList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'app_status.view_status'
    model = Status
    template_name = 'app_status/stat_list.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список личного состава'
        context['perm'] = self.request.user.get_group_permissions()
        return context

class StatUpda(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app_status.change_status'
    model = Status
    form_class = StatusForm
    template_name = 'app_status/stat_upda.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор статуса пользователя'
        context['docs'] = Documents.objects.filter(user=self.get_object().user)
        context['qual'] = Qualifications.objects.filter(user=self.get_object().user)
        return context

    def get_success_url(self):
        return reverse_lazy('stat_list')
    
    def form_valid(self, form):
        out = ''
        docs = Documents.objects.filter(user=self.get_object().user)
        for d in docs:
            out += d.titl
            out += d.seri
            out += d.numb
        qual = Qualifications.objects.filter(user=self.get_object().user)
        for q in qual:
            out += q.titl
            out += q.seri
            out += q.numb
        hash = hashlib.sha1(out.encode())
        hash = hash.hexdigest()
        form.instance.hash = hash
        return super().form_valid(form)


class DocsCrea(LoginRequiredMixin, PermissionRequiredMixin, ResetStatus, CreateView):
    permission_required = 'app_status.add_documents'
    form_class = DocumentsForm
    template_name = 'app_status/docs_crea.html'
    success_url = reverse_lazy('pers')
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Добавить документ')
        context['auth'] = self.request.user
        context['date'] = strftime("%d.%m.%Y", gmtime())
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        # --- отсылка письма админу ---
        # self.send('Добавлена статья "{}"'.format(form.instance.titl))
        return super().form_valid(form)

class DocsUpda(LoginRequiredMixin, PermissionRequiredMixin, ResetStatus, UpdateView):
    permission_required = 'app_status.change_documents'
    model = Documents
    form_class = DocumentsForm
    template_name = 'app_status/docs_upda.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор документов пользователя'
        return context

    def get_success_url(self):
        return reverse_lazy('docs_upda', args = [self.object.pk])  

class DocsRemo(LoginRequiredMixin, PermissionRequiredMixin, ResetStatus, DeleteView):
    permission_required = 'app_status.delete_documents'
    model = Documents
    template_name = 'app_site/obje_remo.html'
    success_url = reverse_lazy('pers')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Удаление объекта №') + ' ' + str(context['object'].pk)
        return context


class QualCrea(LoginRequiredMixin, PermissionRequiredMixin, ResetStatus, CreateView):
    permission_required = 'app_status.add_qualifications'
    form_class = QualificationsForm
    template_name = 'app_status/docs_crea.html'
    success_url = reverse_lazy('pers')
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Добавить документ обобразовании')
        context['auth'] = self.request.user
        context['date'] = strftime("%d.%m.%Y", gmtime())
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        # --- отсылка письма админу ---
        # self.send('Добавлена статья "{}"'.format(form.instance.titl))
        return super().form_valid(form)

class QualUpda(LoginRequiredMixin, PermissionRequiredMixin, ResetStatus, UpdateView):
    permission_required = 'app_status.change_qualifications'
    model = Qualifications
    form_class = QualificationsForm
    template_name = 'app_status/qual_upda.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор квалификаций пользователя'
        return context

    def get_success_url(self):
        return reverse_lazy('qual_upda', args = [self.object.pk])
    
class QualRemo(LoginRequiredMixin, PermissionRequiredMixin, ResetStatus, DeleteView):
    permission_required = 'app_status.delete_qualifications'
    model = Qualifications
    template_name = 'app_site/obje_remo.html'
    success_url = reverse_lazy('pers')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Удаление объекта №') + ' ' + str(context['object'].pk)
        return context
















    # def qr_gen(self):
    #     path = settings.MEDIA_ROOT+str(self.request.user.pk)+'/'
    #     if not os.path.exists(path):
    #         os.mkdir(path)
    #     file_url = path+'qr.png'
    #     img = qrcode.make(self.request.user.email)
    #     img.save(file_url)
    #     return str(self.request.user.pk)+'/'+'qr.png'

    # def form_valid(self, form):
        # qr_url = self.qr_gen()
        # print("qr_url: {}".format(qr_url))
        # form.instance.qrco = qr_url
        # print(form.cleaned_data)
        # return super().form_valid(form)








