from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import DetailView

# Create your views here.


@method_decorator(staff_member_required, name='dispatch')
class BaseSMSView(DetailView):
    url = None
    object = None
    sms_class = None
    lang = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.sms_class(self.object).send(lang=self.lang)
        message = 'The {} SMS has been sent.'.format(self.sms_name)
        messages.success(request, message)
        return redirect(reverse(self.url, args=(self.object.pk,)))
