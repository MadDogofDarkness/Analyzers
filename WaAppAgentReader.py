
def help():
    s = """
    -----------------------------------------------------usage---------------------------------------------------------
    reader.py filename .. filename_N                reads files through end, outputs files failed to read
    -f                                              reads fast instead of slowly
    -F W H I G                                      set alert level: -F shows FATAL alerts
                                                                     -W shows WARN alerts
                                                                     -H shows HEART alerts
                                                                     -I shows INFO alerts
                                                                     -G shows FATAL, WARN, and INFO alerts (V 1.0 only)
                                                                    omitting this tag will show all alerts
                                                note as of this release (V1.0) you can use them as seperate flags
                                                eg (-F -I -W) but not together eg (-FWHI)
                                                shows all alerts equal to or greater than the selected alert in priority
                                                with -F (FATAL) being priority 0, and -I (INFO) being priority 3
    -c                                              outputs the line count
    -t                                              outputs which ALERTS to include
    """
    print(s)

def declutter(line):
    s = ""
    for c in line:
        if c != "\r" or c != "\n" or c != "਍ഀ" or c != "":
            s += c
    return s

def getUsefulData(words, alerts):
    vert = alerts
    if len(alerts) == 1:
        vert = ["WARN", "FATAL", "INFO", "HEART"]
    count = 0
    alert = ""
    for c in words:
        if c == '[' or c == ']':
            count += 1
        elif count == 5:
            alert += c
        elif count > 5:
            for a in vert:
                if a == alert:
                    #print(f"alert: {alert}") # debug
                    return declutter(words)

if __name__ == '__main__':
    print("Version 1.0")
    import sys
    import time
    import random
    h = ["-h", "--h", "man", "help", "?", "/?"]
    alerts = [""]
    count = 0
    c = False
    fast = False
    print(len(sys.argv))
    if len(sys.argv) >= 2: 
        for arg in sys.argv:
            if arg in h:
                help()
                exit()
            elif arg == '-c':
                c = True
            elif arg == '-f':
                fast = True
            elif arg == "-F":
                alerts.append("FATAL")
            elif arg == "-W":
                alerts.append("FATAL")
                alerts.append("WARN")
            elif arg == "-H":
                alerts.append("FATAL")
                alerts.append("HEART")
                alerts.append("WARN")
            elif arg == "-I":
                alerts.append("FATAL")
                alerts.append("HEART")
                alerts.append("INFO")
                alerts.append("WARN")
            elif arg == "-G":
                alerts.append("FATAL")
                alerts.append("WARN")
                alerts.append("INFO")
            elif arg == "-E":
                alerts.append("ERROR")
            elif arg == "-t":
                print(alerts) # debug
            else:
                pass
        for i in range(1, len(sys.argv)):
            try:
                f = open(sys.argv[i], 'r')
                for line in f:
                    data = getUsefulData(line, alerts)
                    if data == None:
                        pass
                    elif c == True:
                        print(data, count, end='\r')
                    else:
                        print(data, end='\r')
                    count = count + 1
                    if fast == False:
                        time.sleep(3 + random.randint(-2, 12))
                f.close()
            except FileNotFoundError or FileExistsError:
                if sys.argv[i] != "-f" and sys.argv[i] != "-c" and sys.argv[i] != "-G" and sys.argv[i] != "-t" and sys.argv[i] != "-H" and sys.argv[i] != "-I" and sys.argv[i] != "-W":
                    print(f"could not find file {sys.argv[i]} line count {count}")
