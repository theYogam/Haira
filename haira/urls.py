from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required, login_required

from ikwen.core.views import DashboardBase
from ikwen.billing.public.views import Pricing
from haira.views import *


urlpatterns = patterns(
    '',
    url(r'^donate/', Donate.as_view(), name='donate'),
    url(r'^booking/', login_required(Booking.as_view()), name='booking'),
    url(r'^glamour_night/', GlamourNight.as_view(), name='glamour_night'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^gallery/', ShowGallery.as_view(), name='gallery'),
    url(r'^partners/', ShowPartners.as_view(), name='partners'),

    url(r'^gallery_list/$', permission_required('haira.ik_manage_gallery')(GalleryList.as_view()),
        name='gallery_list'),
    url(r'^changeGallery/$', permission_required('haira.ik_manage_gallery')(ChangeGallery.as_view()), name='change_gallery'),
    url(r'^changeGallery/(?P<object_id>[-\w]+)/$', permission_required('haira.ik_manage_gallery')(ChangeGallery.as_view())
        , name='change_gallery'),

    url(r'^partner_list/$', permission_required('haira.ik_manage_partner')(PartnerList.as_view()),
        name='partner_list'),
    url(r'^changePartner/$', permission_required('haira.ik_manage_partner')(ChangePartner.as_view()),
        name='change_partner'),
    url(r'^changePartner/(?P<object_id>[-\w]+)/$',
        permission_required('haira.ik_manage_partner')(ChangePartner.as_view())
        , name='change_partner'),

    url(r'^receipt/(?P<receipt_id>[-\w]+)/$', login_required(Receipt.as_view()), name='receipt'),

    # url(r'^set_momo_payment$', set_momo_payment, name='set_momo_payment'),
    # url(r'^confirm_payment/(?P<tx_id>[-\w]+)/(?P<signature>[-\w]+)$', confirm_payment, name='confirm_payment'),
)
