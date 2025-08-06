# Steam Game SAVES 還原程式
#
import sys,os,shutil

with open("game_save_path.ini","r",encoding="utf-8") as f:
    DIST_FOLDER_PATH=f.read()
DIST_FOLDER_PATH=DIST_FOLDER_PATH.replace("\n","").strip()+"\\"

def is_folder_or_file(path):
    if os.path.isfile(path):
        #print(f"{path} 是一個檔案")
        return 'FILE'
    elif os.path.isdir(path):
        #print(f"{path} 是一個目錄")
        return 'FOLDER'
    else:
        #print(f"{path} 不是有效的檔案或目錄")
        return 'FALSE'

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

if __name__ == '__main__':
    try:
        if len(sys.argv)>1 and sys.argv[1]!="":
            #print(argv[1])
            ck = is_folder_or_file(sys.argv[1])
            if ck:
                copy_directory_with_overwrite(sys.argv[1], DIST_FOLDER_PATH)
            else:
                pass
        else:
            print('no thing')
    except:
        pass
    input("press enter key to exit...")
