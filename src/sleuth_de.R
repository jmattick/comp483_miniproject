args = commandArgs(trailingOnly = T) #get list of arguments

#load sleuth
library(sleuth)

#sample table
stab <- read.table(args[1], header=TRUE, stringsAsFactors=FALSE)

#initialize object
so <- sleuth_prep(stab)

#fit a model comparing two conditions
so <- sleuth_fit(so, ~condition, 'full')

#fit reduced model to compare the likelihood ratio test
so <- sleuth_fit(so, ~1, 'reduced')

#performed the likelihood ration test for differentail expression between conditions
so <- sleuth_lrt(so, 'reduced','full')

#load dplyr
library(dplyr)

#extract the test results from the sleuth object
sleuth_table <- sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE) 

#filter most significant results (FDR/qval < 0.05)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05) %>% dplyr::arrange(pval) 

#write top 10 transcripts to file
write.table(sleuth_significant, file=args[2],quote = FALSE,row.names = FALSE)

#extract columns for log file
logfile_data <- select(sleuth_significant, target_id, test_stat, pval, qval)

#output data to log
write.table(logfile_data, file="miniProject.log", quote = FALSE, row.names = FALSE,  append = TRUE)
