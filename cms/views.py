from cms.models import Book
from django.shortcuts import redirect, render
from .forms import TestForm
from .forms import BookAdd

# Create your views here.
def book_list(request):
    """書籍の一覧"""
    books = Book.objects.all().order_by('id')
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'Bashi',
    'form':TestForm(),
    'insert_forms':'初期値',
    'books': books,
    }

    if (request.method == 'POST'):
        my_dict['insert_forms']  = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    return render(request,
                  'cms/book_list.html',     # 使用するテンプレート
                  my_dict)         # テンプレートに渡すデータ

def create(request):
    if (request.method == 'POST'):
        obj = Book()
        info = BookAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/cms/book')
    modelform_dict = {
        'title':'modelformテスト',
        'form':BookAdd(),
    }
    return render(request, 'cms/create.html', modelform_dict)

def update(request, num):
    obj = Book.objects.get(id=num)
    # POST送信されていたら
    if (request.method == 'POST'):
        info = BookAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/cms/book')
    update_dict = {
        'title':'登録情報更新画面',
        'id':num,
        'form':BookAdd(instance=obj),
    }
    return render(request, 'cms/update.html',update_dict)

def delete(request, num):
    obj = Book.objects.get(id=num)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/cms/book')
    delete_dict = {
        'title':'削除確認',
        'id':num,
        'obj':obj,
    }
    return render(request, 'cms/delete.html',delete_dict)