from django.shortcuts import render

# Create your views here.
def homepage(request):
    # print(request.user.is_autheticated)
    if 'search' in request.session:
        del request.session['search']
    if 'field' in request.session:
        del request.session['field']
    if 'category' in request.session:
        del request.session['category']
    return render(request,'homepage.html')