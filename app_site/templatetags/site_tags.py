import qrcode
import io
import os

from django import template
from django.db.models import Count
from django.conf import settings

from app_site.forms import SearForm
from app_site.models import PersMenu

from PIL import Image

register = template.Library()



@register.simple_tag()
def smenu():
    smenu = [
        # { 'title': 'Articles',   'img': 'app_site/images/arts.png', 'url': 'arts_list', 'class': 'smenu' },
        # { 'title': 'Ginecology', 'img': 'app_site/images/gine.png', 'url': 'gine',      'class': 'smenu' },
        # { 'title': 'Тест',       'img': 'app_site/images/test.png', 'url': 'test',      'class': 'smenu' },
    ]
    return smenu


@register.simple_tag()
def sear_form():
    form = SearForm()
    return form


@register.simple_tag(takes_context=True)
def persmenu(context):
    groulist = context.request.user.groups.all()
    pmenu = PersMenu.objects.filter(publ=True, grou__in=groulist).annotate(num_grou=Count('grou'))
    return pmenu



@register.simple_tag(takes_context=True)
def qrco(context, obj):

    path_root = settings.MEDIA_ROOT + str(obj.pk)+'/'
    if not os.path.exists(path_root):
        os.mkdir(path_root)
    
    file_url = settings.MEDIA_URL + str(obj.pk)+'/qr.png'

    try:
        os.remove(path_root)
    except:
        print('Path is not a file')

    data = obj.hash

    if data:
        print('data: '.format(data))
        qrco = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=40, border=1)
        qrco.add_data(data)
        qrco.make(fit=True)
        qrco = qrco.make_image(fill_color="black", back_color="white")
        qrco.save(path_root+'qr.png')
        return file_url
    else:
        return False

