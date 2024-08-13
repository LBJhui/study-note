# _*_ coding: utf-8 _*_
# @Time: 2024/3/26 10:13
# @Author: LBJ辉
# @File: os
# @Project: nxops

import os

'''
os 模块常用功能:
    文件的目录、路径操作
    进程管理
    环境参数的设置
'''

# 返回当前工作目录(文件夹)
print(os.getcwd())  # D:\Desktop\note-docsify\nxops\note
# 新建一个文件夹，如果文件夹已存在会报错
# os.mkdir('url')
# 跳转当前文件路径
os.chdir('../nxops')
# 获得路径下的所有文件名称：一层
print(os.listdir('./'))
# 返回是否是文件夹
print(os.path.isdir(os.getcwd()))  # True
# 返回是否是文件
print(os.path.isfile(os.getcwd()))  # False
# 将文件路径进行拆分
print(os.path.split(os.getcwd()))  # ('D:\\Desktop\\note-docsify\\nxops', 'nxops')
# 修改文件名称
# os.rename('要修改的文件', '修改后的文件名')
# 连接两个或更多的路径名组件
print(os.path.join(os.getcwd(), 'os.py'))  # D:\Desktop\note-docsify\nxops\note\os.py

# os.environ 可以获取有关系统的各种信息
print('os.environ', os.environ)
{
		'ALLUSERSPROFILE': 'C:\\ProgramData',
		'APPCODE_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\appcode.vmoptions',
		'APPDATA': 'C:\\Users\\LBJ辉\\AppData\\Roaming',
		'CLION_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\clion.vmoptions',
		'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
		'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
		'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
		'COMPUTERNAME': 'LAPTOP-II9VDB3Q',
		'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
		'DATAGRIP': 'D:\\LenovoSoftstore\\DataGrip 2021.2.2\\bin;',
		'DATAGRIP_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\datagrip.vmoptions',
		'DATASPELL_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\dataspell.vmoptions',
		'DEVECOSTUDIO_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\devecostudio.vmoptions',
		'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
		'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',
		'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
		'GATEWAY_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\gateway.vmoptions',
		'GOLAND_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\goland.vmoptions', 'HOMEDRIVE': 'C:',
		'HOMEPATH': '\\Users\\LBJ辉', 'IDEA_INITIAL_DIRECTORY': 'C:\\Windows\\System32',
		'IDEA_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\idea.vmoptions',
		'INTELLIJ IDEA': 'C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin;',
		'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-17',
		'JETBRAINSCLIENT_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\jetbrainsclient.vmoptions',
		'JETBRAINS_CLIENT_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\jetbrains_client.vmoptions',
		'LOCALAPPDATA': 'C:\\Users\\LBJ辉\\AppData\\Local', 'LOGONSERVER': '\\\\LAPTOP-II9VDB3Q',
		'NODE_PATH': 'C:\\Program Files\\nodejs', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\LBJ辉\\OneDrive',
		'OS': 'Windows_NT',
		'PATH': 'C:\\Program Files\\Java\\jdk-17\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin;D:\\mingw\\mingw64\\bin;C:\\Program Files\\Apache Software Foundation\\apache-tomcat-8.5.81\\lib;C:\\Program Files\\Apache Software Foundation\\apache-tomcat-8.5.81\\bin;C:\\Program Files\\Apache Software Foundation\\apache-maven-3.8.6\\bin;C:\\Program Files\\nodejs\\;C:\\Program Files\\Git\\cmd;C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\dll;C:\\Program Files\\Microsoft VS Code\\bin;C:\\Users\\LBJ辉\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\LBJ辉\\AppData\\Local\\Programs\\Python\\Python38\\;C:\\Users\\LBJ辉\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin\\;C:\\Users\\LBJ辉\\AppData\\Local\\Microsoft\\WindowsApps;D:\\LenovoSoftstore\\DataGrip 2021.2.2\\bin;;C:\\Program Files\\MongoDB\\Server\\5.0\\bin;D:\\Apache-Subversion-1.14.2\\bin;C:\\Program Files\\nodejs;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin;;C:\\Program Files (x86)\\Prince\\engine\\bin;D:\\mingw\\mingw64\\bin;C:\\Windows\\system32;C:\\Users\\LBJ辉\\AppData\\Roaming\\npm;C:\\Program Files\\Git\\bin;C:\\Users\\LBJ辉\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;“C:\\Program Files\\nodejs”;C:\\Program Files\\JetBrains\\PyCharm 2023.1\\bin;;',
		'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',
		'PHPSTORM_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\phpstorm.vmoptions', 'PROCESSOR_ARCHITECTURE': 'AMD64',
		'PROCESSOR_IDENTIFIER': 'AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD', 'PROCESSOR_LEVEL': '25',
		'PROCESSOR_REVISION': '5000', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files',
		'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files',
		'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
		'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2023.1\\bin;',
		'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1',
		'PYCHARM_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\pycharm.vmoptions', 'PYTHONIOENCODING': 'UTF-8',
		'PYTHONPATH': 'D:\\Desktop\\note-docsify\\nxops;C:/Program Files/JetBrains/PyCharm 2023.1/plugins/python/helpers/pycharm_matplotlib_backend;C:/Program Files/JetBrains/PyCharm 2023.1/plugins/python/helpers/pycharm_display',
		'PYTHONUNBUFFERED': '1', 'RIDER_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\rider.vmoptions',
		'RUBYMINE_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\rubymine.vmoptions', 'SESSIONNAME': 'Console',
		'STUDIO_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\studio.vmoptions', 'SYSTEMDRIVE': 'C:',
		'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\LBJ辉\\AppData\\Local\\Temp',
		'TMP': 'C:\\Users\\LBJ辉\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-II9VDB3Q',
		'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-II9VDB3Q', 'USERNAME': 'LBJ辉', 'USERPROFILE': 'C:\\Users\\LBJ辉',
		'WEBIDE_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\webide.vmoptions',
		'WEBSTORM_VM_OPTIONS': 'C:\\Crack\\jetbra\\vmoptions\\webstorm.vmoptions', 'WINDIR': 'C:\\Windows',
		'WXDRIVE_START_ARGS': '--wxdrive-setting=0 --disable-gpu --disable-software-rasterizer --enable-features=NetworkServiceInProcess'
}
