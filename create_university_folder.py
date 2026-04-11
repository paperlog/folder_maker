import os
import shutil

def create_folder(folder_name, folder_type="sub"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"{folder_name} を作成しました")
    else:
        print(f"{folder_name} はすでに存在します")
    
    if folder_type == "sub":
        subfolders = ["授業", "提出済み", "未提出"]
        for subfolder in subfolders:
            create_folder(os.path.join(folder_name, subfolder), folder_type="none")

if __name__ == "__main__":
    folder_list = []
    top_folder = "example"
    create_folder(top_folder, folder_type="top")
    shutil.copy("deadline.py", top_folder)
    print("deadline.pyをexample内に作成しました")
    while True:
        print(f"フォルダーリスト:{folder_list}")
        class_name = input("授業名を入力してください。入力を終了する際には[end]と入力してください: ")
        if class_name == "end" or class_name == "[end]":
            break
        if class_name == "":
            print("授業名を入力するか[end]を入力してください。")
            continue
        folder_list.append(class_name)
    for folder in folder_list:
        create_folder(os.path.join(top_folder, folder))
    input("完了しました。Enterキーを押して終了してください。")