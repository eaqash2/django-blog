from django.contrib import admin

from post import models

from post.models import Content, Image

class ImageInline(admin.StackedInline):
    model = Image
    show_change_link = True
    extra = 1


class ContentInline(admin.StackedInline):
    #inlines = [ImageInline]
    model = Content
    extra = 1
    show_change_link = True



class ImageAdmin(admin.ModelAdmin):
    list_display = ["title",]
    def title(self, obj):
        return obj

class ContentAdmin(admin.ModelAdmin):
    list_display = [models.Content.post_id.field.name,
                    models.Content.text.field.name,
                    models.Content.main_image.field.name]
    inlines = [ImageInline]
    def title(self, obj):
        return obj


class PostAdmin(admin.ModelAdmin):
    inlines = [ContentInline,]
    list_display = [
        "title",
        models.Post.author.field.name,
        models.Post.created_at.field.name,
    ]
    readonly_fields = [
        models.Post.created_at.field.name,
    ]



    def title(self, obj):
        return obj

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Content, ContentAdmin)
#admin.site.register(Content)
admin.site.register(models.Image, ImageAdmin)
