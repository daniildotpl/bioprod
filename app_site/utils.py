from django.contrib import messages
from django.shortcuts import redirect



class GetGroups:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = [g.name for g in self.request.user.groups.all()]
        return context


class ResoUpdaMixi:
    
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         messages.success(self.request, 'Обновлено')
    #         return self.form_valid(form)
    #     else:
    #         messages.error(self.request, 'Ошибка доступа')
    #         return redirect('somewrong')
    pass
    

# --- Mixin for resources --------------------------
class ResourceEditGetPostMixin:

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.auth.id == self.request.user.id:
            form = self.get_form()
            if form.is_valid():
                messages.success(self.request, 'Обновлено')
                return self.form_valid(form)
            else:
                return redirect('somewrong')
        else:
            return redirect('somewrong')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.auth.id == self.request.user.id:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('somewrong')

class ResourceRemoGetPostMixin:

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        if object.auth.id == self.request.user.id:
            object.dele = True
            object.publ = False
            object.save()
            return redirect('pers') 
        else:        
            return redirect('somewrong')

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if object.auth.id == self.request.user.id:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('somewrong')


# --- Mixin for person -----------------------------
class PersonEditGetPostMixin:

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.id == self.request.user.id:
            form = self.get_form()
            if form.is_valid():
                messages.success(self.request, 'Обновлено')
                return self.form_valid(form)
            else:
                return redirect('somewrong')
        else:
            return redirect('somewrong')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.id == self.request.user.id:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('somewrong')

class PersonRemoGetPostMixin:

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        if object.id == self.request.user.id:
            object.dele = True
            object.is_active = False
            object.save()
            return redirect(self.success_url)
        else:
            return redirect('somewrong')

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if object.id == self.request.user.id:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('somewrong')
