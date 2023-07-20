from mtranslate import translate
import xml.etree.ElementTree as ET
import os


def translate_text(text, target_lang='ru'):
    return translate(text, target_lang)


def translate_specific_tag(xml_paths, tag_name, target_lang='ru', output_directory='translated_output'):
    for xml_path in xml_paths:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for element in root.iter(tag_name):
            if element.text:
                segment_length = 500
                segments = [element.text[i:i + segment_length] for i in range(0, len(element.text), segment_length)]
                translated_text = ' '.join([translate_text(segment, target_lang=target_lang) for segment in segments])
                element.text = translated_text

        # Создаем папку для сохранения переведенных файлов, если она не существует
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Получаем имя файла без расширения
        file_name_without_extension = os.path.splitext(os.path.basename(xml_path))[0]

        # Сохраняем переведенный XML в указанную директорию с именем, как у исходного файла
        translated_xml_filename = f'{file_name_without_extension}.xml'
        translated_xml_path = os.path.join(output_directory, translated_xml_filename)
        tree.write(translated_xml_path, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    xml_file_paths = ['text.xml', 'test1.xml']
    target_tag = 'Text'
    target_language = 'ru'
    output_dir = 'translated_output'
    translate_specific_tag(xml_file_paths, target_tag, target_language, output_directory=output_dir)
