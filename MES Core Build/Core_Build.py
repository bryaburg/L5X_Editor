import xml.etree.ElementTree as ET

xmlfile = "_002_IGNITION_DATA_OVERALL_MACHINE.L5X"
tree = ET.parse(xmlfile)
root = tree.getroot()

p = tree.find("./Controller/Programs/Program/Routines/Routine/RLLContent/Rung/Text")
#p.text = 'XIO(LNXX_SCHEDULED_RUN)MOV(1,LNXX_TO_DC01_DOWNTIME_CODE[0])'
print(p.text)
