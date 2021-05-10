import os
from pathlib import Path
from lxml import etree as et


def replace_chars(doc, chars_to_replace):
    variable_names = doc.xpath('//variable')
    for variable in variable_names:
        for k, v in chars_to_replace.items():
            variable.attrib['label'] = variable.attrib['label'].replace(k, v)
            variable.attrib['qLabel'] = variable.attrib['qLabel'].replace(k, v)

    table_names = doc.xpath('//table')
    for table in table_names:
        for k, v in chars_to_replace.items():
            table.attrib['title'] = table.attrib['title'].replace(k, v)
            table.attrib['titleWrapped'] = table.attrib['titleWrapped'].replace(k, v)


def main():
    # set this to true if you want to fix characters in all projects
    fix_all_projects = False

    path = Path(r'C:\Users\aturu\CEDMetadata')  # r'C:\Projects\CEDMetadata')

    if fix_all_projects:
        project_list = [project.name for project in path.iterdir() if project.name.endswith('.xml')]
    else:
        # in case you don't want all projects to be checked, you can create a list of selected projects for fixing
        project_list ={'DCM2018.xml','DCM2017.xml','DCM2016.xml','DCM2015.xml','DCM2014.xml','DCM2013.xml','DCM2012.xml','DCM2011.xml','DCM2010.xml','DCM2009.xml','DCM2008.xml','DCM2007.xml','DCM2006.xml','DCM2005.xml','DCM2004.xml','DCM2003.xml','DCM2002.xml'}

    chars_to_replace = {'Ã³': 'ó', 'Ã¡': 'á', 'Ã±': 'ñ', 'Ãº': 'ú', 'Ã©': 'é'}

    for project in project_list:
        file = path / project
        parser = et.XMLParser(strip_cdata=False)
        doc = et.parse(str(file), parser=parser)

        replace_chars(doc, chars_to_replace)

        doc.write(str(file), pretty_print=True)


if __name__ == '__main__':
    main()
