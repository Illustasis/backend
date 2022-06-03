from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(('System.urls', 'System'))),
    path('api/book/', include(('Book.urls', 'Book'))),
    path('api/topic/', include(('Topic.urls', 'Topic'))),
    path('api/group/', include(('Group.urls', 'Group'))),
    path('api/movie/', include(('Movie.urls', 'Movie'))),
    path('api/tele/', include(('Tele.urls', 'Tele'))),
    path('api/passage/', include(('Passage.urls', 'Passage'))),
]

