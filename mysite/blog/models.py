from django.db import models
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=200,unique=True)
    summery=models.CharField(max_length=300)
    content=models.TextField()
    created=models.DateField(auto_now_add=True)
    published=models.BooleanField()
    class Meta:
        ordering=['-created']

        def __unicode__(self):
            return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post',args=[self.slug])
# Create your models here.
