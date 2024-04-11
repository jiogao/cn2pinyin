# 批量修改文件名
import os
import pinyin


# 把中文改为拼音
def rename_chinese(path):
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isdir(file_path):
            rename_chinese(file_path)
        else:
            new_name = pinyin.get(file_name, format="strip", delimiter="")
            new_path = os.path.join(path, new_name)
            # 循环判断同名文件是否存在
            # 如果存在，则在文件名后面数字加1
            i = 1
            # 分别获取文件名和后缀名
            only_name, suffix = os.path.splitext(new_name)
            while os.path.exists(new_path):
                new_name_with_num = only_name + "_" + str(i) + suffix
                new_path = os.path.join(path, new_name_with_num)
                i += 1

            os.rename(file_path, new_path)
