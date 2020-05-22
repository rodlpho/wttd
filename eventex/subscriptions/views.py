from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription

new = EmailCreateView.as_view(
    model=Subscription,
    form_class=SubscriptionForm,
    email_subject='Confirmação de inscrição'
)

class DescriptionDetail(DetailView):
    def get_object(self):
        object = get_object_or_404(Subscription, hash_url=self.kwargs['hash_url'])
        return object


detail = DetailView.as_view(model=Subscription)
