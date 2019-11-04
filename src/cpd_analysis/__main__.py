import argparse
import sys
import logging
import os
from DemultiplexUtils import demultiplex

def initialize_logger(logfile, args):
  logger = logging.getLogger('cpd_analysis')
  loglevel = logging.INFO
  logger.setLevel(loglevel)

  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')    
 
  # create console handler and set level to info
  handler = logging.StreamHandler()
  handler.setLevel(loglevel)
  handler.setFormatter(formatter)
  logger.addHandler(handler)
 
  # create error file handler and set level to error
  handler = logging.FileHandler(logfile, "w")
  handler.setLevel(loglevel)
  handler.setFormatter(formatter)
  logger.addHandler(handler)
 
  return(logger)

def runCommand(command, logger):
  logger.info("run : " + command )
  os.system(command)

def main():
  parser = argparse.ArgumentParser(description="CPDseq analysis",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  
  DEBUG = True
  NOT_DEBUG = not DEBUG
  
  parser.add_argument('-i', '--input', action='store', nargs='?', help="Input fastq gzipped file", required=NOT_DEBUG)
  parser.add_argument('-o', '--output', action='store', nargs='?', help="Output file prefix", required=NOT_DEBUG)
  parser.add_argument('-b', '--barcodeFile', action='store', nargs='?', help='Barcode definition file', required=NOT_DEBUG)
  
  if not DEBUG and len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

  args = parser.parse_args()
  
  if DEBUG:
    args.database=""
    args.input="E:/projects/20191104_cpd_analysis/top1000.txt"
    args.output="E:/projects/20191104_cpd_analysis/top1000"
    args.barcodeFile="E:/projects/20191104_cpd_analysis/fileList1.txt"
  
  logger = initialize_logger(args.output + ".log", args)
  demultiplex(args.input, args.output, args.barcodeFile, args, logger)
  
if __name__ == "__main__":
    main()
