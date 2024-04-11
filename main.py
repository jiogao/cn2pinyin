from module.translate_file_name import rename_chinese

import sys

if __name__ == '__main__':
    # 传入命令行参数为文件夹路径
    print(sys.argv[1])
    rename_chinese(sys.argv[1])
