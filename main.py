import requests
import asyncio
import flask
import xml.etree.ElementTree as ET

from child import Child
from classes import Classes
from teacher import Teacher

# TODO -> GET(flask)
# def getXMLresponse(url):
#     response = requests.get(url)
#     tree = ET.ElementTree.fromstring(response.content)


def get_objects(xml_file: str, name_of_object: str):
    if name_of_object != "Child" and name_of_object != "Teacher":
        return []
    tree = ET.parse(xml_file)
    elements = tree.findall(name_of_object)
    if name_of_object == "Child":
        return [Child(elem) for elem in elements]
    else:
        return [Teacher(elem) for elem in elements]


def get_subjects(teachers: list[Teacher]):
    return [teacher.subject for teacher in teachers]


def get_classes(subjects, children, teachers):
    return [Classes(teachers, children, subject) for subject in subjects]


def parsetoXML(classes_vals, subjects):
    classesTag = ET.Element("Classes")
    classesTag = ET.SubElement(classesTag, "Classes")
    for i in range(len(classes_vals)):
        classesTag.insert(i, classes_vals[i].toXML())
    tree = ET.ElementTree(classesTag)
    tree.write("Classes2.xml", encoding="windows-1252", xml_declaration=True)


def main_fun():
    teachers = get_objects("Teachers.xml", "Teacher")
    children = get_objects("Children.xml", "Child")
    subjects = get_subjects(teachers)
    subjects.extend(["Unknown"])
    classes_vals = get_classes(subjects, children, teachers)
    parsetoXML(classes_vals, subjects)


if __name__ == '__main__':
    main_fun()
