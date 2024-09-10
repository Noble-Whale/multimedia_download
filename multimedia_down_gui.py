from tkinter import *
import tkinter.messagebox as mbox
import tkinter.ttk as ttk
import multimedia_down as mmd

def process():
    if len(URL_space.get()) == 0:
        mbox.showinfo("Warning", "URL을 입력해주세요.")
        return
    elif len(target_combobox.get()) == 10:
        mbox.showinfo("Warning", "대상을 지정해주세요.")
        return
    else:
        try:
            mmd.main(target_combobox.get(), URL_space.get())
            mbox.showinfo("Complete", "Complete")
        except:
            mbox.showinfo("Error", "Error occurred")
        return


app = Tk()
app.title('multimedia down')

#창 크기 +붙은 부분은 좌상단 떨어진 위치
app.geometry("300x300+100+100")

#------------------------------------------------------------------------------

lab11=Label(app,
    text="URL",
    width=11,
    height=1,
    font=('맑은 고딕',16,'bold'),
    bg='#2F5597',
    fg='white')
lab11.grid(row=0,column=0,padx=5,pady=10)

URL_space = Entry(font=('맑은 고딕',16,'bold'),bg='white',width=8)
URL_space.grid(row=0,column=1,padx=5,pady=10)

#------------------------------------------------------------------------------

lab21=Label(app,
    text="다운로드 대상",
    width=11,
    height=1,
    font=('맑은 고딕',16,'bold'),
    bg='#2F5597',
    fg='white')

lab21.grid(row=1,column=0,padx=5,pady=10)

target = ["movie", "music", "image"]
target_combobox = ttk.Combobox(app, height = 5, values=target, width=8)
target_combobox.grid(row=1,column=1,padx=5,pady=10)

#------------------------------------------------------------------------------

bt_process = Button(app, text="Process", width=10, command=process)
bt_process.grid(row=3,column=0,padx=5,pady=5)

app.mainloop()