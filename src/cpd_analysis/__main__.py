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


# CPD-seq data analysis
# CPD-seq sequencing reads were trimmed of barcode sequences and the 3′ nucleotide of the sequencing read, 
# and then aligned to the hg19 human genome using the bowtie 2 software44. The resulting alignment files were 
# processed with SAMtools45 and BEDtools46, and custom Perl scripts were used to identify dinucleotide sequence 
# immediately upstream of the 5′ end of each sequencing read. The dinucleotide sequence on the opposite strand 
# was extracted as a putative CPD lesion. Background reads associated with non-dipyrimidine sequences, which were 
# likely due to incomplete 3′ DNA end blocking or non-specific DNA cleavage by T4 endonuclease V/APE1, were excluded 
# from subsequent analyses. Both positions in the dipyrimidine nucleotide were counted as lesion sites. Three independent 
# CPD-seq experiments mapped CPD lesions in UV-irradiated NHF1 cells (UV cells) and two independent CPD-seq experiments 
# mapped lesions in isolated NHF1 genomic DNA that was UV-irradiated in vitro (UV naked DNA). These biological replicates 
# were combined for most of the analyses. Additionally, in some cases only mutagenic CPD (mCPDs), which are CPD reads 
# associated with TC, CT, or CC dinucleotides, were analyzed.

def main():
  parser = argparse.ArgumentParser(description="CPDseq analysis",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  
  DEBUG = False
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
    #args.input="E:/projects/20191104_cpd_analysis/top1000.txt"
    #args.output="E:/projects/20191104_cpd_analysis/top1000"
    args.input="/scratch/cqs/shengq2/guoyan/20191104_cpd_analysis/R_2016_10_20_11_19_27_user_Proton1-224-Peng_Mao.fastq.txt"
    args.output="/scratch/cqs/shengq2/guoyan/20191104_cpd_analysis/cpdtest"
    args.barcodeFile="/scratch/cqs/shengq2/guoyan/20191104_cpd_analysis/fileList1.txt"
  
  logger = initialize_logger(args.output + ".log", args)
  demultiplex(args.input, args.output, args.barcodeFile, args, logger)
  
if __name__ == "__main__":
    main()
