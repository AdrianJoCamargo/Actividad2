import xml.etree.ElementTree as ET
from tkinter import Tk, Button, Frame,Label

tree=ET.parse('ejemplo1.xml')
root= tree.getroot()

#Declaracion de clases
class Armamento:
    def __init__(self,dur):
        self.duracion=dur

class Armadura(Armamento):
    def __init__(self,mat,dur,res):
        self.material=mat
        self.duracion=dur
        self.resistencia=res

class Armas(Armamento):
    def __init__(self,dañ,dur):
        self.daño=dañ
        self.duracion=dur

class Espadas(Armas):
    def __init__(self,mate,dur,daño):
        self.material=mate
        self.duracion=dur
        self.daño=daño

#Declaracion de atributos junto con objetos
#############  CASCOS  #############

for i in root.iter('duracionCC'):
    du=i.text
for i in root.iter('resistenciaCC'):
    re=i.text
CascoCuero=Armadura("Cuero",du,re)

for i in root.iter('duracionCO'):
    du=i.text
for i in root.iter('resistenciaCO'):
    re=i.text
CascoOro=Armadura("Oro",du,re)

for i in root.iter('duracionCH'):
    du=i.text
for i in root.iter('resistenciaCH'):
    re=i.text
CascoHierro=Armadura("Hierro",du,re)

for i in root.iter('duracionCD'):
    du=i.text
for i in root.iter('resistenciaCD'):
    re=i.text
CascoDiamante=Armadura("Diamante",du,re)

for i in root.iter('duracionCI'):
    du=i.text
for i in root.iter('resistenciaCI'):
    re=i.text
CascoInframundita=Armadura("Inframundita",du,re)

#############  PECHERAS  #############

for i in root.iter('duracionPC'):
    du=i.text
for i in root.iter('resistenciaPC'):
    re=i.text
PecheraCuero=Armadura("Cuero",du,re)

for i in root.iter('duracionPO'):
    du=i.text
for i in root.iter('resistenciaPO'):
    re=i.text
PecheraOro=Armadura("Oro",du,re)

for i in root.iter('duracionPH'):
    du=i.text
for i in root.iter('resistenciaPH'):
    re=i.text
PecheraHierro=Armadura("Hierro",du,re)

for i in root.iter('duracionPD'):
    du=i.text
for i in root.iter('resistenciaPD'):
    re=i.text
PecheraDiamante=Armadura("Diamante",du,re)

for i in root.iter('duracionPI'):
    du=i.text
for i in root.iter('resistenciaPI'):
    re=i.text
PecheraInframundita=Armadura("Inframundita",du,re)

#############  PANTALONES  #############

for i in root.iter('duracionPTC'):
    du=i.text
for i in root.iter('resistenciaPTC'):
    re=i.text
PantalonCuero=Armadura("Cuero",du,re)

for i in root.iter('duracionPTO'):
    du=i.text
for i in root.iter('resistenciaPTO'):
    re=i.text
PantalonOro=Armadura("Oro",du,re)

for i in root.iter('duracionPTH'):
    du=i.text
for i in root.iter('resistenciaPTH'):
    re=i.text
PantalonHierro=Armadura("Hierro",du,re)

for i in root.iter('duracionPTD'):
    du=i.text
for i in root.iter('resistenciaPTD'):
    re=i.text
PantalonDiamante=Armadura("Diamante",du,re)

for i in root.iter('duracionPTI'):
    du=i.text
for i in root.iter('resistenciaPTI'):
    re=i.text
PantalonInframundita=Armadura("Inframundita",du,re)

#############  BOTAS  #############

for i in root.iter('duracionBC'):
    du=i.text
for i in root.iter('resistenciaBC'):
    re=i.text
BotasCuero=Armadura("Cuero",du,re)

for i in root.iter('duracionBO'):
    du=i.text
for i in root.iter('resistenciaBO'):
    re=i.text
BotasOro=Armadura("Oro",du,re)

for i in root.iter('duracionBH'):
    du=i.text
for i in root.iter('resistenciaBH'):
    re=i.text
BotasHierro=Armadura("Hierro",du,re)

for i in root.iter('duracionBD'):
    du=i.text
for i in root.iter('resistenciaBD'):
    re=i.text
BotasDiamante=Armadura("Diamante",du,re)

for i in root.iter('duracionBI'):
    du=i.text
for i in root.iter('resistenciaBI'):
    re=i.text
BotasInframundita=Armadura("Inframundita",du,re)

#############  ESPADAS  #############

for i in root.iter('duracionEM'):
    du=i.text
for i in root.iter('dañoEM'):
    da=i.text
EspadaMadera=Espadas("Madera",du,da)

for i in root.iter('duracionEO'):
    du=i.text
for i in root.iter('dañoEO'):
    da=i.text
EspadaOro=Espadas("Oro",du,da)

for i in root.iter('duracionEP'):
    du=i.text
for i in root.iter('dañoEP'):
    da=i.text
EspadaPiedra=Espadas("Piedra",du,da)

for i in root.iter('duracionEP'):
    du=i.text
for i in root.iter('dañoEP'):
    da=i.text
EspadaPiedra=Espadas("Piedra",du,da)

for i in root.iter('duracionEH'):
    du=i.text
for i in root.iter('dañoEH'):
    da=i.text
EspadaHierro=Espadas("Hierro",du,da)

for i in root.iter('duracionED'):
    du=i.text
for i in root.iter('dañoED'):
    da=i.text
EspadaDiamante=Espadas("Diamante",du,da)

for i in root.iter('duracionEI'):
    du=i.text
for i in root.iter('dañoEI'):
    da=i.text
