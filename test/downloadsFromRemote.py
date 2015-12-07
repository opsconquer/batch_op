import ssh_connect
import confRead

#download files from remote host dir
if __name__=='__main__':
    host_list = confRead.read_configBySection('config.ini', 'HOST')
    remote_dir = confRead.read_config('config.ini', 'DOWNLOADS_REMOTE_DIR', 'REMOTE_DIR')
    for each_host in host_list:
        hostConf_list = each_host[1].strip().split(':')
        hostname = hostConf_list[0]
        port = hostConf_list[1]
        username = hostConf_list[2]
        passwd = hostConf_list[3]
        print remote_dir
        local_dir = 'downloads/'    
        #filesUpload(hostname,port,username,passwd,local_dir,remote_dir)
        ssh_connect.filesDownload(hostname,port,username,passwd,local_dir,remote_dir)
