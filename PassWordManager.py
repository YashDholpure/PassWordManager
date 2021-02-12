
import tkinter
import tkinter.messagebox
import tkinter.ttk
Project_Name='PassWordManager'
Width=542
Height=296
my_password='x ae a-12'
# data=[{'Account':'None','Name':'yash','PassWord':'Hail hydra'}]
#values=['None']
def valuemake():
    try:
        file=open('Combooptions.py','x')
        file.write("data=[{'Account':'None','Name':'yash','PassWord':'Hail hydra'}]")
        file.close()
        value_loaded=''
        with open('Combooptions.py') as value_loader:
            for i in value_loader.readline():
                 value_loaded+=i
        value_loader.close()
        return value_loaded
    except:
        value_loaded=''
        with open('Combooptions.py') as value_loader:
            for i in value_loader.readline():
                 value_loaded+=i
        value_loader.close()
        return value_loaded
values=[]
value_loaded=valuemake()
exec(value_loaded)
def datamake():
    try:
        file=open('Create_data_file.py','x')
        file.write("values=['None']")
        file.close()
        data_loaded=''
        with open('Create_data_file.py') as data_loader:
            for i in data_loader.readline():
                 data_loaded+=i
        data_loader.close()
        return data_loaded
    except:
        data_loaded=''
        with open('Create_data_file.py') as data_loader:
            for i in data_loader.readline():
                 data_loaded+=i
        data_loader.close()
        return data_loaded
    
data=[]
data_loaded=datamake()
exec(data_loaded)
class Data_Objects:
        def __init__(self,accountname,name,password):
            self.accountname=accountname
            self.name=name
            self.password=password
        def get_accountname(self):
            return str(self.accountname)
        def get_name(self):
            return str(self.name)
        def get_password(self):
            return str(self.password)
        def save_info(self):
            infokey=["Account","Name","PassWord"]
            account=r'{}'.format(self.get_accountname())
            account=account.capitalize()
            name=r'{}'.format(self.get_name())
            password=r'{}'.format(self.get_password())
            infovalue=[account,name,password]
            information={}
            for key,value in zip(infokey,infovalue):
                    information[key]=value
            maxindex=len(data)
            already=True
            saver=False
            notmatched=True
            for i in range(0,maxindex):
                if  (a:=information['Account']) == (b:=data[i]['Account']):
                    notmatched=False
            if notmatched:
                    data_file=open('Create_data_file.py','w')
                    data_file.truncate(0)
                    data.append(information)
                    data_file.write(f'data={data}')
                    data_file.close()
                    comfile=open('Combooptions.py','w')
                    comfile.truncate(0)
                    values.append(information['Account'])
                    comfile.write(f'values={values}')
                    comfile.close()
                    
                    already=False
                    saver=True

                    
            if  already:  
                tkinter.messagebox.showinfo(f'{Project_Name}',f'{account} Already Exists.')
            
            if saver:
                tkinter.messagebox.showinfo(f'{Project_Name}','Saved ;)')

                
                    

def quit_win1():
    win1.destroy()

