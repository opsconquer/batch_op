#-*- coding: utf-8 -*-

#!/usr/bin/python 

import paramiko
import os
import string

import confRead


import iniLog

infoLogger,errorLogger=iniLog.ini()

#登陆到远程主机执行命令
def sshCmd(ip,port,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,string.atoi(port),username,passwd,timeout=5)
        print '%s start processing'%(ip)
        infoLogger.info(ip+" start processing")
        for m in cmd:
            try:
                stdin, stdout, stderr = ssh.exec_command(m)
    #           stdin.write("Y")   #简单交互，输入 ‘Y’
                out = stdout.readlines()
                print "cmd :"+m
                #屏幕输出
                for o in out:
                    print o,
                    infoLogger.info(o)
            except:
                errorLogger.error(ip+" failed! "+ "stdin: "+stdin+"stdout: "+stdout+"stderr+ "+stderr)
        print '%s is processed over--------------------'%(ip)
        infoLogger.info(ip+" is processed over---------------")
        ssh.close()
    except:
        print '%s connect failed!-------------------- '%(ip)
        errorLogger.error(ip+" connect failed!-------------------- ")

#文件上传
def filesUpload(hostname,port,username,password,local_dir,remote_dir): 
    try:
        #必须传入一个tuple
        t=paramiko.Transport((hostname,string.atoi(port)))
        #必须使用这种形式，connect内部进行类型转换
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        print 'begin to upload file to %s' % hostname
        for root,dirs,files in os.walk(local_dir):
            #上传目录中的文件
            for filespath in files:
                local_file = os.path.join(root,filespath)
                a = local_file.replace(local_dir,remote_dir)
                remote_file = os.path.join(remote_dir,a)
                try:
                    sftp.put(local_file,remote_file)
                except Exception,e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file,remote_file)
                print "upload %s to remote %s" % (local_file,remote_file)
                infoLogger.info("upload %s to remote %s successfully" % (local_file,remote_file))
        print '%s is processed over--------------------'%(hostname)
        infoLogger.info(hostname+" is processed over---------------")
        t.close()
    except Exception,e:
        print e
        print '%s failed!-------------------- '%(hostname)
        errorLogger.error(hostname+" failed!-------------------- ")



#文件下载
def filesDownload(hostname,port,username,password,local_dir,remote_dir):
    try:
        t=paramiko.Transport((hostname,string.atoi(port)))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        #print sftp.listdir(remote_dir)
        for files in sftp.listdir(remote_dir):
            remote_path = os.path.join(remote_dir,files)
            a = remote_path.replace(remote_dir,local_dir)
            local_path = os.path.join(local_dir,files)
            sftp.get(remote_path,local_path)
            print "download %s from remote %s" % (files,remote_dir)
            infoLogger.info("download %s from remote %s successfully" % (local_path,remote_path))
            oldfile=os.path.join(os.getcwd(),local_dir[:-1]+os.sep+str(files))
            newfile=os.path.join(os.getcwd(),local_dir[:-1]+os.sep+str(hostname)+"_"+str(files))
            os.rename(oldfile,newfile)
        print '%s is processed over--------------------'%(hostname)
        infoLogger.info(hostname+" is processed over---------------")
        t.close()
    except Exception,e:
        print e
        print '%s failed!-------------------- '%(hostname)
        errorLogger.error(hostname+" failed!-------------------- ")


        
if __name__=='__main__':
    host_list = confRead.read_configBySection('config.ini', 'HOST')
    remote_dir = confRead.read_config('config.ini', 'DOWNLOADS_REMOTE_DIR', 'REMOTE_DIR')
    for each_host in host_list:
        hostConf_list = each_host[1].strip().split(':')
        hostname = hostConf_list[0]
        port = hostConf_list[1]
        username = hostConf_list[2]
        passwd = hostConf_list[3]
        local_dir = 'downloads/'    
        #filesUpload(hostname,port,username,passwd,local_dir,remote_dir)
        filesDownload(hostname,port,username,passwd,local_dir,remote_dir)


    
    
    
