


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})





def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'core/user_list.html', { 'users': users })