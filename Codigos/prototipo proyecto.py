import xml.etree.ElementTree as ET

def generar_factura_electronica(emisor, receptor, productos, impuestos):
  """Genera una factura electrónica en formato XML.

  Args:
    emisor: Información del emisor de la factura electrónica.
    receptor: Información del receptor de la factura electrónica.
    productos: Lista de productos o servicios vendidos.
    impuestos: Lista de impuestos aplicables.

  Returns:
    El archivo XML de la factura electrónica.
  """

  # Crear el elemento raíz de la factura electrónica.
  factura = ET.Element("FacturaElectronica", {"version": "1.0"})

  # Agregar el emisor de la factura electrónica.
  emisor_tag = ET.SubElement(factura, "Emisor")
  emisor_tag.text = emisor

  # Agregar el receptor de la factura electrónica.
  receptor_tag = ET.SubElement(factura, "Receptor")
  receptor_tag.text = receptor

  # Agregar los productos o servicios vendidos.
  for producto in productos:
    producto_tag = ET.SubElement(factura, "Producto")
    producto_tag.text = producto

  # Agregar los impuestos aplicables.
  for impuesto in impuestos:
    impuesto_tag = ET.SubElement(factura, "Impuesto")
    impuesto_tag.text = impuesto

  # Convertir el árbol XML a una cadena.
  factura_xml = ET.tostring(factura)

  return factura_xml


# Ejemplo de uso.
emisor = "Empresa XYZ"
receptor = "Cliente ABC"
productos = ["Producto 1", "Producto 2"]
impuestos = ["IVA 19%", "ICE 5%"]

factura_xml = generar_factura_electronica(emisor, receptor, productos, impuestos)

# Imprimir la factura electrónica.
print(factura_xml)
