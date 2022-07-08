from django.urls import path,include
from .views import LabTechRegistrationView,DoctorRegistrationView, ReceptionistRegistrationView,UserLoginView,NurseRegistrationView

urlpatterns = [
	
	path('signup/doctor/',DoctorRegistrationView.as_view(),name='signup_doctor'),
	path('signup/nurse/',NurseRegistrationView.as_view(),name='signup_nurse'),
	path('signup/labtech/',LabTechRegistrationView.as_view(),name='labtech_signup'),
	path('signup/reception/',ReceptionistRegistrationView.as_view(),name='labtech_signup'),

	
	path('signin/',UserLoginView.as_view()),
]