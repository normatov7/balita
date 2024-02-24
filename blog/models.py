from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    image = models.ImageField(upload_to="posts/")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    created_atb = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    subject = models.CharField(max_length=120,blank=True,null=True)
    email = models.EmailField()
    message = models.TextField()

    is_solved = models.BooleanField(default=False)

    created_atb = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name