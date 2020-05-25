class PostForm(forms.ModelForm):
    products = Product.objects.all()
    wishlist = products

    class Meta:
       model=wish_list
       fields=product