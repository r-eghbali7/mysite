from django.db import models


class post(models.Model):
    # image
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # 2024-09-17 19:02:55.146707
                                                        # 2024-09-17 19:05:49.694708

