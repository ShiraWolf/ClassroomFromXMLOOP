import xml.etree.ElementTree as ET


class Child:
    def __init__(self, xml: ET):
        xml_children = list(xml)
        self.child_id = xml_children[0].attrib.get("id")
        data = list(xml_children.pop(0))
        names = [child.text for child in data[0]]
        if len(names) == 3:
            self.full_name = " ".join([names[0], names[-1], names[1]])
        else:
            self.full_name = " ".join(names)
        self.email = data[1].text
        self.hobbies = [child.text for child in xml_children]

    def childXML(self) -> ET.Element:
        childTag = ET.Element("Child")
        childTag = ET.SubElement(childTag, "Child")
        idTag = ET.SubElement(childTag, "ID")
        idTag.text = str(self.child_id)
        nameTag = ET.SubElement(childTag, "Name")
        nameTag.text = str(self.full_name)
        emailTag = ET.SubElement(childTag, "Email")
        emailTag.text = str(self.email)
        return childTag

    def __repr__(self):
        return "%s" % [self.child_id, self.full_name, self.email]