def Mp_Sub(event='event'):
      entered_password=E1.get()
      if entered_password==my_password:  
    
        def setapasswd():
            win2.destroy()
            win_setapasswd=tkinter.Tk()
            win_setapasswd.geometry(f"{Width}x{Height}")
            win_setapasswd.title('PassWordManager')
           # win_setapasswd.iconbitmap(r'C:\Users\yash\Downloads\Icons8-Windows-8-Very-Basic-Lock.ico')
            win_setapasswd.configure(bg='black')
            get=tkinter.StringVar()
            def sub():
                B_for_combo.destroy()
                got=combooptions.get()
                maxindex=len(data)
                for i in range(0,maxindex):
                    if got.capitalize()==data[i]['Account']:
                        
                        def saver(event='event'):
                            data[i]['Name']=r'{}'.format(E1.get())
                            data[i]['PassWord']=r'{}'.format(E2.get())
                            with open('Create_data_file.py','w') as file:
                                file.truncate(0)
                                file.write(f'data={data}')
                            with open('Combooptions.py','w') as file:
                                file.truncate(0)
                                file.write(f'values={values}')
                            tkinter.messagebox.showinfo(f'{Project_Name}','Changes Saved.')
                        E1_var=tkinter.StringVar()
                        E2_var=tkinter.StringVar()
                        oldl1=tkinter.Label(win_setapasswd,text=f"Old Name->{data[i]['Name']}").place(x=100,y=110)
                        lab1=tkinter.Label(win_setapasswd,text='Enter New Name-->').place(x=100,y=140)
                        oldl2=tkinter.Label(win_setapasswd,text=f"Old PassWord->{data[i]['PassWord']}").place(x=100,y=170)
                        lab2=tkinter.Label(win_setapasswd,text='Enter New PassWord-->').place(x=100,y=210)
                        E1=tkinter.Entry(win_setapasswd,textvariable=E1_var)
                        E1.place(x=240,y=140)
                        E2=tkinter.Entry(win_setapasswd,textvariable=E2_var)
                        E2.place(x=240,y=210)
                        save=tkinter.Button(win_setapasswd,text='Save',command=saver).place(x=348,y=270)
                        break
            combooptions=tkinter.ttk.Combobox(win_setapasswd,textvariable=get)
            combooptions['values']=values
            combooptions.place(x=220,y=50)
            B_for_combo=tkinter.Button(win_setapasswd,text='Enter',command=sub,font='algerian')
            B_for_combo.place(x=348,y=250)
            my_frame=tkinter.Frame(win_setapasswd,bg='white',height=10,width=10)
            my_frame2=tkinter.Frame(win_setapasswd,bg='white',height=10,width=10)
            my_frame3=tkinter.Frame(win_setapasswd,bg='white',height=10,width=10)
            my_frame4=tkinter.Frame(win_setapasswd,bg='white',height=10,width=10)
            my_frame.place(x=9,y=280)
            my_frame2.place(x=525,y=280)
            my_frame3.place(x=9,y=10)
            my_frame4.place(x=525,y=10)
            
            win_setapasswd.mainloop()

            
            
        def getapasswd():
            win2.destroy()
            win_getapasswd=tkinter.Tk()
            win_getapasswd.geometry(f"{Width}x{Height}")
            win_getapasswd.title('PassWordManager')
            #win_getapasswd.iconbitmap(r'C:\Users\yash\Downloads\Icons8-Windows-8-Very-Basic-Lock.ico')
            win_getapasswd.config(bg='black')
            get=tkinter.StringVar()
            def sub(event='event'):
                got=combooptions.get()
                maxindex=len(data)
                for i in range(0,maxindex):
                    if got.capitalize() == (data[i]['Account']):
                        Name=data[i]['Name']
                        PassWord=data[i]['PassWord']
                        L_name=tkinter.Label(win_getapasswd,text=f"Here's Your Name-->{data[i]['Name']}",font='comicsansms')
                        L_name.place(x=180,y=160)
                        L_pw=tkinter.Label(win_getapasswd,text=f"Here's Your PassWord-->{data[i]['PassWord']}" ,font='comicsansms')
                        L_pw.place(x=180,y=190)
                
                
            combooptions=tkinter.ttk.Combobox(win_getapasswd)
            combooptions['values']=values
            combooptions.place(x=220,y=130)
            B_for_combo=tkinter.Button(win_getapasswd,text='Enter',command=sub,font='algerian').place(x=348,y=230)
            win_getapasswd.bind('<Return>',sub)
            my_frame=tkinter.Frame(win_getapasswd,bg='white',height=10,width=10)
            my_frame2=tkinter.Frame(win_getapasswd,bg='white',height=10,width=10)
            my_frame3=tkinter.Frame(win_getapasswd,bg='white',height=10,width=10)
            my_frame4=tkinter.Frame(win_getapasswd,bg='white',height=10,width=10)
            my_frame.place(x=9,y=280)
            my_frame2.place(x=525,y=280)
            my_frame3.place(x=9,y=10)
            my_frame4.place(x=525,y=10)
            
            
            win_getapasswd.mainloop()
            
            
        def createapasswd():
                                          #creater_func was here
            win2.destroy()
            win_createapasswd=tkinter.Tk()
            win_createapasswd.geometry(f"{Width}x{Height}")
            win_createapasswd.title('PassWordManager')
            #win_createapasswd.iconbitmap(r'C:\Users\yash\Downloads\Icons8-Windows-8-Very-Basic-Lock.ico')
            win_createapasswd.config(bg='black')
        
            E_create_account_var=tkinter.StringVar()
            E_create_name_var=tkinter.StringVar()
            E_create_passwd_var=tkinter.StringVar()
            def creater_var(Event='Event'):
                var1=E_create_account.get()
                var2=E_create_name.get()
                var3=E_create_passwd.get()
        
                    
                if len(var1)>0:
                    if len(var2)>0:
                        obj_name=Data_Objects( var1 , var2 , var3 )
                        obj_name.save_info()
                        
                
                else:
                    tkinter.messagebox.showinfo(f"{Project_Name}",'Please Enter Account And Name')
            win_createapasswd.bind('<Return>',creater_var)
            L_create_account=tkinter.Label(win_createapasswd,text='ACCOUNT',font='algerian').place(x=160,y=100)
            L_create_name=tkinter.Label(win_createapasswd,text='NAME',font='algerian').place(x=160,y=130)
            L_create_passwd=tkinter.Label(win_createapasswd,text='PASSWORD',font='algerian').place(x=160,y=160)
            E_create_account=tkinter.Entry(win_createapasswd,textvariable=E_create_account_var)
            E_create_account.place(x=270,y=100)
            E_create_name=tkinter.Entry(win_createapasswd,textvariable=E_create_name_var)
            E_create_name.place(x=270,y=130)
            E_create_passwd=tkinter.Entry(win_createapasswd,textvariable=E_create_passwd_var)
            E_create_passwd.place(x=270,y=160)
            B_create_submit=tkinter.Button(win_createapasswd,text='Submit',command=creater_var).place(x=348,y=215)
            my_frame=tkinter.Frame(win_createapasswd,bg='white',height=10,width=10)
            my_frame2=tkinter.Frame(win_createapasswd,bg='white',height=10,width=10)
            my_frame3=tkinter.Frame(win_createapasswd,bg='white',height=10,width=10)
            my_frame4=tkinter.Frame(win_createapasswd,bg='white',height=10,width=10)
            my_frame.place(x=9,y=280)
            my_frame2.place(x=525,y=280)
            my_frame3.place(x=9,y=10)
            my_frame4.place(x=525,y=10)

            win_createapasswd.mainloop()
        
        win1.destroy()
        win2=tkinter.Tk()           #win2 start
        win2.title(f'{Project_Name}')
        win2.geometry(f'{Width}x{Height}')
        #win2.iconbitmap(r'C:\users\yash\Downloads\Icons8-Windows-8-Very-Basic-Lock.ico')
        win2.configure(bg='black')
        B_for_SetPassWDs=tkinter.Button(win2,text='Set A PassWord',command=setapasswd,font='algerian').place(x=100,y=120)
        B_for_GetPassWDs=tkinter.Button(win2,text='Get A PassWord',command=getapasswd,font='algerian').place(x=100,y=160)
        B_for_CreatePassWD=tkinter.Button(win2,text='Create A New PassWord',command=createapasswd,font='algerian').place(x=100,y=200)
        my_frame=tkinter.Frame(win2,bg='white',height=10,width=10)
        my_frame2=tkinter.Frame(win2,bg='white',height=10,width=10)
        my_frame3=tkinter.Frame(win2,bg='white',height=10,width=10)
        my_frame4=tkinter.Frame(win2,bg='white',height=10,width=10)
        my_frame.place(x=9,y=280)
        my_frame2.place(x=525,y=280)
        my_frame3.place(x=9,y=10)
        my_frame4.place(x=525,y=10)
        
        win2.mainloop()         #win2 end
      else:
          tkinter.messagebox.showinfo(f'{Project_Name}',f'Wrong PassWord {entered_password}.')

    
