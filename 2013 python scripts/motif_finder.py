      filename = raw_input('Enter file name:')
   if len(filename) > 0:
       try:
           dnafile = open(filename, 'r')
           fileinput = False
       except:
           print 'File does not exist, please try again'
   else:
       fileinput = False
       sys.exit()</syntax>
       
   inmotif = raw_input('Enter motif to search: ')
   if len(inmotif) >= 1:
       motif = re.compile('%s' % inmotif)
       if re.search(motif, sequence):
           print 'Yep, I found it'
       else:
           print 'Sorry, try another one'
   else:
       print 'Done, thanks for using motif_search'
       inputfromuser = False</syntax>
