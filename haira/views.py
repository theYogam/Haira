# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.db.models.loading import get_model
from django.http.response import Http404
from django.views.generic import TemplateView


from ikwen.core.views import HybridListView, ChangeObjectBase
from ikwen.core.utils import get_service_instance

from ikwen.billing.utils import get_next_invoice_number
from ikwen.billing.models import Product, Payment
from ikwen.billing.admin import ProductAdmin

from haira.models import Gallery, Partner
from haira.admin import GalleryAdmin, PartnerAdmin

logger = logging.getLogger('ikwen')


class Home(TemplateView):
    template_name = 'haira/home.html'


# class Pricing(HybridListView):
#     """
#     Pricing view that shows up billing Product user
#     may subscribe to.
#     """
#     queryset = Product.objects.filter(is_active=True)
#     ordering = ('order_of_appearance', 'cost', )
#     template_name = 'billing/public/pricing.html'
#     context_object_name = 'product_list'


class Donate(TemplateView):
    template_name = 'billing/public/donate.html'


class Booking(HybridListView):
    model = Product
    model_admin = ProductAdmin
    template_name = 'haira/show_product_list.html'
    # html_results_template_name = 'haira/snippets/product_list_results.html'


class GlamourNight(TemplateView):
    template_name = 'haira/glamour_night.html'


class ShowGallery(TemplateView):
    template_name = 'haira/show_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(ShowGallery, self).get_context_data(**kwargs)
        context['gallery_list'] = Gallery.objects.all()
        return context


class ShowPartners(TemplateView):
    template_name = 'haira/show_partners.html'

    def get_context_data(self, **kwargs):
        context = super(ShowPartners, self).get_context_data(**kwargs)
        context['partner_list'] = Partner.objects.all()
        return context


class ChangeGallery(ChangeObjectBase):
    model = Gallery
    model_admin = GalleryAdmin


class GalleryList(HybridListView):
    model = Gallery
    model_admin = GalleryAdmin


class ChangePartner(ChangeObjectBase):
    model = Partner
    model_admin = PartnerAdmin


class PartnerList(HybridListView):
    model = Partner
    model_admin = PartnerAdmin


class About(TemplateView):
    template_name = 'haira/about.html'


class Receipt(TemplateView):
    template_name = 'everyday/receipt.html'

    def get_context_data(self, **kwargs):
        context = super(Receipt, self).get_context_data(**kwargs)
        config = get_service_instance().config
        receipt_id = self.kwargs.get('receipt_id')
        try:
            payment = Payment.objects.select_related('pack', 'member').get(pk=receipt_id)
        except Payment.DoesNotExist:
            raise Http404("Payment not found")
        context['currency_symbol'] = config.currency_symbol
        context['payment'] = payment
        context['amount'] = payment.amount
        context['payment_number'] = get_next_invoice_number()
        return context


