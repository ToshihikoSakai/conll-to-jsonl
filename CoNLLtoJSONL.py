#coding: UTF-8
import os
import re
import glob
import pathlib
import pprint

filename = "/Users/tsakai/Downloads/20210411.conll"
#filename = "~/Downloads/100-conll.txt"

fid = 0
text = []

labels = ""

with open('{}'.format(filename),mode='r') as f:
    position = 0
    tagstart = 0
    end = 0
    tagend = 0
    flag = 0
    
    for s_line in f:

        if(s_line == "\n"):
            position = 0
            tagstart = 0
            end = 0
            tagend = 0
            flag = 0

            printsen = ""
            
            printsen += "{\"id\":%s," % fid
            #最後の空白を除く処理もre.sub()で記載している
            printsen += "\"text\":\"%s\"," % re.sub(' $',''," ".join(text))
            printsen += "\"meta\":{},\"annotation_approver\":null,\"comment_count\":0," 
            printsen += "\"labels\":[%s]}" % re.sub(',$','',labels)
            
            print(printsen)
            #print("\{\"id\":{},\"text\":\"\",\"meta\":\{\},\"annotation_approver\":null,\"comment_count\":0,\"labels\":\[{}\]}".format(fid,text,re.sub(',$','',labels)))
            #print(re.sub(',$','',labels))
            
            text = []
            labels = ""
            fid = fid + 1
            continue
                
        line_sp = s_line.split()
        
        if(flag == 1):

            if(not("I-" in line_sp[1])):
                if(len(line_sp[0]) == 1):
                    tagend = position-1
                else:
                    tagend = position
                    
                labels += "[{},{},\"{}\"],".format(tagstart,tagend,line_sp_sp[1])
                flag = 0
                
        if((flag == 0) and (line_sp[1] != "O")):
            tagstart = position

            flag = 1
            
            #line_sp_sp[0] =  B
            #line_sp_sp[1] =  atom
            line_sp_sp = line_sp[1].split("-")
            
        #print("{} position={}".format(line_sp[0],position))
        position += len(line_sp[0])+1

        text.append(line_sp[0])
                

    
