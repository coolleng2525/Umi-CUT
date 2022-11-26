# 通过 pyinstaller 打包为 exe
# pip install opencv-python
# pip install Pillow
import os

dirPath = os.getcwd()

os.system(f'cd /d {dirPath}')
os.system(r'pyinstaller -F -w -i icon/icon.ico -n "Umi-CUT 批量图片去黑边" main.py')
