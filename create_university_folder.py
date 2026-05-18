import os
import shutil

def create_folder(folder_name, folder_type="sub"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    if folder_type == "sub":
        subfolders = ["授業", "未提出", "提出済み"]
        for subfolder in subfolders:
            create_folder(os.path.join(folder_name, subfolder), folder_type="none")
            if subfolder == "授業":
                create_folder_numbers("class", os.path.join(folder_name, subfolder), 16)
            elif subfolder == "未提出":
                create_folder_numbers("file", os.path.join(folder_name, subfolder), 16)
def create_folder_numbers(name,folder_name,numbers):
    for i in range(1, numbers+1):
        n=name+str(i)
        create_folder(os.path.join(folder_name, n), folder_type="none")

if __name__ == "__main__":
    folder_list = []
    top_folder = "example"
    create_folder(top_folder, folder_type="top")
    files = os.listdir('.')
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