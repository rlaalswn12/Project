import filter as f
import os
import xml.etree.ElementTree as ET


Wafer = str(input("Input wafer name : "))
a = f.call_dir(Wafer, 'LMZ')

for t in a:
    path = os.path.basename(t)
    root = ET.parse(t).getroot()
    print(path)

    element1 = root.find('.//Modulator')
    name = element1.attrib['Name']

    element2 = root.find('.//ModulatorSite')
    operator = element2.attrib['Operator']

    element3 = root.find('.//PortCombo')
    date = element3.attrib['DateStamp']

