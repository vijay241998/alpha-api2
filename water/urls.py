from django.urls import path
from django.urls import path
from.views import registerform


urlpatterns = [
    path('register/', registerform.as_view()),

]