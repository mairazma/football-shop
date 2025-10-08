from django.urls import path
from main.views import (
    show_main, create_product, show_product, show_xml, show_json, 
    show_xml_by_id, show_json_by_id, register, login_user, logout_user,
    edit_product, delete_product,
    # AJAX endpoints
    get_products_json, create_product_ajax, edit_product_ajax, 
    delete_product_ajax, get_product_json, login_ajax, register_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('news/<uuid:id>/edit', edit_product, name='edit_product'),
    path('news/<uuid:id>/delete', delete_product, name='delete_product'),

    path('api/products/', get_products_json, name='get_products_json'),
    path('api/products/<uuid:id>/', get_product_json, name='get_product_json'),
    path('api/products/create/', create_product_ajax, name='create_product_ajax'),
    path('api/products/<uuid:id>/edit/', edit_product_ajax, name='edit_product_ajax'),
    path('api/products/<uuid:id>/delete/', delete_product_ajax, name='delete_product_ajax'),
    path('api/login/', login_ajax, name='login_ajax'),
    path('api/register/', register_ajax, name='register_ajax'),
]