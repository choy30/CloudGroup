from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView, AddBoatView, MyBoat, BoatDetail, UpdateBoatView, DeleteBoatView, RentBoatView, RentListView, rent_success, DeleteRentView
from blog import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('boat_details/<int:pk>', BoatDetail.as_view(), name="boat-detail"),
    path('my_boat/', MyBoat.as_view(), name="my-boat"),
    path('my_boat/add_boat/', AddBoatView.as_view(), name="add-boat"),
    path('boat/update/<int:pk>', UpdateBoatView.as_view(), name="update-boat"),
    path('boat/delete/<int:pk>', DeleteBoatView.as_view(), name="delete-boat"),
    path('boat_details/<int:pk>/rent/', RentBoatView.as_view(), name='rent-boat'),
    path('rent_list/', RentListView.as_view(), name="rent-list"),
    path('rent_success/', rent_success, name='rent-success'),
    path('rent/delete/<int:pk>', DeleteRentView.as_view(), name='delete-rent'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)