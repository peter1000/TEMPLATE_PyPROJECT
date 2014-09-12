#!/usr/bin/env python3
"""
========================================
RenameTEMPLATE_PyPROJECT - helper module
========================================

Overview
========
This module helps to start a new Python project using: TEMPLATE_PyPROJECT

#. Replaces all occurrences of ``TEMPLATE_PyPROJECT`` with ``NEW_PROJECT_NAME``
#. Replaces all occurrences of ``template_pyproject`` with ``NEW_PROJECT_NAME lower case``
#. Replaces all occurrences of ``TEMPLATE__OneLine_PyPROJECT_Description`` with ``NEW_PROJECT_ONE_LINE_DESCRIPTION``
#. Renames all File which contain in their name: ``TEMPLATE_PyPROJECT`` with ``NEW_PROJECT_NAME``
#. Renames all Folder/SubFolder with name: ``TEMPLATE_PyPROJECT`` with ``NEW_PROJECT_NAME``

Must be removed from the project
"""
from os import (
   rename as os_rename,
   walk as os_walk,
)
from os.path import (
   basename as path_basename,
   dirname,
   isdir,
   join as path_join,
)


# ===========================================================================================================================
# CONFIGURE - HERE
# ===========================================================================================================================

# Path to the ``TEMPLATE_PyPROJECT`` which should be renamed
TEMPLATE_PyPROJECT_DIR_PATH = '/home/PycharmProjects/TEMPLATE_PyPROJECT'

# New Project Name
NEW_PROJECT_NAME = 'XXX'

# New Project One Line Description: may not contain double quotes ``"``
NEW_PROJECT_ONE_LINE_DESCRIPTION = "XXX Description"

# Any file to be skipped reading and replacing names: just the name: example: binary files like images
SkipFileNames = [
   'P-Projects32_32.ico',
]

# ===========================================================================================================================
# END CONFIGURE
# ===========================================================================================================================


# check no " double quote in: NEW_PROJECT_ONE_LINE_DESCRIPTION
if '"' in NEW_PROJECT_ONE_LINE_DESCRIPTION:
   print('''


   ATTENTION::::::The Specified NEW_PROJECT_ONE_LINE_DESCRIPTION may not contain double quotes <">

      We got: NEW_PROJECT_ONE_LINE_DESCRIPTION:
          <{}>

   '''.format(NEW_PROJECT_ONE_LINE_DESCRIPTION))
   raise Exception



NewProjectName__lower_case = NEW_PROJECT_NAME.lower()
OrigTemplateName__lower_case = 'template_pyproject'

OrigTemplateName = 'TEMPLATE_PyPROJECT'

OrigTemplateOneLineDescription = 'TEMPLATE__OneLine_PyPROJECT_Description'

# check that the TEMPLATE_PyPROJECT_DIR_PATH dir exist
if not isdir(TEMPLATE_PyPROJECT_DIR_PATH):
   # noinspection PyPep8
   raise Exception('\n\n\nATTENTION::::::The Specified TEMPLATE_PyPROJECT_DIR_PATH Dir does not exist:\n<{}>\n\n'.format(TEMPLATE_PyPROJECT_DIR_PATH))


DirList = []
FileList = []
for root, dirs, files in os_walk(TEMPLATE_PyPROJECT_DIR_PATH, topdown=False):
   for dir_ in dirs:
      DirList.append((root, dir_))
   for file_ in files:
      FileList.append((root, file_))


# FIRST: replace text in Files
for root, file_ in FileList:
   file_path = path_join(root, file_)
   # check SkipFileNames
   if path_basename(file_path) in SkipFileNames:
      continue
   with open(file_path, 'r') as file_p:
      file_content = file_p.read()

   if OrigTemplateName in file_content:
      file_content = file_content.replace(OrigTemplateName, NEW_PROJECT_NAME)

   if OrigTemplateName__lower_case in file_content:
      file_content = file_content.replace(OrigTemplateName__lower_case, NewProjectName__lower_case)

   if OrigTemplateOneLineDescription in file_content:
      file_content = file_content.replace(OrigTemplateOneLineDescription, NEW_PROJECT_ONE_LINE_DESCRIPTION)

   with open(file_path, 'w') as file_p:
      file_p.write(file_content)


# SECOND: replace File Names
for root, file_name in FileList:
   if OrigTemplateName in file_name:
      new_file_name = file_name.replace(OrigTemplateName, NEW_PROJECT_NAME)
      os_rename(path_join(root, file_name), path_join(root, new_file_name))


# THIRD: replace Dir Names
for root, dir_ in DirList:
   if dir_ == OrigTemplateName:
      os_rename(path_join(root, dir_), path_join(root, NEW_PROJECT_NAME))


# FINALLY: rename the Root folder
NewPathName = '{}/{}'.format(dirname(TEMPLATE_PyPROJECT_DIR_PATH), NEW_PROJECT_NAME)
os_rename(TEMPLATE_PyPROJECT_DIR_PATH, NewPathName)

print('\nFINISHED....\n')
