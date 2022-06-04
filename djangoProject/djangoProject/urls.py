from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(('System.urls', 'System'))),
    path('api/book/', include(('Book.urls', 'Book'))),
    path('api/topic/', include(('Topic.urls', 'Topic'))),
    path('api/group/', include(('Group.urls', 'Group'))),
    path('api/movie/', include(('Movie.urls', 'Movie'))),
    path('api/tele/', include(('Tele.urls', 'Tele'))),
    path('api/passage/', include(('Passage.urls', 'Passage'))),
    path('api/photo/', include(('Photo.urls', 'Photo'))),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
