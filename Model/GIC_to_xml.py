import csv
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.etree.ElementTree as etree

root = Element('root')
number = Element('number')

datafile='GIC-codes1.csv'
with open(datafile) as f:

    root = Element('GIC-code')
    tree = ElementTree(root)
    reader = csv.DictReader(f)
    for row in reader:
        xml_row = SubElement(root, "doc")
        for k in reader.fieldnames:
            child = SubElement(xml_row, k)
            child.text = row[k]

    tree.write(open(r'GIC.xml','w'))
#    print tostring(root)
