from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from questionary.views import *


from rest_framework import routers
from questionary import views

router = routers.DefaultRouter()
router.register(r'quest', views.QuestionaryViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'questiontype', views.QuestionTypeViewSet)
router.register(r'answers', views.AnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_questionary, name='list_quest'),
    path('<int:questionary_id>/', quest, name='quest'),
    path('add_questionary/', add_questionary, name='add_quest'),
    path('add_questions/', add_questions, name='add_questions'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
