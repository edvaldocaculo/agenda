from django.shortcuts import render
from contact.models import Contact


contacts = Contact.objects.all().order_by('-id')

context = {'contacts': contacts}
def index(request):
    return render(request, 
                  'contact/pages/index.html',
                  context)
