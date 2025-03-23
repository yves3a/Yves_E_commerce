from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from products.views import login_view, signup_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Make login the default page
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('products/', include('products.urls')),
    
    # Password reset URLs
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='password-reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),
         name='password_reset_complete'),
]
