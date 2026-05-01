from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='article_pics/',blank=True,null=True)

    category_choices = (('technology','Technology'),
                        ('lifestyle','Lifestyle'),
                        ('coding','Coding'))

    category = models.CharField(max_length=25, choices=category_choices)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        # Check if old image is present and is not the same as new image, if not then delete it
        ## Get the object of current Article old image
        ## Check if Article contains an image and if old image is same as new image
        try:
            current_article = Article.objects.get(id = self.id)
            if current_article.image and current_article.image != self.image:
                if os.path.isfile(current_article.image.path):
                    os.remove(current_article.image.path)
        except Article.DoesNotExist:
            pass

        # Do the normal saving using the default save method
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)        
        super().delete(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name= 'comment')
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.user.username} at {self.created_at}"