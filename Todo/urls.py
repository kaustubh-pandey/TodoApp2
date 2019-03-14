from django.conf.urls import url
from . import views
app_name="Todo"
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login_user,name='login'),
    url(r'^logout/',views.logout_user,name='logout'),
    url(r'^log/',views.log,name='log'),
    url(r'^reg/',views.reg,name='reg'),
    url(r'^addTodo/',views.addTodo,name='addTodo'),
    url(r'^deleteTodo/',views.deleteTodo,name='deleteTodo'),
    url(r'^edit/(?P<tid>[0-9]+)/', views.edit, name='edit'),
    url(r'^editTodo/', views.editTodo, name='editTodo'),
]

