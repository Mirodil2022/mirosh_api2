from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),

    path('advocates/', views.advocate_list, name="advocates"),
    # path('advocates/<str:username>/', views.advocate_detail),
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),


#companies/
path('companies/', views.companies_list)
#companies/:id

]

