import hashlib
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.db.models import *

from .utils import *
from .models import *
from .forms import *
from app_status.models import *
from app_status.utils import *



# --- common ----------------------------------------
class SearResu(ListView):
    template_name = 'app_site/sear_resu.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результат поиска'
        context['quer'] = self.request.GET.get('quer')
        return context

    def get_queryset(self):
        quer = self.request.GET.get('quer')
        q = User.objects.filter(
            Q(titl__icontains=quer) | 
            Q(desc__icontains=quer) |
            Q(cont__icontains=quer), 
            Q(publ=True))
        return q

class Site(TemplateView):
    template_name = 'app_site/start.html'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New service'
        context['data'] = 'New service Home Page'
        return context

class Somewrong(TemplateView):
    template_name = 'app_site/data.html'

    def data(self):
        return 'Что-то пошло не так'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data()
        return context

class Test(TemplateView):
    template_name = 'app_site/data.html'

    def testfun(self):
        return 'Test'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.testfun()
        context['data'] = self.testfun()
        return context


# --- Gete ------------------------------------------
class Lgn(LoginView):
    form_class = LgnForm
    template_name = 'app_site/gate/lgn.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context
    
    def get_success_url(self):
        # url = self.request.GET.get('next')
        # if url:
        #     return url
        # else:
        #     return reverse_lazy('pers')
        return reverse_lazy('pers')

class Lgt(LogoutView):
    template_name = 'app_site/gate/lgt.html'

    def get_success_url(self):
        return reverse_lazy('site')


# --- Register New User -----------------------------
class Regi(CreateView, ResetStatus):
    form_class = RgtForm
    template_name = 'app_site/regi/regi.html'
    success_url = reverse_lazy('regi_done')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация нового пользователя"
        return context

    def form_valid(self, form):
        toem = form.instance.email
        token = self.do_confirm_token(toem)
        form.instance.is_active = False
        form.instance.toke = token
        if form.save():
            res = self.send_confirm_link(toem, token)
            return HttpResponseRedirect(self.success_url)
        else:
            return redirect('somewrong')

    def send_confirm_link(self, toem, token):
        if self.request.is_secure == True:
            prot = 'https://'
        else:
            prot = 'http://'
        link = prot + str(self.request.get_host()) + '/regi_conf/' + token
        subj = 'Подтверждение регистрации. Технологии биоискусственных систем'
        mess = 'Вы зарегистрировалитсь на сайте crm.ru. '
        mess += 'Для подтверждения регистрации пройдите пожалуйста по ссылке ' + link
        frem = 'crm <{}>'.format(settings.EMAIL_HOST_USER)
        result = send_mail(subj, mess, frem, [toem])
        print('send_confirm_link: ', result)
        return result

    def do_confirm_token(self, toem):
        token = toem.replace("@","") 
        token = token.replace(".","") 
        token = hashlib.md5(token.encode('ascii')).hexdigest() 
        return token

class RegiDone(TemplateView):
    template_name = 'app_site/regi/regi_done.html'
    
    def data(self):
        mess = '<p>Вы зарегистрировалитсь на сайте crm.ru.</p>'
        mess += '<p>На указанную почту выслано письмо '
        mess += 'с ссылкой для подтверждения.</p>'
        return mess

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация нового пользователя'
        context['data'] = self.data()
        return context

class RegiConf(TemplateView):
    template_name = 'app_site/regi/regi_conf.html'
    
    def data(self):
        token = self.kwargs['token']
        try: 
            res = User.objects.get(toke=token)
            res.is_active = True
            res.toke = ''
            res.save()
            mess = 'Уважаемый(ая) <b>'
            mess += str(res.username)
            mess += '</b>, Ваша регистрация подтверждена'
        except:
            mess = '<p>Возможно Вы уже активировали ссылку для регистрации или она устарела </p>'
            mess += '<p>Попробуйте зайти на сайт или пройти регистрацию заново</p>'
        return mess

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация подтверждена'
        context['data'] = self.data()
        return context


# --- Reset Password --------------------------------
class Rese(PasswordResetView):
    form_class = ReseForm
    template_name = 'app_site/rese/rese.html'
    success_url = reverse_lazy('rese_done')
    email_template_name = "app_site/rese/rese_form_emai.html"
    from_email = settings.EMAIL_HOST_USER

class ReseDone(PasswordResetDoneView):
    template_name = 'app_site/rese/rese_done.html'

class ReseConf(PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'app_site/rese/rese_conf.html'
    success_url = reverse_lazy('rese_cmpl')

class ReseCmpl(PasswordResetCompleteView):
    template_name = 'app_site/rese/rese_cmpl.html'


# --- Personal User Data ----------------------------
class Pers(LoginRequiredMixin, GetGroups, TemplateView):
    login_url = reverse_lazy('lgn')
    permission_required = 'app_site.view_user'
    template_name = 'app_site/pers/pers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        context['user'] = self.request.user
        # context['user_groups'] = [g for g in self.request.user.groups.all()]
        context['docs'] = Documents.objects.filter(user=self.request.user)
        context['qual'] = Qualifications.objects.filter(user=self.request.user)
        return context

class PersRemo(LoginRequiredMixin, PersonRemoGetPostMixin, DeleteView):
    model = User
    template_name = 'app_site/pers/pers_remo.html'
    pk_url_kwarg = 'user_id'
    success_url = reverse_lazy('site')
    login_url = reverse_lazy('lgn')

class PersUpda(LoginRequiredMixin, PersonEditGetPostMixin, ResetStatus, UpdateView):
    model = User
    form_class = UserFormUpda
    template_name = 'app_site/pers/pers_upda.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'data'
    login_url = reverse_lazy('lgn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактор личных данных'
        return context

    def get_success_url(self):
        return reverse_lazy('pers_upda', args = [self.object.pk])
