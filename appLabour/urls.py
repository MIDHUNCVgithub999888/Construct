from django.urls  import path
from. import views
from django.conf.urls import url

app_name='appLabour'
urlpatterns= [
	path('UserRegistration/', views.UserRegistration, name='UserRegistration'),
	path('UserLogin/',views.UserLogin,name='UserLogin'),
	path('UserHome/<int:id>/',views.UserHome,name='UserHome'),
	path('ViewProfile/<int:id>/',views.ViewProfile,name='ViewProfile'),
	path('UserDelete/<int:id>/',views.UserDelete,name='UserDelete'),
	path('UserLogout/',views.UserLogout,name='UserLogout'),
	path('ChangePassword/<int:id>/',views.ChangePassword,name='ChangePassword'),
	path('index/',views.index,name="index"),
	path('ImageUpload/',views.ImageUpload,name='ImageUpload'),
	path('ImageGallery/',views.ImageGallery,name='ImageGallery'),
	path('ProductDetails/<int:pk>/',views.ProductDetails,name='ProductDetails'),
	url(r'^.*/$',views.View_404,name="View_404"),

    ]