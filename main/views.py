from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Products
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': 'Maira Azma Shaliha',
        'class': 'PBP C',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'active_user': request.user
    }
    return render(request, "main.html", context)

def get_products_json(request):
    try:
        filter_type = request.GET.get("filter", "all")
        
        if filter_type == "all":
            products_list = Products.objects.all()
        else:
            # For "my" filter, require authentication
            if not request.user.is_authenticated:
                return JsonResponse({'products': []}, safe=False)
            products_list = Products.objects.filter(user=request.user)
        
        # Convert to list of dictionaries
        products_data = []
        for product in products_list:
            # Handle potential None values
            try:
                products_data.append({
                    'id': str(product.id),
                    'name': product.name or '',
                    'price': product.price or 0,
                    'description': product.description or '',
                    'thumbnail': product.thumbnail or '',
                    'category': product.category or '-',
                    'is_featured': product.is_featured or False,
                    'purchase_count': product.purchase_count or 0,
                    'user': product.user.username if product.user else 'Unknown',
                    'is_owner': request.user.is_authenticated and product.user and product.user == request.user
                })
            except Exception as e:
                # Skip products with errors
                print(f"Error processing product {product.id}: {str(e)}")
                continue
        
        return JsonResponse({'products': products_data}, safe=False)
    except Exception as e:
        import traceback
        print(f"Error in get_products_json: {str(e)}")
        print(traceback.format_exc())
        return JsonResponse({'error': str(e), 'products': []}, status=500)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def create_product_ajax(request):
    try:
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        thumbnail = request.POST.get('thumbnail')
        category = request.POST.get('category')
        is_featured = request.POST.get('is_featured') == 'on'
        
        # Validasi
        if not name or not price:
            return JsonResponse({
                'success': False,
                'message': 'Name and price are required'
            }, status=400)
        
        # Create product
        product = Products.objects.create(
            user=request.user,
            name=name,
            price=int(price),
            description=description,
            thumbnail=thumbnail if thumbnail else None,
            category=category if category else '-',
            is_featured=is_featured
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Product created successfully!',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'thumbnail': product.thumbnail,
                'category': product.category,
                'is_featured': product.is_featured,
                'purchase_count': product.purchase_count,
                'user': product.user.username,
                'is_owner': True
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

# AJAX VIEW untuk edit product
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Products, pk=id)
        
        # Check ownership
        if product.user != request.user:
            return JsonResponse({
                'success': False,
                'message': 'You do not have permission to edit this product'
            }, status=403)
        
        # Update fields
        product.name = request.POST.get('name', product.name)
        product.price = int(request.POST.get('price', product.price))
        product.description = request.POST.get('description', product.description)
        product.thumbnail = request.POST.get('thumbnail', product.thumbnail)
        product.category = request.POST.get('category', product.category)
        product.is_featured = request.POST.get('is_featured') == 'on'
        
        product.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Product updated successfully!',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'thumbnail': product.thumbnail,
                'category': product.category,
                'is_featured': product.is_featured,
                'purchase_count': product.purchase_count,
                'user': product.user.username,
                'is_owner': True
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

# AJAX VIEW untuk delete product
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Products, pk=id)
        
        # Check ownership
        if product.user != request.user:
            return JsonResponse({
                'success': False,
                'message': 'You do not have permission to delete this product'
            }, status=403)
        
        product.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Product deleted successfully!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

# AJAX VIEW untuk get single product (untuk edit)
@login_required(login_url='/login')
def get_product_json(request, id):
    try:
        product = get_object_or_404(Products, pk=id)
        
        return JsonResponse({
            'success': True,
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'thumbnail': product.thumbnail,
                'category': product.category,
                'is_featured': product.is_featured,
                'purchase_count': product.purchase_count,
                'user': product.user.username,
                'is_owner': product.user == request.user
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=404)

def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        products_item = Products.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        products_item = Products.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [products_item])
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        news_entry = form.save(commit=False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Products, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')
        
        form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2
        })
        
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Your account has been successfully created!'
            })
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            
            return JsonResponse({
                'success': False,
                'errors': errors
            }, status=400)
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    }, status=405)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Login successful!',
                'username': user.username
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid username or password'
            }, status=401)
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    }, status=405)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    news = get_object_or_404(Products, pk=id)
    form = ProductForm(request.POST or None, instance=news)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Products, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))