import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
name_list = []
# リストにデーターを追加する方法
# リスト名.append(内容)

# ループ処理
# for 代入したい関数名 in 繰り返し処理させたい内容(リストなども使用可)

# 既存の関数に文字を追加する方法
# 関数名 += 内容
# 例) num = 100
# num += 25
# print(num)　結果：125
# 改行コード　Option(⌥) + ¥で\を出す
# \n　←これが改行コード
# 例) num += j + "\n"


def add_button_action():
    # ↓ここにすべての処理を書いてね
    name_out = ""   # name_outに結果をいれる
    name = entry1.get()
    name_list.append(name)
    for i in name_list:
        name_out += i + "\n"
    print(name_out)
    label2.config(text=name_out)
    # ↑


#  1. ラベル: 名前を入力してください
label1 = tk.Label(window, text="名前を入力してください", bg=fg_color, fg=bg_color)
label1.pack(pady=10)

#  2. エントリー: 名前を入力するための入力フィールド
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
#  3. ボタン: ボタンを押すと配列に名前が追加される
button1 = tk.Button(window, text="name", command=add_button_action)  # 足し算ボタン
button1.pack(pady=10)

#  4. ラベル: 配列に追加された名前を表示する
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
