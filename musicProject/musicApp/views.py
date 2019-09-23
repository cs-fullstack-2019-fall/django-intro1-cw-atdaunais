from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")


def music(request):
    return HttpResponse(
        f"These are my favorite artists: Brockhampton (/brockhampton), Jacob Collier (/jacobCollier), Active Child (/activeChild).")


def brockhampton(request):
    return HttpResponse(
        "Brockhampton is a self-proclaimed boyband that makes music spanning from hip-hop to pop to rock. They're comprised of several vocalists (rappers and singers) as well as a few producers who all collaborate on every album.")


def jacobCollier(request):
    return HttpResponse("Jacob Collier is a jazz prodigy who explores a wide range of music. He has written jazz, rock, fully orchestrated pieces, electronic music, and everthing in between. He's currently in the midst of a four volume series of albums exploring a different musical 'world' within each individual volume.")


def activeChild(request):
    return HttpResponse("Active Child is an electronic artist, harpist, and vocalist who produces his own music. Most of his music can be considered electronic pop with his soaring falsetto dominating most of the vocal soundscapes.")
