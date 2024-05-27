from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        add_enter = request.POST.get('add_enter')
        add_number = request.POST.get('add_number')
        if int(add_number) > 0:
            i = 1
            result = []
            while i <= int(add_number):
                result.append((i, add_enter))
                i += 1

            return render(request, 'home.html', {'result': result})
    else:
        return render(request, 'home.html', {'error': 'error'})
            
    return render(request, 'home.html')

def cal(request):
    if request.method == "POST":
        
        add_number = int(request.POST.get("number"))
        
        results = []
        for i in range(1, 11):
            results.append(add_number * i)
        
        return render(request, 'cal.html', {'number': add_number, 'results': results})

    return render(request, 'cal.html')
