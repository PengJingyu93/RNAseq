# wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR1916152/SRR1916152

import sys   #导入pythn的sys模块
#print(sys.argv[1])   #打印python的sys.argv(system argument value:系统参数值)的第2个参数,即打python后跟的第2个文件 #python的使用:python 脚本文件[0] 对象文件[1] #其中脚本文件[0]为sys.argv的第1个参数,对象文件[1]为sys.argv的第2个参数
acc_file = sys.argv[1]      #把sys.argv中的第2个变量(SRR_Acc_List.txt)赋值给acc_file
with open(acc_file) as acc_file_handle:    #打开acc_file以acc_file_handle(管道句柄)的形式
      for line in acc_file_handle:     #按行读取acc_file_handle中的内容  
          line = line.rstrip()    #如果RR_Acc_List.txt文件中有换行符,通过该行代码去掉该文件中的换行符. 因为在执行print (line)的时候会自动在字符串之间加上一个换行符. 不删,会造成字符串之间换行两次.
          #print (line)
          cmd_str = "wget https://sra-pub-run-odp.s3.amazonaws.com/sra/{srr_acc}/{srr_acc}".format(srr_acc = line)
          print(cmd_str)
