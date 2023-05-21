from time import gmtime, strftime
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView
from django.urls.base import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.utils.translation import gettext as _

from app_site.models import User
from .models import *
from .forms import *
from app_site.utils import *


class LocaList(LoginRequiredMixin, ListView):
    model = Locations
    template_name = 'app_rearward/loca_list.html'
    context_object_name = 'data'
    success_url = reverse_lazy('loca_list')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список локаций'
        return context

class LocaCrea(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app_rearward.add_locations'
    form_class = LocaForm
    template_name = 'app_rearward/loca_crea.html'
    success_url = reverse_lazy('loca_list')
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Добавить локацийю')
        context['auth'] = self.request.user
        context['date'] = strftime("%d.%m.%Y", gmtime())
        return context

    def form_valid(self, form):
        # form.instance.user = self.request.user
        # --- отсылка письма админу ---
        # self.send('Добавлена статья "{}"'.format(form.instance.titl))
        return super().form_valid(form)

class LocaUpda(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app_rearward.change_locations'
    model = Locations
    form_class = LocaForm
    template_name = 'app_rearward/loca_upda.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор локаций'
        return context

    def get_success_url(self):
        return reverse_lazy('loca_upda', args = [self.object.pk])  

class LocaRemo(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app_rearward.delete_locations'
    model = Locations
    template_name = 'app_site/obje_remo.html'
    success_url = reverse_lazy('loca_list')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Удаление объекта №') + ' ' + str(context['object'].pk)
        return context



class FaksList(LoginRequiredMixin, ListView):
    model = Faks
    template_name = 'app_rearward/faks_list.html'
    context_object_name = 'data'
    success_url = reverse_lazy('faks_list')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список аптечек'
        return context

class FaksCrea(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app_rearward.add_faks'
    form_class = FaksForm
    template_name = 'app_rearward/faks_crea.html'
    success_url = reverse_lazy('faks_list')
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Добавить аптечку')
        context['auth'] = self.request.user
        context['date'] = strftime("%d.%m.%Y", gmtime())
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        # --- отсылка письма админу ---
        # self.send('Добавлена статья "{}"'.format(form.instance.titl))
        return super().form_valid(form)

class FaksUpda(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app_rearward.change_faks'
    model = Faks
    form_class = FaksForm
    template_name = 'app_rearward/faks_upda.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор аптечек'
        context['medi'] = Medicines.objects.filter(faks=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('faks_upda', args = [self.object.pk])  
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        medi_pk = self.request.POST.get('faks')
        print(medi_pk)

        medi = Medicines.objects.get(pk=medi_pk)
        medi.faks = self.object
        medi.save()

        # --- отсылка письма админу ---
        # self.send('Добавлена статья "{}"'.format(form.instance.titl))
        return super().form_valid(form)

class FaksRemo(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app_rearward.delete_faks'
    model = Faks
    template_name = 'app_site/obje_remo.html'
    success_url = reverse_lazy('faks_list')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Удаление объекта №') + ' ' + str(context['object'].pk)
        return context


# class FaksUpdaMedi(LoginRequiredMixin, PermissionRequiredMixin, FormView):
#     permission_required = 'app_rearward.change_faks'
    
#     form_class = FaksUpdaMediForm
#     template_name = 'app_rearward/faks_upda_medi.html'
#     context_object_name = 'data'
#     login_url = reverse_lazy('lgn')

#     def faks_pk(self):
#         return self.request.resolver_match.kwargs['pk']


#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Редактор аптечек'
#         return context

#     def get_success_url(self):
#         return reverse_lazy('faks_upda', args = [self.faks_pk()])  
    
#     def form_valid(self, form):
#         print(form.instance)

#         medi_pk = form.instance

#         medi = Medicines.objects.get(pk=medi_pk)
#         medi.faks = Faks.objects.get(pk=self.faks_pk())
#         medi.save()

        
        
#         form.instance.user = self.request.user
#         # --- отсылка письма админу ---
#         # self.send('Добавлена статья "{}"'.format(form.instance.titl))
#         return super().form_valid(form)



class MediList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'app_rearward.view_medicines'
    model = Medicines
    template_name = 'app_rearward/medi_list.html'
    context_object_name = 'data'
    success_url = reverse_lazy('medi_list')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список препаратов'
        return context

class MediCrea(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app_rearward.add_medicines'
    form_class = MediForm
    template_name = 'app_rearward/medi_crea.html'
    success_url = reverse_lazy('medi_list')
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Добавить препарат')
        context['auth'] = self.request.user
        context['date'] = strftime("%d.%m.%Y", gmtime())
        return context

    def form_valid(self, form):
        # form.instance.user = self.request.user
        # --- отсылка письма админу ---
        # self.send('Добавлена статья "{}"'.format(form.instance.titl))
        return super().form_valid(form)

class MediUpda(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app_rearward.change_medicines'
    model = Medicines
    form_class = MediForm
    template_name = 'app_rearward/medi_upda.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор препарата'
        return context

    def get_success_url(self):
        return reverse_lazy('medi_upda', args = [self.object.pk])  

class MediRemo(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app_rearward.delete_medicines'
    model = Medicines
    template_name = 'app_site/obje_remo.html'
    success_url = reverse_lazy('medi_list')
    login_url = reverse_lazy('lgn')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Удаление объекта №') + ' ' + str(context['object'].pk)
        return context
