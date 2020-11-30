from django.shortcuts import render
#from django.http import HttpResponse

def buku(request):
    # judul = "Belajar Django"
    # buat list
    judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]
    penulis = "Budi Setiawan"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)

    #def  buku(request):
    #return render(request, 'buku.html')

def penerbit(request):
    return render(request, 'penerbit.html')
