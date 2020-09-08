from django.urls import path


urlpatterns = [
    path('', BlogIndexView.as_view()),
    path(''), BlogDetailView.as_view()
]