from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

class JobOffer(models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    application_date = models.DateTimeField()
    url = models.URLField(default='https://www.welcometothejungle.com/fr')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

@receiver(post_save, sender=JobOffer)
def update_job_offer_number(sender, instance, created, **kwargs):
    if created:
        user_job_offers = JobOffer.objects.filter(user=instance.user)
        instance.number = user_job_offers.count() - 1  # Adjust for 0-based indexing
        instance.save()
