import xml.etree.ElementTree as ET

# Загружаем первый XML файл с указанием кодировки UTF-8
tree1 = ET.parse('test1.xml', parser=ET.XMLParser(encoding='utf-8'))
root1 = tree1.getroot()

# Загружаем второй XML файл с указанием кодировки UTF-8
tree2 = ET.parse('test.xml', parser=ET.XMLParser(encoding='utf-8'))
root2 = tree2.getroot()

# Меняем значения в теге Text у каждого элемента второго файла на значения из первого файла
for elem1, elem2 in zip(root1.iter('OptionText'), root2.iter('OptionText')):
    elem2.text = elem1.text

# Сохраняем изменения обратно во второй XML файл с указанием кодировки UTF-8
tree2.write('test.xml', encoding='utf-8')
