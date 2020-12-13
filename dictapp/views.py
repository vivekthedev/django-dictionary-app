from django.shortcuts import render, redirect
from .forms import Word
from PyDictionary import PyDictionary
# Create your views here.

def index(request):
    form = Word()
    meaning = ""
    synonym = ""
    antonym = ""
    dictionary=PyDictionary()

    if request.method == "POST":
        form = Word(request.POST)
        if form.is_valid():
            word = form.cleaned_data["wordInput"]
            meaning = dictionary.meaning(word)
            synonym = dictionary.synonym(word)
            antonym = dictionary.antonym(word)
            meaning, synonym, antonym = str(meaning), str(synonym), str(antonym) 
            redirect('/')

    context = {'form' : form, 'meaning' : meaning, 'synonym' : synonym, 'antonym' : antonym}
    return render(request, 'dictapp/index.html', context)