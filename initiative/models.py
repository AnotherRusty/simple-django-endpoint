from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Initiative(models.Model):
    title = models.TextField()
    description = models.TextField()
    team_leader = models.ForeignKey(User, on_delete=models.PROTECT)
    completion = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    timeline = models.TextField(blank=True)


class StatusReport(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='goals',
        related_query_name='Post',)
    date = models.DateField(auto_now=True)

    class Meta: # new
        verbose_name = 'goal'
        verbose_name_plural = 'goals'

    def __str__(self):
        return '%s %s' % (self.author, self.content)

    def get_absolute_url(self):
        return reverse('initiative:status', args=[str(self.id)])

