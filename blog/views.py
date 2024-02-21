from django.shortcuts import render, redirect
from .models import Post, Comment, Contact, Category


def home_view(request):
    posts = Post.objects.filter(is_published=True)
    categores = Category.objects.all()

    d = {
        'posts': posts,
        'categores':categores
    }
    return render(request, 'index.html', context=d)

def category_view(request):
    return render(request, 'category.html')



def blog_single_view(request, pk):

    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data['name'], email=data['email'], website=data['website'], message=data['message'])
        obj.save()
        return redirect(f'/blog-single/{pk}/')
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'blog-single.html', context={'post':post, 'comments':comments})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    print("=" * 50)
    print(request.method)
    print("=" * 50)

    if request.method == "POST":
        data = request.POST
        obj = Contact.objects.create(name=data.get('name'),  phone_number=data.get('phone_number'), email=data.get('email'),
                                     message=data.get('message'), subject=data.get('subject'))

        obj.save()

        #telegram notify
        # token = "6256225356:AAHJeyuEZVwQ-_RllJZHtkQqQtnWbQB69p8"
        # requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=&text')


        return redirect('/contact')
    return render(request, 'contact.html')