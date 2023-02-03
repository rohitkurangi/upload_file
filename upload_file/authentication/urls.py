from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    ## login operations and admin crud operation here
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain'),
    ]