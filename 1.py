from os import error
import subprocess
from django.conf import settings
from pathlib import Path
import re
import logging
import hashlib

class Process:

    def __init__(self) -> None:
        self.aapt_path = 'F:\\Android\Sdk\\build-tools\\30.0.3\\aapt.exe'
        self.apktool_path = 'F:\\AndroidDevelopTool\\apktool_2.5.0.jar'
        self.apk_path = "E:\\JoJo-Test\\mysite\\data\\apk\\Read.apk"

    def process_unzip_apk(self, file_path):
        """使用apktool解压apk

        Args:
            file_path (str): apk文件路径
        """

        try:
            
            path = 'E:\\JoJo-Test\\mysite\\output\\%s' % 'Read'
            print('java -jar E:\\JoJo-Test\\mysite\\data\jar\\apktool_2.5.0.jar d ' + file_path +' -o ' + str(path))
            # path.mkdir(exist_ok=True)
            p = subprocess.Popen(['java', '-jar' ,'E:\\JoJo-Test\\mysite\\data\jar\\apktool_2.5.0.jar','d' , file_path ,'-o' , str(path)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output,err = p.communicate()
            logging.warning(err)
            logging.warning(output)
        except Exception as e:
            print(e)

    def check_md5(self, file_path):
        """检查apkMD5值"""
        with open(file_path,'rb') as f:
            data = f.read()
        file_md5 = hashlib.md5(data).hexdigest()
        return file_md5


    def get_apk_base_info(self):  # 获取apk包的基本信息
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % 'E:\\JoJo-Test\\mysite\\data\\apk\\Read.apk',
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        package_match = re.compile(
            "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not package_match:
            raise Exception("can't get package,versioncode,version")
        package_name = package_match.group(1)
        version_code = package_match.group(2)
        version_name = package_match.group(3)
        launch_activity_match = re.compile(
            "launchable-activity: name='(\S+)'").search(output.decode())
        if not launch_activity_match:
            raise Exception("can't get launch_activity")
        launch_activity = launch_activity_match.group(1)
        sdk_version_match = re.compile(
            "sdkVersion:'(\S+)'").search(output.decode())
        if not sdk_version_match:
            raise Exception("can't get min_sdk_version")
        min_sdk_version = sdk_version_match.group(1)
        target_sdk_version_match = re.compile(
            "targetSdkVersion:'(\S+)'").search(output.decode())
        if not target_sdk_version_match:
            raise Exception("can't get target_sdk_version")
        target_sdk_version = target_sdk_version_match.group(1)
        application_label_match = re.compile(
            "application-label:'([\u4e00-\u9fa5_a-zA-Z0-9-\S]+)'").search(output.decode())
        if not application_label_match:
            raise Exception("can't get application_label")
        application_label = application_label_match.group(1)
        p.kill()
        return package_name, version_name, version_code, launch_activity, min_sdk_version, target_sdk_version, application_label


if __name__ == '__main__':
    p = Process()
    print(p.process_unzip_apk(p.apk_path))