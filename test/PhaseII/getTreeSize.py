#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ROOT
import argparse
import matplotlib.pyplot as plt
import numpy as np

def GetHumanReadable(size,precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1
        size = size/1024.0
    return "%.*f%s"%(precision,size,suffixes[suffixIndex])

def printTreeSize(filename, treename, savefig, zipsize):
    t = ROOT.TChain(treename)
    t.AddFile(filename)
    branchSizes = []
    for b in t.GetListOfBranches():
        if not zipsize:
            branchSizes.append( (b.GetName(), b.GetTotalSize()) )
        else:
            branchSizes.append( (b.GetName(), b.GetZipBytes()) )
    branchSizes = sorted(branchSizes, key=lambda x: x[1], reverse=True)
    maxWidthEntry = max(branchSizes, key=lambda x: len(x[0])+len(str(x[1]))+1)
    width = len(maxWidthEntry[0]) + len(str(maxWidthEntry[1]))

    totalSize = sum([b for a,b in branchSizes])
    fractions = [float(b)/float(totalSize)*100. for a,b in branchSizes]
    i=0
    for a,b in branchSizes:
		print a, " "*(width-len(a)-len(str(GetHumanReadable(b)))), GetHumanReadable(b), np.round(fractions[i],1),"%"
		i=i+1
    print "-"*(width+len(str(GetHumanReadable(totalSize))))
    print "Total", " "*(width-len("Total")-len(str(GetHumanReadable(totalSize)))),GetHumanReadable(totalSize)

    if savefig:
        labels = [a for a,b in branchSizes]
        sizes = [b for a,b in branchSizes]
        fig = plt.figure()
        ax = fig.gca()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, radius=1)
        plt.savefig("treeSize.pdf")
        print ""
        print "Saved to: treeSize.pdf"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--tree", default="writeNTuple/NTuple")
    parser.add_argument("--savefig", default=False, action='store_true')
    parser.add_argument("--zipsize", default=False, action='store_true')
    args = parser.parse_args()

    printTreeSize(args.file, args.tree, args.savefig, args.zipsize)
