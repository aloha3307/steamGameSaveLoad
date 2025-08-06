# Steam Game SAVES 備份程式
#

import os,shutil

from datetime import datetime
current_time=(datetime.now().strftime('%Y%m%d%H%M%S'))

def copy_directory_with_overwrite(src, dst):
    """
    使用shutil.copytree复制目录，如果目标目录已存在，则先删除再复制。
    """
    if os.path.exists(dst):
        try:
            shutil.rmtree(dst)
        except OSError as e:
            print(f"无法删除目标目录 '{dst}': {e}")
            return
    try:
        shutil.copytree(src, dst)
    except Exception as e:
         print(f"复制目录时出错: {e}")

sav_note=input("請輸入存檔備註?(英文或數字為佳，若無備註直接按Enter開始備份)")

with open("game_save_path.ini","r",encoding="utf-8") as f:
    source_dir=f.read()
source_dir=source_dir.replace("\n","").strip()

dist_dir = os.getcwd()

# 指定文件路徑
if sav_note!="":
    new_folder_name = f"GAME-SAV-{current_time}-{sav_note}"
else:
    new_folder_name = f"GAME-SAV-{current_time}"

dist_folder_path = dist_dir+"\\"+new_folder_name

copy_directory_with_overwrite(source_dir, dist_folder_path)
##################################################
##################################################
input(f'GAME存檔備份完成! 資料夾:{dist_folder_path}')

