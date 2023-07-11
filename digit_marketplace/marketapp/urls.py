from django.urls import path
from marketapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:id>", views.detail, name="detail"),
    path("payment/success/", views.payment_success_view, name="success"),
    path("payment/failed/", views.payment_failed_view, name="failed"),
    path(
        "api/checkout-session/<int:id>/",
        views.create_checkout_session,
        name="api_checkout_session",
    ),
    path("createproduct/", views.create_product, name="create-product"),
    path("editproduct/<int:id>/", views.product_edit, name="edit-product"),
    path("deleteproduct/<int:id>/", views.product_delete, name="delete-product"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="marketapp/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="marketapp/logout.html"),
        name="logout",
    ),
    path("invalid/", views.invalid, name="invalid"),
    path("purchases/", views.my_purchases, name="purchases"),
    path("sales/", views.sales, name="sales"),
]
