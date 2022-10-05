import random
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    prop = {
        "res": []
    }
    if request.method == "GET":
        print("get")
    elif request.method == 'POST':
        print("post")

        prop["res"] = tarot()
        print(prop["res"])

    return render(request, "tarot_game/index.html", prop)

def tarot():
    # kuji2 のリストを作成
    kuji0=["愚者","魔術師","女教皇","女帝","皇帝","法王","恋人","戦車","力","隠者","運命の輪","正義","刑死者","死神","節制","悪魔","塔","星","月","太陽","審判","世界"]
    kuji1=["正位置","逆位置"]

    kuji2 = ["A","2","3","4","5","6","7","8","9","10","王子","騎士","女王","王",]
    kuji3 = ["ワンド","カップ","ソード","ペンタクル"]
    kuji4 = ["正位置","逆位置"]


    # random_number という名前の変数に、0 1 2 の数字をランダムでいれる
    random_number0 = random.randint(0, 21)
    random_number1 = random.randint(0, 1)
    random_number2 = random.randint(0, 13)
    random_number3 = random.randint(0, 3)
    random_number4 = random.randint(0, 1)

    # random_number を kujiリストの番号に指定すると...
    return [ kuji0[ random_number0 ], kuji1[ random_number1 ], kuji2[ random_number2 ], kuji3[ random_number3 ], kuji4[ random_number4 ] ]
