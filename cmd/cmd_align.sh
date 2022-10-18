hisat2 -x /share/home/cau_pengjy/document/yeast_project/data/reference/yeast_ref -U /share/home/cau_pengjy/document/yeast_project/data/RNA_seq//SRR1916152.fastq | samtools view -bS - | samtools sort - -o EV_3.sort.bam
samtools index EV_3.sort.bam
hisat2 -x /share/home/cau_pengjy/document/yeast_project/data/reference/yeast_ref -U /share/home/cau_pengjy/document/yeast_project/data/RNA_seq//SRR1916153.fastq | samtools view -bS - | samtools sort - -o EV_4.sort.bam
samtools index EV_4.sort.bam
hisat2 -x /share/home/cau_pengjy/document/yeast_project/data/reference/yeast_ref -U /share/home/cau_pengjy/document/yeast_project/data/RNA_seq//SRR1916154.fastq | samtools view -bS - | samtools sort - -o DNMT3B_2.sort.bam
samtools index DNMT3B_2.sort.bam
hisat2 -x /share/home/cau_pengjy/document/yeast_project/data/reference/yeast_ref -U /share/home/cau_pengjy/document/yeast_project/data/RNA_seq//SRR1916155.fastq | samtools view -bS - | samtools sort - -o DNMT3B_3.sort.bam
samtools index DNMT3B_3.sort.bam
hisat2 -x /share/home/cau_pengjy/document/yeast_project/data/reference/yeast_ref -U /share/home/cau_pengjy/document/yeast_project/data/RNA_seq//SRR1916156.fastq | samtools view -bS - | samtools sort - -o DNMT3B_4.sort.bam
samtools index DNMT3B_4.sort.bam
