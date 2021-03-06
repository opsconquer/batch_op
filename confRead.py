# -*- coding:utf-8 -*-  #desc: use to read ini  # #
#实现一个配置文件读取模块，支持两种方式，一种是类的形式，一种是函数形式 #---------------------

import sys,os,time  
import ConfigParser  

#类的形式
class Config:  
    def __init__(self, path):  
        self.path = path  
        self.cf = ConfigParser.ConfigParser()  
        self.cf.read(self.path)  
    def get(self, field, key):  
        result = ""  
        try:  
            result = self.cf.get(field, key)  
        except:  
            print "cannot find the value for: [%s:%s]" % (field,key)
            result = ""
        return result  
        
    def set(self, filed, key, value):  
        try:  
            self.cf.set(field, key, value)  
            cf.write(open(self.path,'w'))  
        except:
            print "write configure failed!"
            return False  
        return True  
              
              
 
#函数形式
def read_config(config_file_path, field, key):   
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        result = cf.get(field, key)  
    except:
        print "cannot find the value for: [%s:%s]" % (field,key)    
        sys.exit(1)  
    return result  
 
#读取该Section下的所有键值对
def read_configBySection(config_file_path, field):   
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        result = cf.items(field)  
    except:
        print "cannot find the section for: [%s]" % (field) 
        sys.exit(1)  
    return result

    
def write_config(config_file_path, field, key, value):  
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        cf.set(field, key, value)  
        cf.write(open(config_file_path,'w'))  
    except:  
        sys.exit(1)  
    return True  

if __name__ == "__main__":  
    config_file_path = 'config.ini'

    #从配置文件中读取路径参数
    hosts = read_configBySection(config_file_path, 'HOST')
    print hosts


