from django.contrib import admin
from .models import Reflection
from .models import Question
from .models import Submission
from .models import QuestionSubmission


class ReflectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reflection, ReflectionAdmin)
admin.site.register(QuestionSubmission, ReflectionAdmin)
admin.site.register(Question, ReflectionAdmin)
admin.site.register(Submission, ReflectionAdmin)
