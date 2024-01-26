from django.shortcuts import render, redirect
from contact.models import Contact
from django.shortcuts import get_object_or_404
from django.db.models import Q


def index(request):
    contacts = Contact.objects\
            .filter(show=True)\
            .order_by('-id')[:10]

    context = {'contacts': contacts}
    return render(request, 
                  'contact/pages/index.html',
                  context)

def contact(request, contact_id):
    single_contact = get_object_or_404(
                    Contact.objects
                    .filter(id=contact_id, show=True)
                    )

    context = {'contact': single_contact}
    return render(request,
                  'contact/pages/contact.html',
                  context)

def search(request):

    search_term = request.GET.get('q', '').strip()
    if search_term == '':
        return redirect('contact:index')
    
    contacts = Contact.objects\
            .filter(show=True)\
            .filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(phone__icontains=search_term)
            )\
            .order_by('-id')

    context = {'contacts': contacts}
    return render(request, 
                  'contact/pages/index.html',
                  context)