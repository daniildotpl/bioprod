from .models import *


class ResetStatus:
    
    def form_valid(self, form):
        self.resetstatus()
        return super().form_valid(form)
    
    def resetstatus(self):
        obj, res = Status.objects.get_or_create(user=self.request.user)
        obj.stat = ''
        obj.hash = ''
        obj.save()