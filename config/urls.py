from django.contrib import admin
from django.urls import path
from app.views import HouseList, HouseDetail, AgentProfile, ProfileUpdate, \
    HouseUpdate, HouseCreate, HouseDelete, LoginUser, SignUpUser
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from app import views


urlpatterns = [
    path('', HouseList.as_view(), name='houses'),
    path('profile/<str:pk>/', AgentProfile.as_view(), name='profile'),
    path('profile-update/<str:pk>/', ProfileUpdate.as_view(), name='profile-update'),
    path('detail/<str:pk>/', HouseDetail.as_view(), name='house'),
    path('update/<str:pk>/', HouseUpdate.as_view(), name='update'),
    path('create/', HouseCreate.as_view(), name='create'),
    path('delete/<str:pk>/', HouseDelete.as_view(), name='delete'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('properties/', views.property_page, name='properties'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
