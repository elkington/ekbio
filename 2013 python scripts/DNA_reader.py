filename = raw_input('Please enter a file to check: ')
if len(filename) >= 1:
    try:
        seqlist = open(filename, 'r').readlines()
    	sequence = .join(seqlist)
    	sequence = sequence.replace('\n', )
        totalA = sequence.count('A')
        totalC = sequence.count('C')
        totalG = sequence.count('G')
        totalT = sequence.count('T')
        otherletter = re.compile('[BDEFHIJKLMNOPQRSUVXZ]')
    extra = re.findall(otherletter, sequence)
    output = open(filename+'.count', 'w')
    output.write('Count report for file ' + filename + '\n')
    output.write('A = ' + str(totalA) + '\n')
    output.write('C = ' + str(totalC) + '\n')
    output.write('G = ' + str(totalG) + '\n')
    output.write('T = ' + str(totalT) + '\n')
    if len(extra) > 0:
        output.write('Also were found ' + str(len(extra)) + ' errors\n')
        for i in extra:
        output.write(i + ' ')
    else:
    output.write('No error found')
        output.close()
    print 'Result file saved on ' + filename + '.count'
    except:
        print 'File not found. Please try again.'
else:
    fileentered = False
    sys.exit()