#coding: UTF-8
import os
import re
import glob
import pathlib
import pprint
import sys


fid = 0
text = []

labels = ""

with open(sys.argv[1],mode='r') as f:
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
            printsen += "\"text\":\"%s\"," % re.sub(' $','',"".join(text))
            printsen += "\"meta\":{},\"annotation_approver\":null,\"comment_count\":0," 
            printsen += "\"labels\":[%s]}" % re.sub(',$','',labels)
            
            print(printsen)
            #print("\{\"id\":{},\"text\":\"\",\"meta\":\{\},\"annotation_approver\":null,\"comment_count\":0,\"labels\":\[{}\]}".format(fid,text,re.sub(',$','',labels)))
            #print(re.sub(',$','',labels))
            
            text = []
            labels = ""
            fid = fid + 1
            continue
                
        w, BIOtag = s_line.split()
        
        # flag : determine B or I
        # flag = 0 : Begin of tag
        # flag = 1 : I of tag
        if(flag == 1):

            if(not("I-" in BIOtag)):
                tagend = position
                    
                labels += "[{},{},\"{}\"],".format(tagstart,tagend,tag)
                flag = 0

        # If the tag is B
        if((flag == 0) and (BIOtag != "O")):
            tagstart = position

            flag = 1
            
            # B_or_I : B
            # tag : atom
            B_or_I, tag = BIOtag.split("-")
            
        # print("{} position={}".format(w,position))

        position += len(w)

        text.append(w)
                    
