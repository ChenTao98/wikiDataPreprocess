import os,time,sys,getopt

def preprocess(path,out_file_a):
    file_list=os.listdir(path)
    file_list.sort()
    print(file_list)
    with open(out_file_a,"w",encoding='utf-8') as out_file:
        for filename in file_list:
            with open(os.path.join(path,filename),"r",encoding='utf-8') as input_file:
                temp_str=""
                flag=False
                for line in input_file:
                    if(line.find("<doc")==0):
                        temp_str=""
                        flag=True
                    elif(line.find("</doc")==0):
                        out_file.write(temp_str+"\n")
                    elif(flag):
                        flag=False
                    else:
                        temp_str+=line.strip()
            print("done one")

if __name__ == "__main__":
    opt,args=getopt.getopt(sys.argv[1:],"p:o:")
    path=None
    out_file=None
    for o,a in opt:
        if(o=="-p"):path=a
        if(o=="-o"):out_file=a
    if(path==None or out_file==None):
        print("usage:python extra.py -p <path> -o <out_file>")
        sys.exit()
    if((not os.path.exists(path)) or (not os.path.isdir(path)) or (len(os.listdir(path))==0)):
        print("path must be the dir containing extracted file ")
        sys.exit()
    if(os.path.exists(out_file)):
        print("out file:{} is existed".format(out_file))
        sys.exit()
    start=time.time()
    preprocess(path,out_file)
    end=time.time()
    print("total time: %0.2fs" %(end-start))