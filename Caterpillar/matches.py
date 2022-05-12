import re
import sys

def main():
    
    # Matches <some variation of a port tag> 
    # <a number between 1 - 65535>
    # <Optional closing double-quote>
    pattern = \
        "((port:\"|service:\"|port\\s|Port:\\s)"\
        "((65[0-5][0-3][0-5])|(6[0-4][0-9]{{3}})|([0-5][0-9]{{4}})|([0-9]{{2,4}})|([1-9]{{1}}))"\
        "(?:\")?)"
    
    # Opens log file. I tested this against a simple .txt file, but it should work with other
    # files. Expects the log file to be passed in at the command line as the second 
    # argument, after the script location\name.
    with open(sys.argv[1]) as logs:
        ports = re.findall(pattern.format(),logs.read())

    # Print each port from matches.
    for port in ports:
        print("Port:", port[2])        

if __name__ == "__main__":
    main()