def notme(event='event'):
    entered_password=E1.get()
    tkinter.messagebox.showinfo(f'{Project_Name}',f'Wrong PassWord {entered_password}.')
win1=tkinter.Tk()                       #win1 start
#win1.iconbitmap(r'/user/yash/PythonProjects/Icons8-Ios7-Very-Basic-Lock-Filled.ico')
win1.title(f'{Project_Name}')
win1.config(bg='black',relief='raised')
win1.geometry(f'{Width}x{Height}')
E1_var=tkinter.StringVar()
E1=tkinter.Entry(win1,textvariable=E1_var) 
E1.place(x=300,y=120)
L1=tkinter.Label(win1,text='Enter The MasterPassWord-->',font='algerian',bg='black',fg='white',).place(x=40,y=120)
B_for_MPsub=tkinter.Button(win1,text='Enter',command=Mp_Sub,width=6,height= -3).place(x=445,y=120)
#win1.bind('<Return>',notme)
B_for_quit=tkinter.Button(win1,text='Quit',width=6,command=quit_win1).place(x=445,y=150)
#my_frame=tkinter.Frame(win1,bg='white',height=10,width=10)
#my_frame2=tkinter.Frame(win1,bg='white',height=10,width=10)
#my_frame3=tkinter.Frame(win1,bg='white',height=10,width=10)
#my_frame4=tkinter.Frame(win1,bg='white',height=10,width=10)
#my_frame.place(x=9,y=280)
#my_frame2.place(x=525,y=280)
#my_frame3.place(x=9,y=10)
#my_frame4.place(x=525,y=10)
#my_frame.bind('<Button-3>',MP_Sub)




win1.mainloop()             #win1 end

