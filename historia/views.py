import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import mifotos, Evento, Participante
from .forms import mifotosForm

# Create your views here.


def inicio(request):
    # return HttpResponse('<h1>Buenviadidid</h1>')
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def institucion(request):
    #revisar las imagenes en institucion

    # eventos = Evento.objects.all()
    fecha = datetime.date.today().year  # , fecha O ANIO actual
    eventos = Evento.objects.filter(fecha__year=fecha).order_by('orden')
    if eventos: # si existe registo continuar
        print("existe")
    else:   # en caso de no haber revisa el dia anterior
        fecha = fecha -1

    eventos = {'eventos': Evento.objects.filter(fecha__year=fecha).order_by('orden')}
    return render(request, 'paginas/institucion.html', {'eventos': eventos})


def mision(request):
    return render(request, 'paginas/mision.html')


def vision(request):
    return render(request, 'paginas/vision.html')


def historia(request):
    lista = []
    # eventos = Evento.objects.all()
    fecha = datetime.date.today().year  # , fecha O ANIO actual
    # Crear lista de los anios desde 1990 hasta el anio actual
    for i in range((fecha), 1989, -1):
        miEvento = str(i) + "-"+str(i+1)
        lista.append(miEvento)
    # print(lista)                  #, Ano seleccionado
    periodo = request.POST.get('selCategoria')
    # print(periodo)
    nperiodo = str(fecha) + "-"+str(fecha+1)
    if periodo:
        fecha = periodo.split('-')[0]
        nperiodo = periodo
    # mydata = Member.objects.all().order_by('firstname').values()
    # mydata = Member.objects.filter(firstname='Emil').values()
    eventos = Evento.objects.filter(fecha__year=fecha).order_by('titulo')

    print("Existe")
    eventos = {'lista': lista, 'eventos': Evento.objects.filter(
    fecha__year=fecha).order_by('orden'), 'anio': nperiodo}
 
    return render(request, 'paginas/historia.html', {'eventos': eventos})


def autores(request):
    participantes = Participante.objects.all()
    return render(request, 'paginas/autores.html', {'participantes': participantes})


def servicios(request):
    return render(request, 'paginas/servicios.html')


def contactanos(request):
    return render(request, 'paginas/contactanos.html')


def fotos(request):
    fotos = mifotos.objects.all()
    print(fotos)
    return render(request, 'registros/index.html', {'fotos': fotos})


def crear(request):
    # formulario = mifotosForm(request.Post or None)
    # return render(request, 'registros/crear.html', {'formulario': formulario})
    return render(request, 'registros/crear.html')


def editar(request):
    return render(request, 'registros/editar.html')
