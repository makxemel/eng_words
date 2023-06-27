from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
#     path('new/', word_post, name='add_word'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('rand/', word_list_rand, name='rand_word'),

    path('words-mode/', TenWordsList.as_view(), name='words_mode'),
    path('word-mode/<int:word_id>/', delete_student_word, name='delete_student_word'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)