from .Dis_Test import RFTest()




def predictdis(request):
    b = request.POST.get('sym')
    d = RFTest()
    dict1 = {}
    a = []
    str = ''
    for i in b:
        str += i
        if i == ' ':
            a.append(int(str))
            str = ''
    a.append(int(str))
        
    # print(a)
    # a = list(map(int, input().split()))
    x = len(a)
    for i in  range(x,17):
        a.append(0)
    print(a)
    
    result = d.RF_Predict(a)[0]
    dict1 = {
        'a':result,
    }
    print(result)
    return render(request, 'FindMyDoc.html', dict1)