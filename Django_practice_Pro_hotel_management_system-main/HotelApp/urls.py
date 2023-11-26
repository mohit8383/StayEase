from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home,name="Home"),
    path('all', views.all),
    path('OnlineBooking', views.OnlineBooking, name='OnlineBooking'),
    path('Aothur_login', views.Aothur_login, name='Aothur_login'),
    path('auth_logout', views.auth_logout, name='auth_logout'),
    path('Aothur_Reg', views.Aothur_Reg, name='Aothur_Reg'),
    path('Aothur_Fotpass', views.Aothur_Fotpass, name='Aothur_Fotpass'),
    path('all_admin', views.all_admin),
    path('Adminpage', views.Admin, name='Adminpage'),
    path('Addemployee', views.Addemployee, name='Addemployee'),
    path('Editemployee/<id>', views.Editemployee, name='Editemployee'),
    path('Allemployee', views.Allemployee, name='Allemployee'),
    path('online_Booking_info', views.online_Booking_info, name='online_Booking_info'),
    path('Edit_online_Booking/<id>', views.Edit_online_Booking, name='Edit_online_Booking'),
    path('AddCustomer', views.AddCustomer, name='AddCustomer'),
    path('AllCustomer', views.AllCustomer, name='AllCustomer'),
    path('EditCustomer/<id>', views.EditCustomer, name='EditCustomer'),
    path('delete/<id>', views.Delete, name='delete'),
    path('Search', views.Search, name='Search'),
    path('AddCustpage_Delete/<id>', views.AddCustpage_Delete, name='AddCustpage_Delete'),
    path('AllCustpage_Delete/<id>', views.AllCustpage_Delete, name='AllCustpage_Delete'),
    path('AddEmplopage_Delete/<id>', views.AddEmplopage_Delete, name='AddEmplopage_Delete'),
    path('Add_Employee_Search', views.Add_Employee_Search, name='Add_Employee_Search'),
    path('AllEmployee_Delete/<id>', views.AllEmployee_Delete, name='AllEmployee_Delete'),
    path('Add_room', views.Add_room, name='Add_room'),
    path('Add_Room_Search', views.Add_Room_Search, name='Add_Room_Search'),
    path('AddRooms_Delete/<id>', views.AddRooms_Delete, name='AddRooms_Delete'),
    path('EditRooms/<id>', views.EditRooms, name='EditRooms'),
    path('All_Room', views.All_Room, name='All_Room'),
    path('AllRooms_Delete/<id>', views.AllRooms_Delete, name='AllRooms_Delete'),
    path('AddEmployeeSalary', views.AddEmployeeSalary, name='AddEmployeeSalary'),
    path('EmployeeShow', views.EmployeeShow, name='EmployeeShow')
]