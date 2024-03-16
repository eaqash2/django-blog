from django.conf import settings
from django.db import models
from django.utils.translation import pgettext_lazy


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=pgettext_lazy("author field name", "author"),
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name=pgettext_lazy("title field name", "title"),
        max_length=200
    )
    '''content = models.TextField(
        #verbose_name=pgettext_lazy("content field name", "content"),
        models.ForeignKey('Content', on_delete=models.CASCADE,)
    )'''
    created_at = models.DateTimeField(
        verbose_name=pgettext_lazy("created_at field name", "created at"),
        auto_now_add=True
    )


    class Meta:
        verbose_name = pgettext_lazy("verbose name for posts", "post")
        verbose_name_plural = pgettext_lazy("verbose name plural for posts", "posts")

    def __str__(self) -> str:
        return self.title


'''Table Content{
  id integer [primary key]
  post_id integer
  text text
  main_image varchar(100)
}'''



class Content(models.Model):
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE,
        verbose_name=pgettext_lazy("post_id field name", "post_id")
    )
    main_image = models.ImageField(
        verbose_name=pgettext_lazy("main_image field name", "main_image"),
        max_length=100,
        upload_to='images/'
    )
    text = models.TextField(
        verbose_name=pgettext_lazy("text field name", "text"),
    )

    class Meta:
        verbose_name = pgettext_lazy("verbose name for contents", "content")
        verbose_name_plural = pgettext_lazy("verbose name plural for contents", "contents")

    def __str__(self) -> str:
        return self.post_id.title


'''Table Image{
  id integer [primary key]
  content_id integer
  image varchar(100)
}'''

class Image(models.Model):
    content_id = models.ForeignKey(Content,
        verbose_name=pgettext_lazy("content_id field name", "content_id"),
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        verbose_name=pgettext_lazy("image field name", "image"),
        max_length=100, null=True,
        upload_to='images/'
    )

    class Meta:
        verbose_name = pgettext_lazy("verbose name for images", "image")
        verbose_name_plural = pgettext_lazy("verbose name plural for images", "images")

    def __str__(self) -> str:
        return f'{self.image}'
