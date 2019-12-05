from django.urls import path
from .views import recruit_information, quiz, main, sith, recruits_withous_hand, recruit_page, accept_recruit, sith_shodow_count

urlpatterns = [
    path('recruit/', recruit_information, name='new_recruit'), # Создание рекрута
    path('quiz/', quiz, name='quiz'),
    path('', main, name='main_page'),
    path('sith/', sith, name='sith'), # Выбор ситха
    path('recruits_withoud_hand/', recruits_withous_hand, name='recruits_without_hand'),
    path('recruit/<int:pk>/', recruit_page, name='recruit_page'),
    path('accept-recruit/', accept_recruit, name='accept-recruit-page'),
    path('sith-count/', sith_shodow_count, name='sith-shadow-count')
]

