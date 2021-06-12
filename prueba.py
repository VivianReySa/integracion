import xml.etree.ElementTree as ET  

def deletePd(id_pt):
    tree = ET.parse('productos.xml')
    root = tree.getroot()
    for producto in root.findall('producto'):
        #name = producto.find('nombre').text
        idP = producto.attrib['id']
        if idP == id_pt:
            root.remove(producto)
    tree.write("./productos.xml")
    return id_pt



deletePd("1")

'''
tree = ET.parse('productos.xml')
root = tree.getroot()
#producto = ET.SubElement(root, "producto")
for producto in root.findall('producto'):
    name = producto.find('nombre').text
    if name == 'cereal':
        root.remove(producto)
tree.write("./productos.xml")'''