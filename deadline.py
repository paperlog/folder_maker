import os

def get_folder_names(target_dir):
    try:
        return [name for name in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, name))]
    except FileNotFoundError:
        print(f"create_university_folderによって作られたフォルダ内に配置してください。")
        return []

text_file_name = "deadline.txt"

# 同階層のフォルダ名A取得
target_dir = '.'

# フォルダ名のみを取得
folders_a = get_folder_names(target_dir)

# それぞれの"フォルダ名A/未提出/"階層にあるフォルダ名B取得
folders_b = {}
for folder_a in folders_a:
    folder_b = get_folder_names(os.path.join(folder_a, "未提出"))
    folders_b[folder_a] = folder_b

# それぞれの"フォルダ名A/未提出/フォルダ名B/deadline.txt"の中身を取得
deadlines = {}
for folder_a, folder_b_list in folders_b.items():
    for folder_b in folder_b_list:
        try:
            with open(os.path.join(folder_a, "未提出", folder_b, text_file_name), "r", encoding="utf-8") as f:
                deadlines[(folder_a, folder_b)] = f.read().strip()
        except FileNotFoundError:
            deadlines[(folder_a, folder_b)] = "deadline.txtが見つかりませんでした。"

if deadlines=={}:
    print("現在、未提出の課題はありません。")
    input()
    exit()

# フォルダ名A：deadline.txtの内容　の形式で出力
for (folder_a, folder_b), deadline in deadlines.items():
    print(f"{folder_a}\n　{deadline}")

input()