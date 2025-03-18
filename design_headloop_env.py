#! /usr/bin/env python

''' Script to design headloop primers for a CRISPR guideRNA target

Uses the Headloop package (https://github.com/GTPowell21/Headloop) '''

import argparse
import sys
import os
from headloop.designer import design

lp = os.environ.get('left_primer')
rp = os.environ.get('right_primer')
context = os.environ.get('context')
orientation = os.environ.get('orientation')
id = os.environ.get('id')
print(id, lp, rp, context, orientation)

hl_design = design(lp, rp, context, orientation)
for d in hl_design:
    id = id + d.id.replace(" ", "-")
    # output name, primer1, primer2, headloop-primer and description
    print("\t".join([id, lp, rp, str(d.seq), d.description]))
