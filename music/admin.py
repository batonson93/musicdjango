from django.contrib import admin
from music.models import Article, Single, Album, Video, Actual

class ActualAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(Article)
admin.site.register(Single)
admin.site.register(Album)
admin.site.register(Video)
admin.site.register(Actual, ActualAdmin)