from django.shortcuts import render

# Create your views here.
def home(request):

    context = {'user': request.user}
    conteudos = [
        {
        'autor': 'Vyctor Olineira',
        'categoria': 'Arocha',
        'time': '3 dias atrás · leitura de 5 min ',
        'conteudo': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur sit amet massa fringilla egestas. Nullam condimentum luctus turpis. ',
        'like': '666'
        },
        {
            'autor': 'Vyctor Olineira   ',
            'categoria': 'Lambada',
            'time': '4 dias atrás · leitura de 45 min ',
            'conteudo': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur sit amet massa fringilla egestas. Nullam condimentum luctus turpis. ',
            'like': '66'
        }
    ]
    context['conteudos'] = conteudos
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contato.html')
