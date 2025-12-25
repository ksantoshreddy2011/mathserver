from django.shortcuts import render

def rectarea(request):

    context = {}

    context['area'] = "0"
    context['l'] = "0"
    context['b'] = "0"

    if request.method == 'POST':
        print("POST method is used")

        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')

        print('request =', request)
        print('Length =', l)
        print('Breadth =', b)

        try:
            area = int(l) * int(b)
        except ValueError:
            area = 0

        context['area'] = area
        context['l'] = l
        context['b'] = b

        print('Area =', area)

    return render(request, 'mathapp/math.html', context)
