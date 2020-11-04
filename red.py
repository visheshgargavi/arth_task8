import os
import getpass
os.system("tput setaf 3")
print("\t\t\t\tPikachu Welcomes you...")
os.system("tput setaf 7")
print("\t\t\t\t---------------------")

password = getpass.getpass('Enter password : ')

if password != "aviforever":
    print('wrong password')
    exit()

def core():
    nn_ip = input('Enter NameNode ip and hadoop port eg. hdfs://1.2.3.4:9000:')
    print(nn_ip)
    os.system('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml')
    os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
    os.system("echo \<value\>{}\<\/value\> >> core-site.xml".format(nn_ip))
    os.system('echo \<\/property\> >> core-site.xml')
    os.system("echo \<\/configuration\> >> core-site.xml")
    os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
    os.system("rm -rf core-site.xml")
    os.system("cp cp.xml core-site.xml")
def hdfs():
    dndir = input('Enter directory name you want to create for datanode:')
    print(dndir)

    os.system('echo \<configuration\> >> hdfs-site.xml')
    os.system('echo \<property\> >> hdfs-site.xml')
    os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
    os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(dndir))
    os.system('echo \<\/property\> >> hdfs-site.xml')
    os.system("echo \<\/configuration\> >> hdfs-site.xml")
    os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))

    os.system("ssh {} mkdir {}".format(ip,dndir))
    os.system("rm -rf hdfs-site.xml")
    os.system("cp hd.xml hdfs-site.xml")
def data():
    dir = input('Enter directory name where java and hadoop file resides:')
    print(dir)
    os.system('ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm'.format(ip,dir))
    os.system("ssh {} rpm -i {}\/hadoop-1.2.1-1.x86_64.rpm --force".format(ip,dir))
    core()
    hdfs()
    os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
    os.system("ssh {} jps".format(ip))


