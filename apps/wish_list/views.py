from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt
from .models import User,WishList

def flashErrors(request,errors):
    for error in errors:
        messages.error(request,error)

def index(request):
    return render(request,'wish_list/index.html')

def homePage(request):
    current_user=User.objects.currentUser(request)
    wishlists=WishList.objects.all()
    other_items=WishList.objects.exclude(id=current_user.id)

    context={
        'user': current_user,
        'wishlists':wishlists,
        'other_items':other_items
    }

    return render(request,'wish_list/homePage.html', context)

def register(request):
    if request.method=='POST':
        errors=User.objects.validateUser(request.POST)
        if not errors:
            print 'Create User'
            user=User.objects.createUser(request.POST)

            request.session['user_id']=user.id

            return redirect('/homePage')

        flashErrors(request,errors)
    return redirect('/')

def login(request):
    if request.method=='POST':
        errors=User.objects.validateLogin(request.POST)
        if not errors:
            user=User.objects.filter(username=request.POST['username']).first()

            if user:
                password=str(request.POST['password'])
                user_password=str(user.password)

                hashed_pw=bcrypt.hashpw(password,user_password)

                if hashed_pw==user_password:
                    request.session['user_id']=user.id

                    return redirect('/homePage')

            errors.append('Invalid account Information')
        flashErrors(request,errors)

    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect('/')

def createWishListPage(request):
    return render(request,'wish_list/createWishListPage.html')

def createNewListItem(request):
    if request.method=='POST':
        errors=WishList.objects.listValidation(request.POST)
        if not errors:
            current_user=User.objects.currentUser(request)
            wishlist=WishList.objects.createListItem(request.POST, current_user)


            return redirect('/homePage')

        flashErrors(request,errors)

    return redirect('/createWishListPage')

def deleteItem(request,item_id):
    if request.method=='POST':
        wishlist=WishList.objects.get(id=item_id)
        print wishlist

        wishlist.delete()

    return redirect('/homePage')

def listItem(request,id):
    current_user=User.objects.currentUser(request)
    wishlists=WishList.objects.get(id=id)


    context={
        'user': current_user,
        'wishlists':wishlists,
    }


    return render(request,'wish_list/listItem.html', context)
