from django.shortcuts import render
import requests
from edt.models import EdtWeek, Edt

# reload json, and rewrite database with new data


def load(request):
    Edt.objects.all().delete()
    EdtWeek.objects.all().delete()
    import json
    matin = None
    Semaine = 0
    url = 'https://api.alternancerouen.fr/planification/session/2290160.json'
    response = requests.get(url)
    data = json.loads(response.text)
    j = 0
    for i in data:
        edt = Edt(
            CodeSeance=i['CodeSeance'],
            NomSession=i['NomSession'],
            NomMatiere=i['NomMatiere'],
            ThemeSeance=i['ThemeSeance'],
            IntervenantNom=i['IntervenantNom'],
            IntervenantPrenom=i['IntervenantPrenom'],
            DebutSeance=i['DebutSeance'],
            FinSeance=i['FinSeance'],
            NomSalle=i['NomSalle'],
        )
        j += 1
        if j == 1 or j == 10:
            try:
                if j == 1:
                    matin = i['DebutSeance']
                    Semaine = Semaine + 1
                if j == 10:
                    soir = i['FinSeance']
                    j = 0
                    edtWeek = EdtWeek(
                        DebutSeance=matin,
                        FinSeance=soir,
                        Semaine=Semaine,
                    )
                    edtWeek.save()

            except Exception as e:
                print(e)
        edt.Semaine = Semaine
        edt.save()
    return render(request, 'index.html')


# Retrieve data in db to display in html

def loadWeek(request, week):
    if week < 1:
        week = 1
    if week > 15:
        week = 15
    edtWeek = EdtWeek.objects.get(Semaine=week)
    edt = Edt.objects.filter(DebutSeance__range=(edtWeek.DebutSeance, edtWeek.FinSeance))

    return render(request, 'edt.html',
                  {'edtWeek': edtWeek, 'lastWeek': edtWeek.Semaine - 1, 'nextWeek': edtWeek.Semaine + 1, 'edt': edt})


def index(request):
    return render(request, 'index.html')
