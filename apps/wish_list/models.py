from __future__ import unicode_literals
from django.db import models
import re,bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def currentUser(self, request):
        id=request.session['user_id']

        return User.objects.get(id=id)

    def validateUser(self,form_data):
        errors=[]
        if len(form_data['name'])==0:
            errors.append('Name is Required.')
        if len(form_data['username'])==0:
            errors.append('Username is Required.')
        if not EMAIL_REGEX.match(form_data['username']):
            errors.append('Please enter a valid Username!')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')
        if form_data['password'] != form_data['password_confirmation']:
            errors.append('Password Confirmation must match Password.')

        return errors

    def validateLogin(self,form_data):
        errors=[]

        if len(form_data['username'])==0:
            errors.append('Username is Required.')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')

        return errors

    def createUser(self,form_data):
        password=str(form_data['password'])
        hashed_pw=bcrypt.hashpw(password, bcrypt.gensalt())

        user=User.objects.create(
            name=form_data['name'],
            username=form_data['username'],

            password=hashed_pw,
        )

        return user

class WishListManager(models.Manager):

    def listValidation(self,form_data):
        errors=[]
        if len(form_data['item'])==0 or len(form_data['item'])<3:
            errors.append('Item must be longer than 3 characters.')

        return errors


    def createListItem(self,form_data,user):
        wishlist=WishList.objects.create(
            item = form_data['item'],
            user = user,
        )
        return wishlist




class User(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class WishList(models.Model):
    item=models.TextField(max_length=255)
    user=models.ForeignKey(User,related_name='wishlists')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=WishListManager()
