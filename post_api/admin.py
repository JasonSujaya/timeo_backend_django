from django.contrib import admin
from .models import Post, PostCategory, PostImages, Tag, PostTag, PostComment, PostBookmark, ReportCategory, PostReport, CommentReport

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostImages)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(PostComment)
admin.site.register(PostBookmark)


admin.site.register(ReportCategory)
admin.site.register(PostReport)
admin.site.register(CommentReport)
