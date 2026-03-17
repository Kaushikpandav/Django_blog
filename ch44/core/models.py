# from django.db import models

# # abstract model
# class basemodel(models.Model):
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   name = models.CharField(max_length=100, blank=True, null=True)

#   class Meta:
#     abstract = True

# class customer(basemodel):
#   def __str__(self):
#     return self.name

# class seller(basemodel):

#   account_open_date = models.DateField(blank=False, null=False, help_text='Account open date')
#   def __str__(self):
#     return self.name

# class admin(basemodel):
#   name = None
#   def __str__(self):
#     return self.name

# # model inheritence
# class Examcenter(models.Model):
#   center_name = models.CharField(max_length=100)
#   location = models.CharField(max_length=100)

#   def __str__(self):
#       return self.name

# class candidate(Examcenter):
#   name = models.CharField(max_length=100)
#   roll_no = models.IntegerField(blank=False, null=False)

#   def __str__(self):
#       return self.name

# # proxy model
# class product(models.Model):
#   name = models.CharField(max_length=100)
#   price = models.DecimalField(max_digits=10, decimal_places=2)
#   def __str__(self):
#     return self.name

# class productproxy(product):
#   class Meta:
#     proxy = True
#     ordering = ['name']

# # - add this 2 model in migrations and admin...


========================================================================

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# 1. One to One:

# class profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE) # if i delete user from User the both user and profile will be deleted But if user will delete from the profile then only profile will be deleted

#   user = models.OneToOneField(User, on_delete=models.PROTECT) # if i try to delete user from USer it will not getting delete untill and unless it hold profile...

#   user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}) # only is staff user can create profile

#   user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
#   name = models.CharField(max_length=100)
#   email = models.EmailField(max_length=100)
#   city = models.CharField(max_length=100)
#   def __str__(self):
#     return self.name

# class page(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   page_name = models.CharField(max_length=100)
#   def __str__(self):
#     return self.name

# class like(page):
#   user = models.OneToOneField(page, on_delete=models.CASCADE, paresrent_link=True)
#   likes = models.IntegerField()
#   def __str__(self):
#     return self.name



# 2. many to one:

class post(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  # user = models.ForeignKey(User, on_delete=models.PROTECTED)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # doesn't delete post if user is deleted , owner of post will be null
  title = models.CharField(max_length=100)
  content = models.TextField()
  def __str__(self):
    return self.title

# class comment(models.Model):
#   post = models.ForeignKey(post, on_delete=models.CASCADE)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   comment = models.TextField()
#   def __str__(self):
#     return self.comment



# 3. Many to Many : saperate table will be created

# class userprofile(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   group = models.ForeignKey(Group, on_delete=models.CASCADE)
#   def __str__(self):
#     return self.user

# class post(models.Model):
#   user = models.ManyToManyField(User)
#   title = models.CharField(max_length=100)
#   content = models.TextField()
#   def __str__(self):
#     return self.title

    # def writen_by(self):
    #   return ', '.join([str(p) for p in self.user.all()])