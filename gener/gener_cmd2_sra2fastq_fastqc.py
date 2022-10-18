import sys   #导入pythn的sys模块
acc_file = sys.argv[1]      #把sys.argv中的第2个变量(即对象文件:SRR_Acc_List.txt)赋值给acc_file
with open(acc_file) as acc_file_handle:    #打开acc_file以acc_file_handle(管道句柄)的形式
      for line in acc_file_handle:     #按行读取acc_file_handle中的内容  
          line = line.rstrip()    #去掉对象文件中的换行符. 避免造成字符串之间换行两次.
          cmd_str = "fastq-dump {sra_file}\nfastqc {fq_file}".format(sra_file = line, fq_file = line + ".fastq")   #若为双端测序,必须改为 fastq-dump --split-files; /n:表示换行,这样的话,该脚本可完成 fastq-dump 和 fastqc 两个指令
          print(cmd_str)
