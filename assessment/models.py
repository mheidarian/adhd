from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import uuid


class ThresholdSettings(models.Model):
    low_threshold = models.IntegerField(default=20, verbose_name="آستانه پایین")
    medium_threshold = models.IntegerField(default=40, verbose_name="آستانه متوسط")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "تنظیمات آستانه‌های ADHD"
        verbose_name_plural = "تنظیمات آستانه‌های ADHD"

    def __str__(self):
        return f"تنظیمات آستانه‌ها (کم: {self.low_threshold}, متوسط: {self.medium_threshold})"

    @classmethod
    def get_thresholds(cls):
        """Return the current threshold settings, creating default values if none exist"""
        settings, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'low_threshold': 20,
                'medium_threshold': 40
            }
        )
        return settings


class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_question_count(self):
        return self.questions.count()


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.test.title} - سؤال {self.order}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=8, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            # Generate a unique ID if not already set
            self.unique_id = str(uuid.uuid4().hex[:8]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.test.title} - {self.unique_id}"

    def get_interpretation(self):
        # Get dynamic thresholds from settings
        thresholds = ThresholdSettings.get_thresholds()

        # براساس امتیاز، تفسیر نتیجه آزمون را برمی‌گرداند
        if self.score <= thresholds.low_threshold:
            return "احتمال ADHD کم"
        elif self.score <= thresholds.medium_threshold:
            return "احتمال ADHD متوسط"
        else:
            return "احتمال ADHD بالا"

    def send_result_email(self):
        subject = f'نتیجه آزمون ADHD: {self.user.username}'
        message = f"""
        کاربر: {self.user.get_full_name() or self.user.username}
        ایمیل: {self.user.email}
        آزمون: {self.test.title}
        تاریخ: {self.date_taken}
        امتیاز: {self.score}
        تفسیر: {self.get_interpretation()}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        return True


class Answer(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.result.user.username} - {self.question.text[:30]} - {self.choice.text}"
