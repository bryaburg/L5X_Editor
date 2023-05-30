import xml.etree.ElementTree as ET

xmlfile = r"C:\Users\burgeB9\Desktop\L5X_Editor\MES Core Build\_002_IGNITION_DATA_OVERALL_MACHINE.L5X"
tree = ET.parse(xmlfile)
RSLogix5000Content = tree.getroot()

# Change Value in Rung 0
for Rung in RSLogix5000Content.findall(".//Rung[@Number='0']/Text"):
    # Create a new CDATA section as a string
    cdata_section = '<![CDATA[XIC(LNXX_SCHEDULED_RUN)MOV(1,LNXX_TO_DC01_DOWNTIME_CODE[0]);]]>'

    # Update the text content of the <Text> element with the CDATA section
    Rung.text = cdata_section

    print(Rung.tag, Rung.attrib, Rung.text)

# Write the modified tree back to the file
tree.write(xmlfile)
