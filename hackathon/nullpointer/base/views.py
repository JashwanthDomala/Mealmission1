from django.shortcuts import render,redirect,get_object_or_404
from .models import food
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'base/home.html')

def org(request):
    foods = food.objects.filter(user=request.user)
    context = {'foods': foods}
    return render(request,'base/org.html',context)
def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        expire = request.POST['expirdate']
        quantity = request.POST['quantity']
        food.objects.create(name=name,expirdate=expire,quantity=quantity,user=request.user)
        return redirect('base:org')
    return render(request,'base/add.html')
from django.http import HttpResponseForbidden

def delete(request):
    if request.method == "POST":
        food_item = get_object_or_404(food, pk=request.POST['pk'])
        food_item.delete()  
        return redirect('base:org')  
    return redirect('base:org')

def update_food(request, pk):
    food_item = get_object_or_404(food, pk=pk)

    if request.method == "POST":
        food_item.quantity = request.POST['quantity'] 
        food_item.save() 
        return redirect('base:org') 

    return render(request, 'base/update_food.html', {'food': food_item})

def vol(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    if search_query:
        foods = food.objects.filter(name__icontains=search_query)  # Filter foods by name
    else:
        foods = food.objects.all()  # Show all foods if there's no search query

    context = {'foods': foods, 'search_query': search_query}
    return render(request, 'base/vole.html', context)
