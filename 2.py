# import base64
# import json
# import urllib
# from django.conf import settings
# from pathlib import Path
# import gzip

# s = """eyJkaXN0aW5jdF9pZCI6IjEwMDEyMDAwIiwibGliIjp7IiRsaWIiOiJqcyIsIiRsaWJfbWV0aG9kIjoiY29kZSIsIiRsaWJfdmVyc2lvbiI6IjEuMTUuMjAifSwicHJvcGVydGllcyI6eyIkdGltZXpvbmVfb2Zmc2V0IjotNDgwLCIkc2NyZWVuX2hlaWdodCI6ODk2LCIkc2NyZWVuX3dpZHRoIjo0MTQsIiRsaWIiOiJqcyIsIiRsaWJfdmVyc2lvbiI6IjEuMTUuMjAiLCIkbGF0ZXN0X3RyYWZmaWNfc291cmNlX3R5cGUiOiLnm7TmjqXmtYHph48iLCIkbGF0ZXN0X3NlYXJjaF9rZXl3b3JkIjoi5pyq5Y%2BW5Yiw5YC8X%2BebtOaOpeaJk%2BW8gCIsIiRsYXRlc3RfcmVmZXJyZXIiOiIiLCJ1aWQiOiIxMDAxMjAwMCIsInVzZXJfaGFzaF9pZCI6IjFiMjU2YmI3OTA1YmFkMzkzYTNlYjEyZmIxOGE0Yjk4IiwicGxhdGZvcm1fdHlwZSI6Img1IiwibG9iIjoibWFya2V0aW5nIiwibG9iX3dlYiI6Im1hcmtldGluZyIsImN1c3RvbV9wbGF0Zm9ybSI6Ind4IiwiJHJlZmVycmVyIjoiIiwiJHVybCI6Imh0dHBzOi8vYWN0LnRpbm1hbi5jbi9lbmNvdXJhZ2UvZnh5ai90YXNrP2NoYW5uZWw9Q1JfUE9TVEVSX05PTkVfZnhoZC1teWNlbnRlciIsIiR1cmxfcGF0aCI6Ii9lbmNvdXJhZ2UvZnh5ai90YXNrIiwiJHRpdGxlIjoi5YiG5Lqr5pyJ5aWWIiwic2VydmVyX3RpbWUiOjE2MTUxOTkxMDk1MDQsImNoYW5uZWwiOiJDUl9QT1NURVJfTk9ORV9meGhkLW15Y2VudGVyIiwiJGlzX2ZpcnN0X2RheSI6ZmFsc2UsIiRpc19maXJzdF90aW1lIjpmYWxzZSwiJHJlZmVycmVyX2hvc3QiOiIifSwibG9naW5faWQiOiIxMDAxMjAwMCIsImFub255bW91c19pZCI6IjE3N2VkMzJiOWNjYTAwLTA4NjMzYzQyMGZjMGZlLTE2MDUxYjBhLTM3MDk0NC0xNzdlZDMyYjljZGMwMCIsInR5cGUiOiJ0cmFjayIsImV2ZW50IjoiJHBhZ2V2aWV3IiwiX3RyYWNrX2lkIjo1MDQ1MDk1NTB9"""
# # print(s.split('&')[1].split('=')[1])
# def gzip_decompress(data):
#         """
#         解密上报数据
#         :param data:
#         :return:
#         """
#         try:
#             return gzip.decompress(data)
#         except AttributeError:
#             from io import StringIO

#             buf = StringIO()
#             buf.write(data)
#             fd = gzip.GzipFile(fileobj=buf, mode="r")
#             fd.rewind()
#             value = fd.read()
#             fd.close()
#             return value
# gzip_data = urllib.parse.unquote(s)
# print(gzip_data)
# data_list = json.loads(gzip_decompress(base64.b64decode(gzip_data)).decode('utf8'))
# print(data_list)
import platform
print(platform.system())