def yum():
    i = input('Enter folder_name/repo_name u want to mount to :')
    print('Before using this tool make sure your dvd is not mounted anywhere if use our 6th option then use this configure yum')
    os.system('ssh {} mkdir \/{}'.format(ip,i))
    os.system('ssh {} mount \/dev\/cdrom \/dvd'.format(ip))
    os.system('ssh {} touch \/etc\/yum.repos.d\/{}\.repo'.format(ip,i))
    os.system('ssh {} echo \[dvd\] \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip))
    os.system('ssh {} echo baseurl\=file\\\:\/\/{}\/BaseOS \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip,i))
    os.system('ssh {} echo gpgcheck\=0 \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip))
    os.system('ssh {} echo \[dvd1\] \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip))
    os.system('ssh {} echo baseurl\=file\\\:\/\/{}\/AppStream \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip,i))
    os.system('ssh {} echo gpgcheck \= 0 \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip))
    os.system('ssh {} echo mount \/dev\/cdrom {} \>\> \/etc\/rc.d\/rc.local'.format(ip,i))
    os.system('ssh {} chmod +x \/etc\/rc.d\/rc.local'.format(ip))
    os.system('ssh {} yum clean all'.format(ip))
    os.system('ssh {} yum repolist'.format(ip))

def unmount():
    i = input('Enter location where ur dvd was mounted')
    os.system('ssh {} umount /dev/cdrom {}'.format(ip,i))

def docker():
    print('Before configuring docker make sure your yum is configured if not choose option 5 first then configure docker')
    os.system('ssh {} sudo yum config\-manager \-\-add\-repo\=https\:\/\/download.docker.com\/linux\/centos\/docker\-ce\.repo'.format(ip))
    os.system('ssh {} dnf install docker-ce --nobest -y'.format(ip))
    os.system('ssh {} systemctl start docker'.format(ip))
    os.system('ssh {} systemctl status docker'.format(ip))

def webserver():
    print('Before configuring webserver make sure your yum is configured if not choose option 5 first')
    os.system('ssh {} yum install httpd -y'.format(ip))
    os.system('ssh {} systemctl start httpd'.format(ip))
    os.system('ssh {} systemctl enable httpd'.format(ip))
    os.system('ssh {} systemctl status httpd'.format(ip))
    os.system('ssh {} echo Automation \>\> \/var\/www\/html\/auto.html'.format(ip))
    os.system('curl -I http\:\/\/{}\/auto.html'.format(ip))

def d_image_webserver():
    print('Before creating the image make sure u have configured docker')
    os.system('ssh {} docker pull centos:latest'.format(ip))
    i = input('Enter os name')
    n = input('Enter image_name u want to create')
    os.system('ssh {} docker run -dit --name {} centos:latest'.format(ip,i))
    os.system('ssh {} docker exec -i {} yum install net-tools -y'.format(ip,i))
    os.system('ssh {} docker exec -i {} yum install httpd -y'.format(ip,i))
    os.system('ssh {} docker commit {} {}:v1'.format(ip,i,n))
    os.system('ssh {} docker images'.format(ip))

def d_webserver():
    p = int(input('Enter port :'))
    i = input('Enter os_name:')
    n = input('Enter image_name with version:')
    os.system('ssh {} docker run -dit --name {} -p {}:80 {}'.format(ip,i,p,n))
    os.system('ssh {} docker exec -i {} /usr/sbin/httpd'.format(ip,i))
    os.system('curl http\:\/\/{}\:{}'.format(ip,p))

def fdisk():
    d = input('Enter drive name: ')
    e = input('Enter filters eg. -l: ')
    os.system('ssh {} fdisk {} {}'.format(ip,d,e))

def pvcreate():
    d = input('Enter disk name u want to convert to physical volume: ')
    os.system('ssh {} pvcreate {}'.format(ip,d))

def pvdisplay():
    d = input('Enter disk name: ')
    os.system('ssh {} pvdisplay {}'.format(ip,d))

def vgcreate():
    i = input('Enter vg name: ')
    d = input('Enter disks name u want to add: ')
    os.system('ssh {} vgcreate {} {}'.format(ip,i,d))

def vgdisplay():
    v = input('Enter the volume group name: ')
    os.system('ssh {} vgdisplay {}'.format(ip,v))

def lvcreate():
    s = input('Enter the size eg.5G,10G: ')
    l = input('Enter the name of logical volume u create: ')
    v = input('Enter volume group: ')
    os.system('ssh {} lvcreate --size {} --name {} {}'.format(ip,s,l,v))

def lvdisplay():
    d = input('Enter the lv name eg. /dev/vg_name/lv_name')
    os.system('ssh {} lvdisplay {}'.format(ip,d))

def mount():
    d = input('Enter destination: ')
    disk = input('Enter disk or lv name u want to mount')
    os.system('ssh {} mount {} {}'.format(ip,disk,d))

def mkfs():
    d = input('Enter disk or lv_name you want to format: ')
    f = input('Enter format in which u want to format: ')
    os.system('ssh {} mkfs.{} {}'.format(ip,f,d))

def partition():
    os.system('ssh {} fdisk -l'.format(ip))
    d = input('Enter disk name: '.format(ip))
    os.system('ssh {} fdisk {}'.format(ip,d))
    mkfs()
    os.system('ssh {} udevadm settle'.format(ip))
    mount()

def LVM():
    fdisk()
    i = 0
    n = int(input('Enter number of disk u want to add: '))
    for i in range(n):
        pvcreate()
        i+=1
    vgcreate()
    vgdisplay()
    lvcreate()
    lvdisplay()
    mkfs()
    mount()
    os.system("ssh {} df -h".format(ip))

def lvextend():
    s = input('Enter size eg.5G,10G: ')
    n = input('Enter logical_Volume name eg. /dev/hadoop/mylv1: ')
    os.system('ssh {} lvextend --size +{} {}'.format(ip,s,n))

def resize2fs():
    n = input('Enter logical_Volume name eg. /dev/hadoop/mylv1: ')
    os.system('ssh {} resize2fs {}'.format(ip,n))
    os.system('ssh {} df -h'.format(ip))

def lvreduce():
    n = input('Enter value: ')
    l = input('Enter logical_Volume name eg. /dev/hadoop/mylv1: ')
    os.system('ssh {} lvreduce -L {} {}'.format(ip,n,l))

r = input('How you want to login as?(local/remote)')
print(r)

while True:
        print("\n \n")
        print("""
        Press 1: date
        Press 2: cal
        Press 3: configure_data_node
        Press 4: configuring_docker
        Press 5: configuring_yum
        Press 6: unmount dvd
        Press 7: configuring_local_webserver
        Press 8: docker_webserver_image
        Press 9: configuring_webserver_inside_docker
        Press 10: fdisk -l
        Press 11: fdisk /dev/*** -l
        Press 12: pvcreate
        Press 13: pvdisplay
        Press 14: vgdisplay
        Press 15: vgcreate
        Press 16: lvcreate
        Press 17: lvdisplay
        Press 18: mkfs.ext4
        Press 19: mount command
        Press 20: static_partition
        Press 21: lvextend
        Press 22: LVM
        Press 23: resize2fs
        Press 24: lvreduce
        Press 25: to exit
        """)

        if r == "local":
                i = int(input("Enter ur choice : "))
                print(i)
                if i==1:
                        os.system("date")
                elif i==2:
                        os.system("cal")
                elif i==3:
                        data()
                elif i==4:
                        docker()
                elif i==5:
                        yum()
                elif i==10:
                        exit()
                else:
                        os.system("hadoop dfsadmin -report")
        else:
            ip = input('Enter Remote Ip:')
            print(ip)

            i = int(input("Enter ur choice"))
            print(i)
            if i==1:
                os.system("ssh {} date".format(ip))
            elif i==2:
                os.system("cal")
            elif i==3:
                data()
            elif i==4:
                docker()
            elif i==5:
                yum()
            elif i==6:
                unmount()
            elif i==7:
                webserver()
            elif i==8:
                d_image_webserver()
            elif i==9:
                d_webserver()
            elif i==10:
                os.system("ssh {} fdisk -l".format(ip))
            elif i==11:
                fdisk()
            elif i==12:
                pvcreate()
            elif i==13:
                pvdisplay()
            elif i==14:
                vgdisplay()
            elif i==15:
                vgcreate()
            elif i==16:
                lvcreate()
            elif i==17:
                lvdisplay()
            elif i==18:
                mkfs()
            elif i==19:
                mount()
            elif i==20:
                partition()
            elif i==21:
                lvextend()
            elif i==22:
                LVM()
            elif i==23:
                resize2fs()
            elif i==24:
                lvreduce()
            elif i==25:
                exit()
            else:
                os.system("hadoop dfsadmin -report")
