#! /usr/bin/env python

''' Script to design headloop primers for a CRISPR guideRNA target

Uses the Headloop package (https://github.com/GTPowell21/Headloop) '''

import argparse
import sys
from headloop.designer import design

def main(args):
    ''' Main body of code '''

    # read in input
    for line in args.input_file:
        info = line.rstrip('\n').split("\t")
        # design primers
        hl_design = design(*info[1:5])
        # print each design
        for d in hl_design:
            id = d.id.replace(" ", "-")
            # output name, primer1, primer2, headloop-primer and description
            output = info[0:3] + [ str(d.seq), d.description ]
            # join which primer contains the headloop tag to the name
            output[0] = output[0] + "-" + id
            print("\t".join(output), file = args.output_file)

if __name__ == '__main__':
    descr = 'Design headloop PCR primers'

    detail = '''The scripts expects input with 5 tab-separated columns:
name            A name for the primer set
sense_oligo     string containing the forward primer
antisense_oligo string containing the reverse primer
guide_context   string containing guide sequence and >= 15 bp forward context
orientation     is the guide in the same strand as the 'sense' primer or 'antisense' primer?

The input can be on STDIN or a file name.'''
    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = descr, epilog = detail)
    parser.add_argument('input_file', nargs='?', metavar='FILE',
        type=argparse.FileType('r'), default=sys.stdin, 
        help='Input file name. Defaults to STDIN')
    parser.add_argument('--output_file', metavar='FILE',
        type=argparse.FileType('w'), default=sys.stdout, 
        help='Name of file for output, Defaults to STDOUT')
    params = parser.parse_args()
    main(params)
