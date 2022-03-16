import os

base_path = r'D:\user\同步文件\Python\geek_crawler'
dir_list = os.listdir(base_path)
dir_list = [
    base_path + '\\' + i for i in dir_list
    if os.path.isdir(base_path + '\\' + i) and i != '.git'
]
for dir in dir_list:
    file_list = os.listdir(dir)
    file_list = [dir + '\\' + i for i in file_list if '.html' in i]
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'img {\n      max-width: 100%\n    }' in content:
            break
        else:
            str_flag = '._2sjJGcOH_0 ._3Hkula0k_0 {\n      color: #b2b2b2;\n      font-size: 14px;\n    }'
            target_content = '._2sjJGcOH_0 ._3Hkula0k_0 {\n      color: #b2b2b2;\n      font-size: 14px;\n    }\n    img {\n      max-width: 100%\n    }'
            img_flag = 'img {\n      width: 544px;\n    }'
            content = content.replace(str_flag, target_content)
            content = content.replace(img_flag, '')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
