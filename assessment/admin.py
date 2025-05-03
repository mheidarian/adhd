from django.contrib import admin
from .models import Test, Question, Choice, Result, Answer, ThresholdSettings


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    min_num = 4
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test', 'order')
    list_filter = ('test',)
    search_fields = ('text',)
    ordering = ('test', 'order')
    inlines = [ChoiceInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'get_question_count')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'instructions')
        }),
    )
    inlines = [QuestionInline]


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ('question', 'choice')
    can_delete = False


class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'score', 'date_taken', 'get_interpretation')
    list_filter = ('test', 'date_taken')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('user', 'test', 'score', 'date_taken')
    inlines = [AnswerInline]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ThresholdSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated')
    fieldsets = (
        ('تنظیمات آستانه‌ها', {
            'fields': ('low_threshold', 'medium_threshold'),
            'description': 'آستانه‌های تشخیص ADHD را تنظیم کنید. اگر امتیاز کمتر یا مساوی "آستانه پایین" باشد، احتمال ADHD کم محسوب می‌شود. '
                           'اگر امتیاز بین "آستانه پایین" و "آستانه متوسط" باشد، احتمال ADHD متوسط، و اگر بالاتر از "آستانه متوسط" باشد، '
                           'احتمال ADHD بالا در نظر گرفته می‌شود.'
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance of settings
        if ThresholdSettings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Don't allow deleting the settings
        return False


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(ThresholdSettings, ThresholdSettingsAdmin)
