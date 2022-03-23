from teacher import Teacher
from child import Child
import xml.etree.ElementTree as ET


class Classes:
    def __init__(self, teachers: list[Teacher], children: list[Child], subject: str = "Unknown"):
        self.subject = subject
        if subject != "Unknown":
            self.teacher = self.get_teacher(teachers)
        else:
            self.teacher = None
        self.children = self.get_children(children)
        self.num_children = len(self.children)

    def get_teacher(self, teachers) -> Teacher:
        return [teacher for teacher in teachers if teacher.subject == self.subject][0]

    def get_children(self, children) -> list[Child]:
        if self.subject != "Unknown":
            return [child for child in children if self.subject in child.hobbies]
        else:
            return [child for child in children if len(child.hobbies) == 0]

    def toXML(self) -> ET.Element:
        if self.subject == "Unknown":
            return self.xmlUnknown()
        class1 = ET.Element("Class")
        class1.set("name", str(self.subject))
        class1.set("noOfChildren", str(self.num_children))
        class1.insert(0, self.teacher.teacherXML())
        for i in range(self.num_children):
            class1.insert(1 + i, self.children[i].childXML())
        return class1

    def __repr__(self):
        return "%s" % [self.subject, self.teacher, self.children, self.num_children]

    def xmlUnknown(self) -> ET.Element:
        unknown = ET.Element("Unknown")
        for i in range(self.num_children):
            unknown.insert(1 + i, self.children[i].childXML())
        return unknown
