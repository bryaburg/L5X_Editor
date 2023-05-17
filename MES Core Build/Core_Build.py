import xml.etree.ElementTree as ET

xmlfile = (r"C:\Users\burgeB9\Desktop\L5X_Editor\MES Core Build\_002_IGNITION_DATA_OVERALL_MACHINE.L5X")
tree = ET.parse(xmlfile)
RSLogix5000Content = tree.getroot()

#ET.dump(tree)

# Select Rung 0
Rung0 = RSLogix5000Content.find(".//Rung[@Number= '0']/Text")
print(Rung0.tag, Rung0.attrib, Rung0.text)

# Change Value in Rung 0 

for Rung in RSLogix5000Content.findall(".//Rung[@Number= '0']/Text"):
    Rung.text = "XIC(LNXX_SCHEDULED_RUN)MOV(0,LNXX_TO_DC01_DOWNTIME_CODE[0]);"
    print(Rung.tag, Rung.attrib, Rung.text)
    ET.SubElement(Rung, "")
