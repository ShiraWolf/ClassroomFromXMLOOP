import xml.etree.ElementTree as ET


class Teacher:
    def __init__(self, xml: ET):
        xml_teachers = list(xml)
        self.name = xml_teachers[0].text
        self.email = xml_teachers[1].text
        self.subject = xml_teachers[-1].text
        self.mobile_phone = ""
        self.work_phone = ""
        self.home_phone = ""
        for elem in xml_teachers:
            if elem.attrib.get("type") == "mobile":
                self.mobile_phone = elem.text
            if elem.attrib.get("type") == "work":
                self.work_phone = elem.text
            if elem.attrib.get("type") == "home":
                self.home_phone = elem.text

    def teacherXML(self) -> ET.Element:
        teacherTag = ET.Element("Teacher")
        teacherTag = ET.SubElement(teacherTag, "Teacher")
        nameTag = ET.SubElement(teacherTag, "Name")
        nameTag.text = str(self.name)
        EmailTag = ET.SubElement(teacherTag, "Email")
        EmailTag.text = str(self.email)
        if self.mobile_phone != "":
            MobilePhone = ET.SubElement(teacherTag, "MobilePhone")
            MobilePhone.text = str(self.mobile_phone)
        if self.work_phone != "":
            WorkPhone = ET.SubElement(teacherTag, "WorkPhone")
            WorkPhone.text = str(self.work_phone)
        if self.home_phone != "":
            HomePhone = ET.SubElement(teacherTag, "HomePhone")
            HomePhone.text = str(self.home_phone)
        return teacherTag

    def __repr__(self):
        return "%s" % [self.name, self.email, self.mobile_phone, self.work_phone, self.home_phone]
