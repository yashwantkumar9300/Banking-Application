"""YesBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from YesBank import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_check/',views.user_check,name="user_check"),
    path('user_home/',views.user_home,name="user_home"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('bank_with_us/',views.bank_with_us,name="bank_with_us"),
    path('work_with_us/',views.work_with_us,name="work_with_us"),
    path('admin_check/',views.admin_check,name="admin_check"),
    path('admin_refresh/',views.admin_refresh,name="admin_refresh"),
    path('user_refresh/',views.user_refresh,name="user_refresh"),
    path('create_account/',views.create_account,name="create_account"),
    path('save_account/',views.save_account,name="save_account"),
    path('view_all_account/',views.view_all_account,name="view_all_account"),
    path('activate_account/',views.activate_account,name="activate_account"),
    path('active_acc/',views.active_acc,name="active_acc"),
    path('change_password/',views.change_password,name="change_password"),
    path('update_password/',views.update_password,name="update_password"),
    path('close_account/',views.close_account,name="close_account"),
    path('clos_acc/',views.clos_acc,name="clos_acc"),
    path('deposit_form/',views.deposit_form,name="deposit_form"),
    path('withdraw_form/',views.withdraw_form,name="withdraw_form"),
    path('deposit_amt/',views.deposit_amt,name="deposit_amt"),
    path('withdraw_amt/',views.withdraw_amt,name="withdraw_amt"),
    path('balance_check/',views.balance_check,name="balance_check"),
    path('transfer_form/',views.transfer_form,name="transfer_form"),
    path('transfer_amt/',views.transfer_amt,name="transfer_amt"),
    path('change_pin_form/',views.change_pin_form,name="change_pin_form"),
    path('change_pin/',views.change_pin,name="change_pin"),
    path('current_account/',views.current_account,name="current_account"),
    path('fd_account/',views.fd_account,name="fd_account"),
    path('fast_cash/',views.fast_cash,name="fast_cash"),
    path('services/',views.services,name="services"),
    path('forgot_pass_form/',views.forgot_pass_form,name="forgot_pass_form"),
    path('mini_statement/',views.mini_statement,name="mini_statement"),
    path('forgot_password/',views.forgot_password,name="forgot_password")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)