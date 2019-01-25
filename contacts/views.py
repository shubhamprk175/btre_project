from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, 
        message=message, user_id=user_id)
        contact.save()

        # send_mail(
        #     'Property Inquiry',
        #     'Somebody has inquired for the property: '+listing+'. Please Sign in to admin panel and check',
        #     'pareek.5343@gmail.com',
        #     [realtor_email, 'shubhamst5343@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'You have successfully submitted your inquiry, a realtor will get back to you soon')

        return redirect('/listings/'+listing_id)