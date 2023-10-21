from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

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
        relator_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            if has_contacted := Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            ):
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect(f'/listings/{listing_id}')
            
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'dummyemail397guest@gmail.com',
            [relator_email, 'delovelo3@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Your request has been submitted, a relator will get back to you soon')
        return redirect(f'/listings/{listing_id}')
