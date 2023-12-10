"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from reports import views as ReportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-product-data/', ReportView.get_product_data),
    path('set-product-data/', ReportView.set_product_data),
    path('order/', ReportView.order),
    path('upi-qr/', ReportView.upi_qr_operation),
    path('sales/', ReportView.sales),
    path('sales-report/', ReportView.sales_report),
    path('analysis/', ReportView.analysis),
    path('clients/', ReportView.clients),
    path('auth/', ReportView.auth),
    path('sales-analysis-date/', ReportView.analysis_date),
    path('update/', ReportView.update),
]
