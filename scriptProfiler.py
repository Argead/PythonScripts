#!/usr/bin/python3
"""
Command Line utility for profiling a Python script.
"""
import argparse
import os
import subprocess
import trace #TODO: is trace import needed? All trace calls are in subprocess command line call. Run with and without this import, and if it still works, which it should, delete this line.
 
 
parser = argparse.ArgumentParser(description='Profile a Python script.')
parser.add_argument('target', type=str, help='Python script to profile')
parser.add_argument('-o', '--output', type=str, help='Name of file containing target script profiling info.')
args = parser.parse_args()
 
 
def validate_python_file(target_file):
    return target_file.endswith('.py')
 
 
def profile_script():
    if validate_python_file(args.target):
        if args.output:
            results_file_name = args.output
        else:
            split_target = os.path.splitext(args.target)
            results_file_name = '{}_results.txt'.format(split_target[0])

        results_file = open(results_file_name, 'w')
        results_file.write(args.target)
        results_file.write('\n\nCOUNT\n')
        trace_call_one_command = 'python3 -m trace --count {}'.format(args.target)
        trace_call_one = subprocess.Popen(trace_call_one_command, shell=True, stdout = subprocess.PIPE)
        print(trace_call_one_command)
        print(trace_call_one)
        if type(trace_call_one) != int:
            results_file.write(trace_call_one.communicate()[0].decode())
     
        results_file.write('\n\nTRACE\n')
        trace_call_two_command = 'python3 -m trace --trace --timing {}'.format(args.target) #calling with the --timing modifier prefixes each line w. time since script started.
        trace_call_two = subprocess.Popen(trace_call_two_command, shell=True, stdout=subprocess.PIPE)
        if type(trace_call_two) != int:
            results_file.write(trace_call_two.communicate()[0].decode())
     
        results_file.write('\n\nLISTFUNCS')
        trace_call_three_command = 'python3 -m trace --listfuncs --missing {}'.format(args.target) #calling with the --missing modifier marks lines not executed with >>>>>>
        trace_call_three = subprocess.Popen(trace_call_three_command, shell=True, stdout=subprocess.PIPE)
        if type(trace_call_three) != int:
            results_file.write(trace_call_three.communicate()[0].decode())
         
        results_file.write('\n\nTRACKCALLS')
        trace_call_four_command = 'python3 -m trace --trackcalls {}'.format(args.target)
        trace_call_four = subprocess.Popen(trace_call_four_command, shell=True, stdout=subprocess.PIPE)
        if type(trace_call_four) != int:
            results_file.write(trace_call_four.communicate()[0].decode())
         
        results_file.write('\n\nEND OF PROFILE')
        results_file.close()
        print('Profiling completed for {}'.format(args.target))
    else:
        print('The target file must be a Python script.')
     
     
if __name__ == '__main__':
    profile_script()

