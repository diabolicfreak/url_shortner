from django.conf.urls import url
from django.contrib import admin
from shortner.views import URLRedirectView, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    # url(r'^a/(?P<shortcode>[\w-]+)', shortner_url_view),
    url(r'^(?P<shortcode>[\w-]+)', URLRedirectView.as_view(), name='shortcode'),
]
