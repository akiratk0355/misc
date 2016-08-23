#!py_env/bin/python
# python3

'''
Basic CLI template with argparse

Created on Aug 15, 2016
'''

import os, sys, argparse, logging, logging.handlers

def file_reader(fobj):
    lines = [x.rstrip('\n') for x in fobj]
    return lines

def logging_setup(args):
    log_root = logging.getLogger('')
    if args.verbose > 1:
        log_root.setLevel(logging.DEBUG)
    elif args.verbose == 1:
        log_root.setLevel(logging.INFO)
    
    log_format = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    log_handler = logging.StreamHandler()
    if args.logfile:
        log_handler = logging.handlers.WatchedFileHandler(args.logfile, encoding='utf-8')
    log_handler.setFormatter(log_format)
    log_root.addHandler(log_handler)

def main(argv):
    parser = argparse.ArgumentParser(description="Basic CLI tool template")
    parser.add_argument("-v", "--verbose", action="count", default=0, dest="verbose",
                        help="Enable verbose output (specify multiple times to increase level)")
    parser.add_argument("-d", "--debug", action="count", default=0, dest="debug",
                        help="Enable debugging mode")
    parser.add_argument("-l", "--logfile", action="store", metavar="FILE", dest="logfile",
                        help="Log file name")
    parser.add_argument("-f", "--srcfile", action="store", metavar="FILE", dest="srcfile",
                        help="Source file path")
    parser.add_argument("-o", "--outfile", action="store", metavar="FILE", dest="outfile",
                        help="Output file path")
    parser.add_argument("-s", "--srcstr", action="append", metavar="STRING", dest="srcstr",
                        help="Source strings")
    parser.add_argument("-m", "--mode", action="store", type=int, metavar="MODENUM", default=0, dest="mode", 
                        help="Mode number")
    args = parser.parse_args(argv)
 
    # Logging setup
    logging_setup(args)
    log_main = logging.getLogger('main')
    
    log_main.info("running in mode %d", args.mode)
    
    if args.srcfile:
        log_main.debug("received file %s", args.srcfile)
        with open(os.path.abspath(args.srcfile), 'r') as f:
            textlines = file_reader(f)
            # do_something(textlines)
    
    if args.srcstr:
        log_main.debug("received strings: %s",  args.srcstr)
        # do_something(args.srcstr)
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
