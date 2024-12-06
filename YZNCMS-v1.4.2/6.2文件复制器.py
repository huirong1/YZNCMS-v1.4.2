import shutil
import sys

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"文件已从 {src} 复制到 {dest}")
    except IOError as e:
        print(f"无法复制文件. {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python 6.2文件复制器.py <源文件路径> <目标文件路径>")
    else:
        src = sys.argv[1]
        dest = sys.argv[2]
        copy_file(src, dest)