""" SpeedCheck
"""
from inspect import (
   getfile,
   currentframe
)
from os.path import (
   abspath,
   dirname,
   join
)
import sys
from sys import path as syspath

try:
   from SpeedIT.MainCode import speed_it
except ImportError as err:
   sys.exit('''
      Example SpeedTest: Can not run example. This example needs the package <SpeedIT >= 4.2.2> to be installed: <{}>
      '''.format(err)
   )

SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PROJECT_ROOT = dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'TEMPLATE_PyPROJECT'
ROOT_PACKAGE_PATH = join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

syspath.insert(0, PROJECT_ROOT)


def dummy():
   pass


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   #  value format: tuple (function, list_of_positional_arguments, dictionary_of_keyword_arguments)
   func_dict = {
      'dummy': (dummy, [], {}),
   }

   setup_line_list = [
   ]

   result = speed_it(
      func_dict,
      setup_line_list,
      enable_benchmarkit=True,
      enable_profileit=True,
      enable_linememoryprofileit=True,
      enable_disassembleit=True,
      use_func_name=True,
      output_in_sec=False,
      profileit__max_slashes_fileinfo=2,
      profileit__repeat=1,
      benchmarkit__with_gc=False,
      benchmarkit__check_too_fast=True,
      benchmarkit__rank_by='best',
      benchmarkit__run_sec=1,
      benchmarkit__repeat=3
   )

   with open('result_output/SpeedCheck.txt', 'w') as file_:
      file_.write('\n\n SpeedCheck.py output\n\n')
      file_.write(result)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
