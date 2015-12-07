import ssh_connect
import confRead

if __name__=='__main__':
    cmd=[]
    #循环读取脚本文件
    script_list=confRead.read_configBySection('config.ini', 'SCRIPTS')
    print script_list
    for each_script in script_list:                     
        #从脚本中读取执行的命令列表
        scriptFile=open(each_script[1]) #打开脚本文件
        line=scriptFile.readlines() #用readlines读取脚本文件到列表
        for m in line:
            cmd.append(m.strip())

    #从配置文件中读取连接参数：HOST_CONF = host:port:username:passwd
    #循环执行
    host_list = confRead.read_configBySection('config.ini', 'HOST')
    for each_host in host_list:
        hostConf_list = each_host[1].strip().split(':')
        ip = hostConf_list[0]
        port = hostConf_list[1]
        username = hostConf_list[2]
        passwd = hostConf_list[3]
        ssh_connect.sshCmd(ip,port,username,passwd,cmd)
        #多线程执行
        #threads = []   
        #a=threading.Thread(target=ssh,args=(ip,port,username,passwd,cmd))
        #a.start()
