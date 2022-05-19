import filter as f
import os
import xml.etree.ElementTree as ET
import pandas as pd


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

    element4 = root.find('.//TestSiteInfo')
    batch = element4.attrib['Batch']
    testsite = element4.attrib['TestSite']
    maskset = element4.attrib['Maskset']
    dierow = element4.attrib['DieRow']
    diecolumn = element4.attrib['DieColumn']

    T = []
    for child in root.find('.//DesignParameters'):
        T.append(list(map(float, child.text.split(','))))
    AnalysisWavelength = (T[1][0])

    rawValues = []
    for child in root.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement'):
        rawValues.append(list(map(float, child.text.split(','))))

    IatV1 = rawValues[1][12]
    IatminV1 = rawValues[1][4]

    print(name)
    print(operator)
    print(date)
    print(batch)
    print(testsite)
    print(maskset)
    print(dierow)
    print(diecolumn)
    print(AnalysisWavelength)
    print(IatV1)
    print(IatminV1)




