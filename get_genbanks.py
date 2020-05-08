#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Thomas J. Creedy
"""
# Imports
import sys
import urllib.request
# Functions
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
# Main
acclist = sys.stdin.read().splitlines()
for chunk in chunker(acclist, 100):
    accstring = ','.join(chunk)
    url = ("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
          + "db=nuccore&id=" + accstring + "&rettype=gb")
    sys.stdout.write(urllib.request.urlopen(url).read().decode('utf-8'))
exit()