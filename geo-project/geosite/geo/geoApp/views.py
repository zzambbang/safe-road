from django.shortcuts import render, redirect
import os
import folium
# import pandas as pd
# import psycopg2


# Create your views here.
def home(request):

    #db connection 
    # connection = psycopg2.connect(dbname='postgres',)

    center = [37.541, 126.986]
    m = folium.Map(location=center, zoom_start=10)


    folium.LayerControl().add_to(m)

    m = m._repr_html_()
    context = {'my_map': m}
    return render(request, 'geoApp/home.html', context)