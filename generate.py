#!/usr/local/bin/python3
# I referred to this article:
# https://pyteyon.hatenablog.com/entry/2018/08/25/202908

import os


def make_contest_dir(contest_name, contest_num, question):
    """Make Contest Dir
    make dir ABX_XXX
    make dir/ABX_XXX_question.cpp
    make dir/CmakeLists.txt
    Arguments
    :contest_name: str ex) "ABC", "ARC"
    :contest_num: str or int ex) "078", "103", "104"
    :quesion_num: str ex) "ABCD", "ABCDEFG"
    """
    contest_path = "{}_{}".format(contest_name, contest_num)  # ex) ABC_105
    
    # make directory
    try:
        os.makedirs(contest_path)  # exist_ok=True 同名ディレクトリが存在した時にエラーを出さないオプション
        flag = True
    except FileExistsError: 
        print("Error Message:", e.strerror)
        print("Error Num:", e.errno)
        print("Can't make '", e.filename, "'\n")
        flag = False

    # make CmakeLists.txt
    version = 3.10
    head = ["cmake_minimum_required(VERSION {})\n".format(version),
            "project({}_{})\n".format(contest_name, contest_num),
            "set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} -std=c++11)\n",
            "\n"]
    executable = ["{}_{}{}_{}".format(str(index + 1), contest_name, contest_num, q) for index, q in enumerate(question)]  # ex) ABC104_C
    text_list = ["add_executable({0} {0}.cpp)\n".format(exe) for exe in executable]
    output = head + text_list  # CMakeLists.txt に書き込むリスト
    with open("{}/CMakeLists.txt".format(contest_path), "w", encoding="utf-8") as file:
        file.writelines(output)  # リスト型変数を改行なしでファイルに書き込む

    
    with open("template.cpp", "r", encoding="utf-8") as template:
        text = template.read()
        for exe in executable:
            with open("{}/{}.cpp".format(contest_path, exe),
                      "w", encoding="utf-8") as cpp_file:
                cpp_file.write("// {}\n".format(exe))
                cpp_file.write(text)
                
    # print directory structure
    if flag:
        print("Made directory {}".format(contest_path))
        print("--- structure ---")
        print(contest_path + "/")

        files = os.listdir(contest_path)

        for i in files:
            if i == files[-1]:
                print(" └─ " + i)
            else:
                print(" ├─ " + i)


if __name__ == '__main__':
    name, num, ques = input().split(" ")
    make_contest_dir(name, num, ques)
