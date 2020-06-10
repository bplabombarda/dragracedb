from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('episodes/', include('episodes.urls')),
    path('lipSyncs/', include('lip_syncs.urls')),
    path('queens/', include('queens.urls')),
    path('seasons/', include('seasons.urls')),
    path('admin/', admin.site.urls),
]

