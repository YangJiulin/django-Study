import os
import platform
import subprocess
from django.conf import settings
from pathlib import Path
import re
import logging
import hashlib


class Process:

    def __init__(self) -> None:
        self.aapt_path = str(Path(self._get_path(
            'ANDROID_HOME')) / 'build-tools/30.0.3/aapt.exe' if platform.system()=='Windows' else 'build-tools/30.0.3/aapt')
        self.apktool_path = str(settings.BASE_DIR / 'data/jar/apktool_2.5.0.jar')

    def _get_path(self, name):
        """
        整理到工具类
        name: 环境变量名
        """
        result = os.environ.get(name, None)
        # if not result:
        #     try:
        #         result = settings.name
        #     except:
        #         result = None
        return result

    def process_unzip_apk(self, file_path):
        """使用apktool解压apk

        Args:
            file_path (str): apk文件路径
        """

        try:
            pattern = re.compile(r'.*[/\\](.*).apk$')
            apk_name = re.match(pattern, file_path).group(1)
            out_path = str(settings.BASE_DIR / ('output/%s' % apk_name))
            print('java -jar E:\\JoJo-Test\\mysite\\data\jar\\apktool_2.5.0.jar d ' +
                  file_path + ' -o ' + str(out_path))
            # path.mkdir(exist_ok=True)
            p = subprocess.Popen(['java', '-jar', self.apktool_path, 'd', file_path, '-o', str(out_path)],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output, err = p.communicate()
            logging.warning(err)
            logging.warning(output)
        except Exception as e:
            print(e)

    def get_md5(self, file):
        """检查apkMD5值"""
        d5 = hashlib.md5()
        for chunk in file.chunks():
            d5.update(chunk)
        file_md5 = d5.hexdigest()
        # with open(file, 'rb') as f:
        #     data = f.read()
        # file_md5 = hashlib.md5(data).hexdigest()
        return file_md5

    def get_apk_base_info(self,apk_path):  # 获取apk包的基本信息
        p = subprocess.Popen(self.aapt_path + " dump badging %s" % apk_path,
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
    print(p.get_apk_base_info())
