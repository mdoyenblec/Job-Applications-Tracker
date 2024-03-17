from django.shortcuts import render, redirect, get_object_or_404
from .models import JobOffer
from .forms import JobOfferForm
from django.db.models import F


def dashboard(request):
    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():
            job_offer = form.save(commit=False)
            job_offer.user = request.user
            # Générer automatiquement le numéro
            job_offer.number = JobOffer.objects.filter(user=request.user).count() + 1
            job_offer.save()
            return redirect('dashboard')
        else:
            print("Erreurs de formulaire :", form.errors)
    else:
        form = JobOfferForm()
    
    num_offers = 0
    if request.user.is_authenticated:
        job_offers = JobOffer.objects.filter(user=request.user)
        num_offers = job_offers.count()
    else:
        job_offers = []

    return render(request, 'registration/dashboard.html', {'job_offers': job_offers, 'form': form, 'num_offers': num_offers})



def delete_job_offer(request, job_offer_id):
    job_offer = JobOffer.objects.get(id=job_offer_id)
    job_offer.delete()

    # Mettre à jour les numéros des offres restantes
    JobOffer.objects.filter(user=request.user, number__gt=job_offer.number).update(number=F('number') - 1)

    return redirect('dashboard')


