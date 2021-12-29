from blog.models import Post



r = Post(auther = "takuma")
r.save()

print(r.auther)

