from django.contrib import admin
from .models import Reflection
from .models import Question
from .models import QuestionSubmission
from .models import Submission


class ReflectionAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class SubmissionAdmin(admin.ModelAdmin):
    pass


class QuestionSubmissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reflection, ReflectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSubmission, QuestionSubmissionAdmin)
admin.site.register(Submission, SubmissionAdmin)

