htseq-count -f bam -r pos /share/home/cau_pengjy/document/yeast_project/analysis/read_align/EV_strain_3.sort.bam /share/home/cau_pengjy/document/yeast_project/data/reference/Saccharomyces_cerevisiae.R64-1-1.54.gtf > EV_strain_3.count.tab
#计数: htseq-count -f bam -r pos xx.sort.bam 参考基因组注释文件.gtf > 结果文件.count.tab
#-f bam 指定待处理文件的格式为bam；-r pos 指定基因的排序模式为基因的位置（也可以是基因的name）
