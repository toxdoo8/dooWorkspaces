import os

jenkins_server='10.11.3.125'
jenkins_login='qa'
jenkins_password='qa'
jenkins_old_builds='/home/codebuilder/builds/ice-build-ap-stable /'
# setup=sh /home/bytonsqa/setup.sh

print(jenkins_server,jenkins_login,jenkins_old_builds)
for i in range(1,3):
    print('hello world:',i)

print(os.getcwdb())
print('hello world')
