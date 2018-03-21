import os,csv,time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    def set_color(self, color):
        if(color == "g"):
            print(self.OKGREEN)
        elif(color == "b"):
            print(self.OKBLUE)

    def end_color(self):
        print(self.ENDDC)

while True:
    count = 0
    path = 'goeranh'
    print('\n\n\n\n')
    print(bcolors.OKGREEN + 'enter the name(or fragments of it) of the file[leave blank to search all]' + bcolors.ENDC)
    fname = str(raw_input('->'))
    print('enter a search string')
    string = str(raw_input('->'))
    time1 = time.time()
    for path, dirs, files in os.walk('/home/%s/.sqlmap/output' % path):
        for f in files:
            if f.endswith('.csv'):
                tempcount = count
                print('')
                print('\033[93m' + f + '\033[0m')
                if(f.lower().find(fname.lower()) != -1):
                    #print os.path.join(path, f)
                    t = os.path.join(path, f)
                    with open(t) as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        for row in readCSV:
                            for item in row:
                                if(item.lower().find(string.lower()) != -1):
                                    count = count + 1
                                    print('   \033[93m' + t + '\033[0m')
                                    print('')
                                    print(bcolors.HEADER + '     #! ' + item + ' !#' + bcolors.ENDC)
                                    print('')
                                    for j in row:
                                        if(j.lower().find(string.lower()) != -1):
                                            print('\033[91m' + j + '\033[0m -- '),
                                        else:
                                            print(j + ' -- '),
                                    print('')
                                    print('')
                                    print('')
                                    print('')
                if(tempcount == count):
                    print('nothing found in this file')
                    print('')

    print('\033[96m')
    if(count == 0):
        print('')
        print('could not find your search string')
        print('')
    else:
        print('')
        print('')
        print(str(count) + ' results in'),
    time2 = time.time()
    time3 = time2 - time1
    print("Your search took " + str(time3) + " seconds")
    print('\033[0m')
