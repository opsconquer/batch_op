import ssh_connect
import confRead

if __name__=='__main__':
    cmd=[]
    #ѭ����ȡ�ű��ļ�
    script_list=confRead.read_configBySection('config.ini', 'SCRIPTS')
    print script_list
    for each_script in script_list:                     
        #�ӽű��ж�ȡִ�е������б�
        scriptFile=open(each_script[1]) #�򿪽ű��ļ�
        line=scriptFile.readlines() #��readlines��ȡ�ű��ļ����б�
        for m in line:
            cmd.append(m.strip())

    #�������ļ��ж�ȡ���Ӳ�����HOST_CONF = host:port:username:passwd
    #ѭ��ִ��
    host_list = confRead.read_configBySection('config.ini', 'HOST')
    for each_host in host_list:
        hostConf_list = each_host[1].strip().split(':')
        ip = hostConf_list[0]
        port = hostConf_list[1]
        username = hostConf_list[2]
        passwd = hostConf_list[3]
        ssh_connect.sshCmd(ip,port,username,passwd,cmd)
        #���߳�ִ��
        #threads = []   
        #a=threading.Thread(target=ssh,args=(ip,port,username,passwd,cmd))
        #a.start()
