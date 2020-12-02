from django.conf.urls import patterns, include, url
from django.contrib import admin

from ikwen.core.views import DashboardBase
from ikwen.billing.public.views import Pricing

from ikwen_webnode.webnode.views import FlatPageView

from haira.views import Home

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^billing/', include('ikwen.billing.urls', namespace='billing')),
    url(r'^cashout/', include('ikwen.cashout.urls', namespace='cashout')),
    url(r'^theming/', include('ikwen.theming.urls', namespace='theming')),
    url(r'^revival/', include('ikwen.revival.urls', namespace='revival')),
    url(r'^ikwen/', include('ikwen.core.urls', namespace='ikwen')),
    url(r'^kakocase/', include('ikwen_kakocase.kakocase.urls', namespace='kakocase')),
    url(r'^kako/', include('ikwen_kakocase.kako.urls', namespace='kako')),
    url(r'^shopping/', include('ikwen_kakocase.shopping.urls', namespace='shopping')),
    url(r'^trade/', include('ikwen_kakocase.trade.urls', namespace='trade')),
    url(r'^rewarding/', include('ikwen.rewarding.urls', namespace='rewarding')),
    url(r'^revival/', include('ikwen.revival.urls', namespace='revival')),
    url(r'^marketing/', include('ikwen_kakocase.commarketing.urls', namespace='marketing')),
    url(r'^sales/', include('ikwen_kakocase.sales.urls', namespace='sales')),

    url(r'^page/(?P<url>[-\w]+)/$', FlatPageView.as_view(), name='flatpage'),
    url(r'^blog/', include('ikwen_webnode.blog.urls', namespace='blog')),
    url(r'^web/', include('ikwen_webnode.web.urls', namespace='web')),
    url(r'^items/', include('ikwen_webnode.items.urls', namespace='items')),
    url(r'^echo/', include('echo.urls', namespace='echo')),


    # STAFF URLs
    url(r'^ikwen/dashboard$', DashboardBase.as_view(), name='admin_home'),
    url(r'^ikwen/dashboard$', DashboardBase.as_view(), name='dashboard'),
    url(r'^ikwen/', include('ikwen.core.urls', namespace='ikwen')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^', include('haira.urls', namespace='haira')),
)

