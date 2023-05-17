import xml.dom.minidom

domtree = xml.dom.minidom.parse("C:\Users\burgeB9\Desktop\L5X_Editor\MES Core Build\_002_IGNITION_DATA_OVERALL_MACHINE.L5X")

group = domtree.documentElement

Rungs = group.getElementsByTagName('Rung')

for Rung in Rungs:
    print(f"-- Rung {Rung.getAttribute('id')} --")
    
    Rung = Rung.getElementsByTagName('Rung')[0].childNodes[0].nodeValue
    
    print(f"Name: {Rung}")
    
    