from django.urls import path
from .views import *
urlpatterns = [

	path('',index,name='home'),
	path('holiday/',holiday),
	path('conveyance/',conveyance),
	path('conveyancelist/',conveyancelist),
	path('allconveyancelist/',allconveyancelist),
	path('update-conveyance/<int:pk>/',Conveyanceupdateview.as_view()),
	path('Conveyanceupdateviewuser/<int:pk>/',Conveyanceupdateviewuser.as_view()),
	path('holidayform/',holidayform),
	path('delete/<int:id>/',deleteview),
	path('editholiday/',editholiday),
	path('holidayedit/<int:pk>/',holidayedit.as_view()),
	path('deleteholiday/<int:id>/',deleteholiday),
	path('post/',Post),
	path('notice/',Notice),
	path('viewpost/',postview),

]