EspadaInframundita=Espadas("Inframundita",du,da)

#############  GRAFICO  #############
class Test():
    def __init__(self):
        self.vent=Tk()
        self.vent.title("Orden de datos")
        self.vent.geometry("600x1080")

        self.bt1=Button(self.vent,text='>')
        self.bt1.place(x=10,y=10,width=20,height=30)

        self.lbl1= Label(self.vent,text="Armamaneto")
        self.lbl1.place(x=30,y=10,width=100,height=30)
        #ARMADURA
        self.lbl2 = Label(self.vent, text="Armadura")
        self.lbl2.place(x=50, y=40, width=100, height=30)
        #CASCOS
        self.lbl3 = Label(self.vent, text="Equipamiento cuero")
        self.lbl3.place(x=75, y=70, width=120, height=30)
        #Cabeza
        self.lbl4 = Label(self.vent, text="Casco de cuero")
        self.lbl4.place(x=95, y=100, width=120, height=30)
        self.lbl4 = Label(self.vent, text="Duracion: "+CascoCuero.duracion)
        self.lbl4.place(x=125, y=130, width=100, height=30)
        self.lbl5 = Label(self.vent, text="Resistencia: " + CascoCuero.resistencia)
        self.lbl5.place(x=132, y=160, width=100, height=30)
        #Pechera
        self.lbl6 = Label(self.vent, text="Pechera de cuero")
        self.lbl6.place(x=100, y=190, width=120, height=30)
        self.lbl7 = Label(self.vent, text="Duracion: " +PecheraCuero.duracion)
        self.lbl7.place(x=125, y=220, width=100, height=30)
        self.lbl8 = Label(self.vent, text="Resistencia: " + PecheraCuero.resistencia)
        self.lbl8.place(x=127, y=250, width=100, height=30)
        #Pantalones
        self.lbl9 = Label(self.vent, text="Pantalones de cuero")
        self.lbl9.place(x=110, y=280, width=120, height=30)
        self.lbl10 = Label(self.vent, text="Duracion: " + PantalonCuero.duracion)
        self.lbl10.place(x=129, y=310, width=100, height=30)
        self.lbl11= Label(self.vent, text="Resistencia: " + PantalonCuero.resistencia)
        self.lbl11.place(x=127, y=340, width=100, height=30)
        #Botas
        self.lbl12 = Label(self.vent, text="Botas de cuero")
        self.lbl12.place(x=105, y=370, width=100, height=30)
        self.lbl13 = Label(self.vent, text="Duracion: " + BotasCuero.duracion)
        self.lbl13.place(x=125, y=400, width=100, height=30)
        self.lbl14 = Label(self.vent, text="Resistencia: " + BotasCuero.resistencia)
        self.lbl14.place(x=127, y=430, width=100, height=30)

        #Segunda rama
        self.lbl20 = Label(self.vent, text="Equipamiento Hierro")
        self.lbl20.place(x=75, y=460, width=120, height=30)
        # Cabeza
        self.lbl21 = Label(self.vent, text="Casco de hierro")
        self.lbl21.place(x=95, y=490, width=120, height=30)
        self.lbl22 = Label(self.vent, text="Duracion: " + CascoHierro.duracion)
        self.lbl22.place(x=125, y=520, width=100, height=30)
        self.lbl23 = Label(self.vent, text="Resistencia: " + CascoHierro.resistencia)
        self.lbl23.place(x=132, y=550, width=100, height=30)
        # Pechera
        self.lbl24 = Label(self.vent, text="Pechera de hierro")
        self.lbl24.place(x=100, y=580, width=120, height=30)
        self.lbl25 = Label(self.vent, text="Duracion: " + PecheraHierro.duracion)
        self.lbl25.place(x=125, y=610, width=100, height=30)
        self.lbl26 = Label(self.vent, text="Resistencia: " + PecheraHierro.resistencia)
        self.lbl26.place(x=127, y=640, width=100, height=30)
        # Pantalones
        self.lbl27 = Label(self.vent, text="Pantalones de hierro")
        self.lbl27.place(x=110, y=670, width=120, height=30)
        self.lbl28 = Label(self.vent, text="Duracion: " + PantalonHierro.duracion)
        self.lbl28.place(x=129, y=700, width=100, height=30)
        self.lbl29 = Label(self.vent, text="Resistencia: " + PantalonHierro.resistencia)
        self.lbl29.place(x=127, y=730, width=100, height=30)
        # Botas
        self.lbl210 = Label(self.vent, text="Botas de hierro")
        self.lbl210.place(x=105, y=760, width=100, height=30)
        self.lbl211 = Label(self.vent, text="Duracion: " + BotasHierro.duracion)
        self.lbl211.place(x=125, y=790, width=100, height=30)
        self.lbl212= Label(self.vent, text="Resistencia: " + BotasHierro.resistencia)
        self.lbl212.place(x=127, y=820, width=100, height=30)

        # tercera rama
        self.lbl2 = Label(self.vent, text="Arma")
        self.lbl2.place(x=35, y=850, width=100, height=30)
        self.lbl20 = Label(self.vent, text="Espada")
        self.lbl20.place(x=40, y=880, width=120, height=30)
        self.lbl210 = Label(self.vent, text="Espada de hierro")
        self.lbl210.place(x=105, y=910, width=100, height=30)
        self.lbl211 = Label(self.vent, text="Duracion: " + EspadaHierro.duracion)
        self.lbl211.place(x=125, y=940, width=100, height=30)
        self.lbl212 = Label(self.vent, text="Daño: " + EspadaHierro.daño)
        self.lbl212.place(x=110, y=970, width=100, height=30)

        self.vent.mainloop()

app=Test()