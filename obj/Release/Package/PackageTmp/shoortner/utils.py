import random
import string
from django.conf import settings


#from shoortner.models import KssirURL

SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)


def code_generator(size=6,chars=string.ascii_lowercase + string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    KssirURL = instance.__class__
    qs_exist = KssirURL.objects.filter(shortcode=new_code).exists()
    if  qs_exist:
            return create_shortcode(size=size)
    return new_code
