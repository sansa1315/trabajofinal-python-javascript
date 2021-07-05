from trabajofinal.settings import BASE_DIR
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import *
import pdb
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
  productos = Producto.objects.all().order_by('-id')[:10]  
  return render(request, "inicio.html", {'productos': productos})

def login(request):
  if request.user.is_authenticated:
    return redirect('inicio')
  else:
    if request.method == 'POST':
      user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
      if user is not None:
        auth_login(request, user)
        # messages.success(request, 'Bienvenido '+ request.POST.get('username'))
        return redirect('inicio')
      else:
        return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request,"login.html")

def logoutUser(request):
  logout(request)
  return redirect('inicio')

def registro(request):
  if request.user.is_authenticated:
    return redirect('inicio')
  else:
    form = CreateUserForm()
    if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request, 'Cuenta creada exitosamente')
        return redirect('login')
    return render(request, "registro.html",{'form':form})

@login_required(login_url = 'login')
def carrito(request, pk=""):
  if request.user.is_superuser:
    return redirect('login')
  if pk:
    producto = Producto.objects.get(id=pk)
    usuario = User.objects.get(username=request.user)  
    order = {'usuario': usuario, 'producto': producto}  
    form = CreateOrderForm(order)        
    if form.is_valid():
      form.save()
  orders = Order.objects.filter(usuario=request.user)  
  total = 0
  for order in orders:
    total += order.producto.precio
  
  return render(request, "carrito.html", {'carrito': orders, 'total':total})

def carritoDel(request, pk):
  if request.user.is_superuser:
    return redirect('login')

  order = Order.objects.get(id=pk)
  order.delete()      
  orders = Order.objects.filter(usuario=request.user)  
  total = 0
  for order in orders:
    total += order.producto.precio
  return render(request, "carrito.html", {'carrito': orders, 'total':total})

def productoCrud(request):
  # if not request.user.is_superuser:
  #   return redirect('inicio')
  if request.method == 'POST':
    form = CreateProductForm(request.POST, request.FILES)
    print(request.POST)
    if form.is_valid():
      form.save()
      form = CreateProductForm()
      return render(request, 'productoCrud.html', {'form':form})

  form = CreateProductForm()
  return render(request, 'productoCrud.html', {'form':form})

def productoEdit(request, pk):   
  if Producto.objects.filter(id=pk).exists():
    producto = Producto.objects.get(id=pk)
    form = CreateProductForm(instance=producto)
  if request.method == 'POST':
    form = CreateProductForm(request.POST, request.FILES, instance=producto)
    if form.is_valid():
      form.save()
      redirect('productoCrud')

  return render(request, 'productoCrud.html', {'form': form})

def productoDetalle(request, pk):   
  # if Producto.objects.filter(id=pk).exists():
  producto = Producto.objects.get(id=pk)
  form = CreateProductForm(instance=producto)
  if request.method == 'POST':
    form = CreateProductForm(request.POST, request.FILES, instance=producto)
    if form.is_valid():
      form.save()
      redirect('productoCrud')

  return render(request, 'productoDetalle.html', {'form': form, 'productoId':pk})
  

def productoFind(request, catg=''):
  if request.method == 'POST':
    productos = Producto.objects.filter(descripcion__icontains=request.POST['search'])
    return render(request, 'productoFind.html', {'productos': productos})
  productos = Producto.objects.filter(categoria=catg)

  # form = CreateProductForm(instance=producto)
  # if request.method == 'POST':
  #   form = CreateProductForm(request.POST, instance=producto)
  #   if form.is_valid():
  #     form.save()
  #     redirect('productoCrud')


  return render(request, 'productoFind.html', {'productos': productos})

def acercaDe(request):
  return render(request, 'acercaDe.html')



