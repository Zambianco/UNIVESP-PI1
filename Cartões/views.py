from django.shortcuts import render
from .models import Flashcard

def card_show(request):
    flashcards = Flashcard.objects.all()
    context = {'flashcards': flashcards}
    return render(request, 'card_list.html', context)
