from django.shortcuts import render
import requests

def home(request):
    if request.GET.get("amount"):
        amount = float(request.GET.get("amount"))
        try:
            url = "https://api.exchangerate-api.com/v4/latest/USD"
            res = requests.get(url)
            data = res.json()
            dollar = data["rates"]["INR"]
            rupees = amount * dollar
            rupees = "\u20B9" + str(round(rupees, 2))
            return render(request, "home.html", {"msg": rupees})
        except Exception as e:
            msg = "Issue: " + str(e)
            return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")
