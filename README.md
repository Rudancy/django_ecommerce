[![Build Status](https://travis-ci.org/Rudancy/django_ecommerce.svg?branch=master)](https://travis-ci.org/Rudancy/django_ecommerce)


# Online Ecommerce Shop

This project is about deploying a working ecommerce shop, I decided to focus my shop on selling retro trainers, this is a specialised shop that has the aim of providing only the best trainers for sale. 

The shop was created as a final project to my skills at creating and making an application using all the skills I have learnt from my foundation degree. The shop includes the use of html, css, JavaScript, Python, Django and many others 

## UX

The app provides many user capabilities including

- Registration
- Login and Sign out
- making purchases through card payments
- View products and there information
- Searching for Products
- Using a cart

The application uses Bootstrap 4 to allow it to be used for different screen sizes through its grid system.

**User Stories**

- As a User I would like to be greeted by a professional looking website, that gives me confidence in the products that I may wish to purchase. I have done this by creating a carousel on the very first page displaying professionally taken photos of models, also creating a small about us reassuring the customer that we have them as the most important aspect of the shop. This initially will give the customer confidence. The layout has been done in such away as to show off some of the products without overwhelming the user.

- As a user I want access to the products at all times. Products are accessible through navigation-links at the top of the page on all pages, this means that no matter what page the user is browsing they can always quickly find the department that they would like to access.

- As a user I buying retro Trainers I would like to know more about them. Every Product has a more information button, that will then redirect the user to another page, where there are more images of that Product, and also some history about them.

- As a user I do not want mass marketing of products. I designed the site so that only a few Products are visible at any one time, so as not to give the impression of more is better, but fewer and better quality is what we (the shop) are about. I also did not want the pages to be too flashy giving a gimmicky feel to the site.

  

  **Wireframes** 

  ![]()

  ![]()

  ![]()

  ![]()

  







## Features

- Navbar

  That allows the user to navigate to different brands, men's, women's and see the cart, it uses drop downs to allow for more space. The Navbar also makes use of if statements so that should a user not be signed in then they do not have access to logout functions, and in turn if the user is signed in then they do not need to see a login link. This keeps the Navbar clean, tidy and also takes away potential points of confusion, you know when your signed in or out. The use of a navigation search bar was immensely important as this allows seamless navigation to any product the user may require, a view was created  (below) that allows the user to search through the database using letters and words that are contained in the product fields. 

```python
def do_search(request):
    """
    a view that allows the customer to
    search for products
    """
    products=Product.objects.filter(name__icontains=request.GET['q'])
    if products is None:
        return render(request, "inde.html")
    else:
        return render(request, "products.html", {"products":products})
```

 

The use of a carousel allowed me to display different shots of models wearing trainers. Instead of using static pictures that would of taken up more page-real-estate. It also adds a small but interactive aspect to the website. 

```javascript
<div class="container-fluid">
    <div class="row justify-content-center">
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img class="d-block w-100 carousel-image-size" height="500" src="{% static 'images/carousel/1.jpg'%}" alt="First slide">
                </div>
                <div class="carousel-item">
                    <img class="d-block w-100 carousel-image-size" height="500" src="{% static 'images/carousel/2.jpg' %}" alt="Second slide">
                </div>
                <div class="carousel-item">
                    <img class="d-block w-100 carousel-image-size" height="500" src="{% static 'images/carousel/3.jpg' %}" alt="Third slide">
                </div>
            </div>
            
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
             </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
            </a>
        </div>
    </div>
</div>
```

The use of Django's systems allowed me to create models that where unique to my needs, for example the need to have multiple fields, and also the ability to create tuples and then use within the models and display them in the templates was highly effective.

```python
from django.db import models


#https://www.youtube.com/watch?v=Xjty8q524Jo&list=PLLRM7ROnmA9F2vBXypzzplFjcHUaKWWP5&index=2

BRAND_CHOICES = (
    ('AD', 'Addidas'),
    ('NK', 'Nike'),
    ('CV', 'Converse'),
    ('DD', 'Diadora'),
    ('EA', 'Emporium Armani'),
    ('NB', 'New Balance'),
    ('PM', 'Puma'),
    
)

AGE_CHOICES = (
    ('M', 'Mens'),
    ('F', 'Women'),
    ('k', 'kids')
    )
    



class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description=models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_1 = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to='images')
    image_3 = models.ImageField(upload_to='images')
    year_created = models.DateField(auto_now=False)
    history_of_product_1 = models.TextField()
    history_of_product_2 = models.TextField()
    history_of_product_3 = models.TextField(blank=True)
    history_of_product_4 = models.TextField(blank=True)
    age = models.CharField(max_length=5, choices=AGE_CHOICES, default='')
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='AD')
    
    
    
    def __str__(self):
        return self.name
    

```

 





### Future Features

Features that I would like to implement are a wish list category that links products to users, so that both user and owner benefit, the user does not have to keep searching for the same product, but also through access in the admin panel an owner could see what users desired and thus adjust there stock or even price to encourage their sale.

Other features would be a review service that allows different specialised Trainer buyers to comment on what Trainers are currently trending. This would allow greater interaction between owner and customer but also allow the owner to be guided as to what to stock for the future.  

## Technologies

-  [Stripe](https://stripe.com/en-no) - This allows for the use of card transactions thus allowing for the exchange of services and goods for money.

- [Django](https://docs.djangoproject.com/en/3.0/releases/1.11/) - this is the server side technology that allows you to POST/GET information between the frontend user and the backend owner. Using its own template language you can then pass database queries to the frontend allowing you to display products, usernames ect.

- [Github](https://github.com/)- allows you to put your website coding into an accessible storage system, it allows for version control.

- [PostgreSQL](https://www.postgresql.org/)Used for deployment in Heroku.

-  [Gunicorn](https://docs.gunicorn.org/en/stable/) Used as the Http server.

-  [Heroku](https://en.wikipedia.org/wiki/Heroku) Used for the deployment of my project.

- [Bootstrap](https://getbootstrap.com/docs/4.4/) - this allows developers to create well organised websites that are easier to position the HTML elements. It has a number of features such as the grid-system, positioning, mobile-responsive and many more

     

## Testing

A HTML validator https://validator.w3.org/nu/#textarea has been used to validate the code.

A JavaScript validator https://jshint.com/ has been used to validate the code.

The website has been tested for responsiveness using Google Chrome Development tools. It has been accessed using a mobile phone and an Ipad to see how the browser reacts to different browser sizes and it is fully functioning (This has been achieved through the use of Bootstrap 4 classes.

Forms have all been tested for functioning manually.

```javascript

```

##  

## Deployment

Website was deployed using GitHub, to do this follow these instructions

1.  go to the GitHib repository  
2. under the repositories name click settings
3. go to GitHub pages (scroll down)
4. click on the drop-down menu under source and click on master branch
5. click save

Heroku

- On Heroku an application was created
- Attach the Heroku-Postgres database
- Installed ***dj-database-urls*** , ***psycopg2***, ***gunicorn***, 
- create dj_database_url in settings.py
- Add the heroku app to allowed settings
- add key value pairs to config vars in heroku 
- push to github

## Credits

Much credit has to go to the members of slack as without their patience in answering questions i would not of been able to do some of the things I have a done.

Further credits must go to scanfccode for their awesome footer  https://codepen.io/scanfcode/pen/MEZPNd

Further credit also must go to the tutors as they have guided me through many a hard problem







