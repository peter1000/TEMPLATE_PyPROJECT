""" Speed-IT
"""
from os.path import abspath as path_abspath
from sys import exit as sys_exit

# Import speed_it
try:
   # noinspection PyPackageRequirements,PyUnresolvedReferences
   from PySpeedIT.speed_it import speed_it
except ImportError as err:
   sys_exit('''
      Example SpeedTest: Can not run speed_it. This module needs the package <PySpeedIT >= 1.0.6> to be installed: <{}>
      '''.format(err)
   )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   # defining the: modules_func_tuple mapping
   modules__func_tuples = (
      # TUPLE format:
      # [module_path_str, ((name_str, function_name_str, list_of_positional_arguments, dictionary_of_keyword_arguments))]

      [path_abspath('speed_check.py'), (
         ('example1', 'example1', [], {}),  # TODO
      )],
   )

   speed_it(
      html_output_dir_path=path_abspath('result_output'),
      enable_benchmarkit=True,
      enable_profileit=True,
      enable_linememoryprofileit=True,
      enable_disassembleit=True,
      modules__func_tuples=modules__func_tuples,
      output_max_slashes_fileinfo=2,
      use_func_name=True,
      output_in_sec=False,
      profileit__repeat=1,
      benchmarkit__output_source=True,
      benchmarkit__with_gc=False,
      benchmarkit__check_too_fast=True,
      benchmarkit__rank_by='best',
      benchmarkit__run_sec=1.0,
      benchmarkit__repeat=3
   )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
