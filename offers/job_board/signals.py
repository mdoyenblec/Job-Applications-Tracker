from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobOffer

@receiver(post_save, sender=JobOffer)
def update_job_offer_number(sender, instance, created, **kwargs):
    if created:
        user_job_offers = JobOffer.objects.filter(user=instance.user)
        instance.number = user_job_offers.count()  # Ne pas soustraire 1
        instance.save()

