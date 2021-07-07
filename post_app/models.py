from django.db import models
from user_app.models import RedditUser
from django.utils import timezone


# Constructed Mixin for both Post and Comment
class CommonFieldsMixin(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_by = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def like_dislike(self):
        return self.like - self.dislike

    class Meta:
        abstract = True


class Comment(CommonFieldsMixin, models.Model):
    ''' 
        The common mixin contants all we'd need for comments so it just passes
    '''
    pass

class Post(CommonFieldsMixin, models.Model):
    ''' 
        Special information for the Posts
    '''
    title = models.CharField(max_length=150)
    url_post = models.URLField()
    comments = models.ManyToManyField(Comment, symmetrical=False, blank=True)
