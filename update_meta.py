import os
import sys

def find_meta_files(folder):
    meta_files = []
    for root, dirs, files in os.walk(folder):

        for file in files:
            if file.endswith('meta.yaml'):
                meta_files.append(os.path.join(root, file))
    return meta_files


folder_path = 'E:\\home/rvlaar/mlflow'

replace = sys.argv[1] == '1'

print(replace)

meta_paths = find_meta_files(folder_path)

print('Starting')
for meta_path in meta_paths:
    print(meta_path)
    with open(meta_path, 'r+') as meta_file:
        content = meta_file.read()
        print(content)
        content = content.replace('/home/rvlaar/.mlflow/', 'file://E:\\'+'/home/rvlaar/mlflow/') if replace \
            else content.replace('file://E:\\'+'/home/rvlaar/mlflow/', '/home/rvlaar/.mlflow/')
        print(content)
        meta_file.seek(0)
        meta_file.truncate()
        meta_file.write(content)
