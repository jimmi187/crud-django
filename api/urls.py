from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_overview, name="home"),
    path("employee/create", views.add_employee, name="add-employee"),
    path("employee/", views.view_employees, name="show-employee"),
    path("employee/<int:pk>", views.get_employee_by_id, name="get-employee-by-id"),
    path("employee/<int:pk>/update", views.update_employee, name="update-employee"),
    path("employee/<int:pk>/delete", views.delete_employee_by_id, name="delete-employee-by-id"),

    
    
    
    
    
    ]
