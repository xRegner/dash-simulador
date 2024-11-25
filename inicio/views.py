from django.shortcuts import render
from .utils import sumar


def inicio(request):
    return render(request, 'inicio/inicio.html')

def contacto(request):
    resultado = None  # Inicializamos el resultado como None

    if request.method == 'POST':
        # Obtenemos los números enviados por el formulario
        numero1 = request.POST.get('numero1')
        numero2 = request.POST.get('numero2')
        
        try:
            # Usamos la función sumar desde utils.py
            resultado = sumar(numero1, numero2)
        except ValueError as e:
            # Si ocurre un error, mostramos un mensaje en el resultado
            resultado = str(e)

    # Pasamos el resultado al template
    return render(request, 'inicio/contacto.html', {'resultado': resultado})


def grafica(request):
    return render(request, 'inicio/grafica.html')