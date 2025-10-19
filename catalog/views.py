from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    model = Product.objects.all()
    context = {"product": model}
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)



def contacts(request):
    if request.method == 'POST':
        with open('catalog/text.txt', 'a', encoding='utf-8') as file:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            file.write(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")
            print(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")

    return render(request, 'catalog/contacts.html')
