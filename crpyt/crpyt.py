#!/usr/bin/env python

'''
crpyt is a module to encrypt and decrypt media data, such as images and
video, while preserving the media type.
'''

from __future__ import print_function # Ensure that pylint accepts parenthesis around 'print'
import argparse
from argparse import ArgumentParser



VERSION = '0.0.1'

SUFFIX = 'crpyt'

class CRPYTArgumentParser(ArgumentParser):
    '''
    CRPYTArgumentParser parses the arguments for crpyt.
    '''

    def __init__(self):
        '''
        The __init__ method defines the parameters for crpyt.
        '''
        super(CRPYTArgumentParser, self).__init__(description='crpyt can be used to' + \
            'encrypt/decrypt media files without changing the media type.', \
            formatter_class=argparse.RawDescriptionHelpFormatter)
        # Add all arguments:
        self.add_argument('-d', '--decrypt', action='store_true', \
            help='decrypt the provided input.')
        self.add_argument('-D', '--directory', help='store the output in the provided directory.')
        self.add_argument('-i', '--ignore-errors', action='store_true', \
            help='proceed in case of an error.')
        self.add_argument('-k', '--key', help='use the key in the provided key file.')
        self.add_argument('-r', '--recursive', action='store_true', \
            help='process folders recursively.')
        self.add_argument('-s', '--suffix', \
            help='use the provided suffix for the output files/folders.')
        self.add_argument('-v', '--verbose', action='store_true', \
            help='display detailed information about the process.')
        self.add_argument('-V', '--version', action='version', version='crpyt '+VERSION+ \
        '\nCopyright (C) 2018\n', help='display information about the installed version.')
        self.add_argument('sources', nargs='*', \
            help='The source file(s) or folder(s) to be encrypted/decrypted.')

class CRPYTExecutor(object):
    '''
    CRPYTExecutor handles the execution of crpyt.
    The main method is execute(self,args), where the parameters are provided in args.
    '''

    def execute(self):
        '''
        The main method parses the arguments and then
        executes the command at the provided destination(s).
        '''
        # The argument parser is instantiated:
        parser = CRPYTArgumentParser()
        # The arguments are parsed and returned:
        args = parser.parse_args()
        if args.verbose:
            print('Verbose is activated...')
        print('Terminate.')

if __name__ == '__main__':
    CRPYT_EXECUTOR = CRPYTExecutor()
    CRPYT_EXECUTOR.execute()
