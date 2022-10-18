import sys   #导入pythn的sys模块
acc_file = sys.argv[1]      #把sys.argv中的第2个变量(SRR_Acc_List_sample.txt)赋值给acc_file
ref_file = sys.argv[2]      #用于指定参考基因组索引文件(xx_ref)
fq_file = sys.argv[3]       #用于指定xx.fastq文件
with open(acc_file) as acc_file_handle:    #打开acc_file以acc_file_handle(管道句柄)的形式
      for line in acc_file_handle:     #按行读取acc_file_handle中的内容  
          line = line.rstrip()    #去掉对象文件中的换行符. 避免造成字符串之间换行两次.
          ele = line.split("\t")    #\t表示 tab键
          #print(ele)
          cmd_str = "hisat2 -x {ref_dir} -U {fq_dir}/{srr_acc}.fastq | samtools view -bS - | samtools sort - -o {sample_real_name}.sort.bam\nsamtools index {sample_real_name}.sort.bam".format(ref_dir = ref_file, fq_dir = fq_file, srr_acc = ele[0], sample_real_name = ele[1])  
#/n:表示换行. 该脚本可完成:1生成xx.sort.bam文件;2并对该文件建立索引. 即"转录组数据分析/数据分析/二/2-5"
#若为双端测序,必须改为 fastq-dump --split-files;
          print(cmd_str)
