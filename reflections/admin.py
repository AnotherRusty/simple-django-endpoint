from django.contrib import admin
from .models import Reflection
from .models import Question
from .models import QuestionSubmission
from .models import Submission


class ReflectionAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class QuestionSubmissionAdmin(admin.TabularInline):
    model = QuestionSubmission
    fields = []
    readonly_fields = ("question__prompt", "answer")
    extra = 0


class SubmissionAdmin(admin.ModelAdmin):
    inlines = [QuestionSubmissionAdmin]
    readonly_fields = ("reflection", "user")

    list_filter = ["reflection"]


# admin.site.register(QuestionSubmissionAdmin, SubmissionAdmin)
admin.site.register(Reflection, ReflectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission, SubmissionAdmin)

