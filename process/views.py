from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Antq
from .forms import AntqForm
#Item

# Create your views here.

def index(request):
    #results = Item.objects.all()
    antique = Antq.objects.all()
    return render(request, 'index.html', {'antiques': antique})

#{'items': results},
    

def add_antique(request):
    if request.method == "POST":
        form = AntqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
        #new_Antq = Antq()
        #new_Antq.name = request.POST.get('atq_name')
        #new_Antq.price = request.POST.get('atq_price')
        #new_Antq.manufacture = request.POST.get('atq_manu')
        #new_Antq.description = request.POST.get('atq_desc')
        #new_Antq.height = request.POST.get('atq_height')
        #new_Antq.width = request.POST.get('atq_width')
        #new_Antq.depth = request.POST.get('atq_depth')
        #new_Antq.save()
        #return redirect(index)
    else:
        form = AntqForm()
        
    return render(request, 'addantique.html', {'form': form})


def edit_antique(request, id):
    
    antq = get_object_or_404(Antq, pk=id)
    
    if request.method == "POST":
        form = AntqForm(request.POST, instance = antq)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = AntqForm(instance=antq)
    
    return render(request, 'addantique.html', {'form': form})