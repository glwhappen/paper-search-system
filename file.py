import os
import hashlib

def get_files(path):
    """
    获取文件夹下的所有文件
    :param path: 文件夹路径
    :return: 文件夹下的所有文件
    """
    files = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            # 判断文件是否是pdf
            if file.endswith('.pdf'):
                files.append(os.path.join(current_dir, path, file))
    return files


def calculate_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5_hash = hashlib.md5()
        while chunk := f.read(8192):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()
