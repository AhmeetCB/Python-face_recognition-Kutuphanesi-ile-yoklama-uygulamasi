import PIL,os
import face_recognition
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageDraw
from tkinter.filedialog import askopenfilename
import os
import pandas as pd
import numpy as np
import locale

class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   
             
        self.master = master
        self.init_window()
        self.ogrenci_foto_path=""
        self.yoklama_foto_path=""

    def init_window(self):

        self.master.title("ÖĞRENCİ YOKLAMA")
        self.labell_bos=Label(self.master, text="")
        self.labell_bos.grid(row=0,column=0)
        self.labell_bos=Label(self.master,height=3, text="")
        self.labell_bos.grid(row=0,column=1)
        self.butonn=Button(self.master, text = 'ÖĞRENCİ EKLE', width = 25,height=3, command=self.ogrenciler)
        self.butonn.grid(row=1,column=1)
        self.label1_bos=Label(self.master,width = 29, text="")
        self.label1_bos.grid(row=2,column=0)
        self.butonn1=Button(self.master, text = 'DERS SİL', width = 25,height=3,command=self.ogrenci_sil) 
        self.butonn1.grid(row=2,column=1)
        self.butonn=Button(self.master, text = 'DERS OLUŞTUR', width = 25,height=3, command=self.ders_ekle)
        self.butonn.grid(row=3,column=1)
        self.btn_yoklama=Button(self.master, text = 'YOKLAMA AL', width = 25,height=3, command=self.yoklama_al)
        self.btn_yoklama.grid(row=4,column=1)
    def ogrenci_sil(self):
        pencere=Tk()
        pencere.title('DERS SİL')
        pencere.geometry('250x250')
        la=Label(pencere, text="")
        la.grid(row=0,column=0)
        
        self.label_ogr_sil=Label(pencere, text="Dersi/Dersleri Seçin:")
        self.label_ogr_sil.grid(row=1,column=0)
        self.Lb2 = Listbox(pencere,selectmode='multiple', exportselection=0)
        self.Lb2.grid(row=1,column=1)
        self.liste1=[]
        dosya=open('dersadlari.txt','r')
        veri=dosya.read()
        veriler=veri.split('\n')
        for i in range(len(veriler)):
            if(veriler[i]!=''):
                self.liste1.append(veriler[i].split(','))
        for i in range(len(self.liste1)):
            self.Lb2.insert(i,self.liste1[i][0])
        dosya.close()
        self.btnSil=Button(pencere,text='SİL',command=self.yeni_ders_sil)
        self.btnSil.grid(row=2,column=1)
        pencere.mainloop()

    def yeni_ders_sil(self):
        if(self.Lb2.curselection()==()):
            messagebox.showinfo('Hata','Ders Seçilmedi')
        else:
            secilen=self.Lb2.curselection()
            dosya=open('dersadlari.txt','r')
            veri=dosya.read()
            veriler=veri.split('\n')
            
            dosya.close()
            yeni_dosya=open('yedek.txt','w')
            j=0
            for i in range(len(veriler)):
                
                if i!=secilen[j]:
                    yeni_dosya.write(veriler[i]+'\n')  #dzelt bunu 
                else:
                    j+=1
                    if j==len(secilen):
                        j-=1
            yeni_dosya.close()
            os.remove('dersadlari.txt')
            os.rename('yedek.txt','dersadlari.txt')
            for i in range(len(secilen)):
                os.remove("dersler/"+veriler[secilen[i]]+".txt")
                os.remove("dersler/"+veriler[secilen[i]]+"_Yoklama.xlsx")
            messagebox.showinfo('Durum','SİLİNDİ')
    def yeni_ogrenci_sil(self):
        secilenler=self.Lb2.curselection()
        dosya=open('kayıtlar.txt','r')
        veri=dosya.read()
        veriler=veri.split('\n')
        
        dosya.close()
        yeni_dosya=open('yedek.txt','w')
        j=0
        for i in range(len(veriler)):
            
            if i!=secilenler[j]:
                yeni_dosya.write(veriler[i]+'\n')  #dzelt bunu 
            else:
                j+=1
                if j==len(secilenler):
                    j-=1
        yeni_dosya.close()

        os.remove('kayıtlar.txt')
        os.rename('yedek.txt','kayıtlar.txt')
        messagebox.showinfo('Durum','SİLİNDİ')

    def yoklama_al(self):
        pencere=Tk()
        pencere.title('YOKLAMA')
        pencere.geometry("250x250")
        self.la=Label(pencere, text="")
        self.la.grid(row=0,column=0)
        self.label_foto_adress=Label(pencere, text="Fotoğrafı Seçin:")
        self.label_foto_adress.grid(row=1,column=1)
        self.foto_button=Button(pencere, text = 'resim seç', width = 6, command=self.browse_yoklama_file)
        self.foto_button.grid(row=1,column=2)
        self.label_drsadi=Label(pencere, text="Ders Adı:")
        self.label_drsadi.grid(row=2,column=1)
        secenekler=[]
        dosya=open('dersadlari.txt','r')
        veri=dosya.read()
        veriler=veri.split("\n")
        for i in range(len(veriler)):
            if(veriler[i]!=""):
                secenekler.append(veriler[i])
        self.drs_adi_al=StringVar(pencere)
        self.drs_adi_al.set(secenekler[0])
        self.w = OptionMenu(pencere, self.drs_adi_al, *secenekler)
        self.w.grid(row=2,column=2)
        self.label_drsgun=Label(pencere, text="Yoklama Alınacak Tarih:")
        self.label_drsgun.grid(row=3,column=1)
        self.drsgun=Entry(pencere)
        self.drsgun.grid(row=3,column=2)     
        self.btn_yoklama_al=Button(pencere, text = 'Yoklama Al', width = 15, command=self.yoklama)
        self.btn_yoklama_al.grid(row=4,column=1)
        pencere.mainloop()
    def browse_yoklama_file(self):

        ftypes = [("Fotoğraf Dosyaları", "*.png; *.jpg; *.jpeg; *.bmp")]
        ttl  = "Title"
        dir1 = 'C:\\'
        self.yoklama_foto_path=askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)

    def yoklama(self):
        if(self.drsgun.get()==""):
            messagebox.showinfo('Hata','Tarih Girilmedi')
        elif(self.yoklama_foto_path==""):
            messagebox.showinfo('Hata','Fotoğraf Seçilmedi')
        else:
            known_face_encodings=[]
            known_face_names=[]
            dosya=open("./dersler/"+self.drs_adi_al.get()+".txt","r", encoding='utf-8')
            veri=dosya.read()
            veriler=veri.split("\n")
            for i in range(len(veriler)):
                if(veriler[i]!=""):
                    aa=veriler[i].split(",")
                image_of_line=face_recognition.load_image_file(aa[1])
                line_face_encoding=face_recognition.face_encodings(image_of_line)[0]
                known_face_encodings.append(line_face_encoding)
                known_face_names.append(aa[0])
            dosya.close()

            test_img=face_recognition.load_image_file(self.yoklama_foto_path) #kullanıcıdn al
            face_locations=face_recognition.face_locations(test_img)
            face_encodings=face_recognition.face_encodings(test_img, face_locations)
            piL_image=Image.fromarray(test_img)
            draw=ImageDraw.Draw(piL_image)
            excel_file = './dersler/'+self.drs_adi_al.get()+'_Yoklama.xlsx'
            deneme = pd.read_excel(excel_file)
            aa=[]
            for(top,right,bottom,left), face_encoding in zip(face_locations,face_encodings):
                matches=face_recognition.compare_faces(known_face_encodings,face_encoding, tolerance=0.55)

                name="Unknown person"

                if True in matches:
                    first_match_index=matches.index(True)
                    name=known_face_names[first_match_index]
                if (name!="Unknown person") : 
                    aa.append(name)
                #
            aa = list(set(aa))
            #aa dizisindekileri dersi alanlarla karşılaştır alan kişinin yüzü varsa 1 yoksa 0 yazdır sonra excel kodlarını al
            dosya=open("./dersler/"+self.drs_adi_al.get()+".txt","r", encoding='utf-8')
            veri=dosya.read()
            veriler=veri.split('\n')
            yoklama=[]
            varmi=0
            for i in range(len(veriler)):
                varmi=0
                if(veriler[i]!=""):
                    bolunmus=veriler[i].split(",")
                for j in range(len(aa)):
                    if(bolunmus[0]==aa[j]):
                        varmi=1
                if(veriler[i]!=""):
                    yoklama.append(varmi)
            dosya.close()
            deneme[self.drsgun.get()]=yoklama
            deneme.to_excel(excel_file, 'Sheet1', index=False)

            messagebox.showinfo("Durum","Yoklama Alındı")
            #

    def ders_ekle(self):
        pencere=Tk()
        pencere.geometry("300x300")
        pencere.title("DERS OLUŞTUR")
        self.label_bos=Label(pencere, text="")
        self.label_bos.grid(row=1,column=0)

        self.label_drs=Label(pencere, text="Ders Adı:")
        self.label_drs.grid(row=2,column=0)
        self.drs_adi=Entry(pencere)
        self.drs_adi.grid(row=2,column=1)

        self.label_bos1=Label(pencere, text="")
        self.label_bos1.grid(row=3,column=0)
        self.Lb1 = Listbox(pencere)

        self.label_ogr_sec=Label(pencere, text="Öğrencileri Secin:")
        self.label_ogr_sec.grid(row=4,column=0)
        self.Lb1 = Listbox(pencere,selectmode='multiple',exportselection=0)
        self.liste=[]
        dosya=open('kayıtlar.txt','r', encoding='utf-8')
        veri=dosya.read()
        veriler=veri.split('\n')
        for i in range(len(veriler)):
            if(veriler[i]!=''):
                self.liste.append(veriler[i].split(','))
        for i in range(len(self.liste)):
            self.Lb1.insert(i,self.liste[i][0])
        self.Lb1.grid(row=4,column=1)

        self.buton_drs=Button(pencere, text = 'Oluştur', width = 6, command=self.ders_olustur)
        self.buton_drs.grid(row=6,column=1)
        pencere.mainloop()
    def ders_olustur(self):
        if(self.drs_adi.get()==""):
            messagebox.showinfo("Hata","Ders Adı Girilmedi")
        elif(self.Lb1.curselection()==()):
            messagebox.showinfo("Hata","Öğrenci Seçilmedi")
        else:   
            a=self.Lb1.curselection()
            deneme=pd.DataFrame(data=None)
            ogrno=[]
            ogradi=[]
            
            dosya1=open('./dersler/'+self.drs_adi.get()+'.txt','w', encoding='utf-8')
            for i in range(len(a)):
                j=0
                while(j<2):
                    dosya1.write(self.liste[a[i]][j]+',')
                    j+=1
                ogrno.append(self.liste[a[i]][2])
                ogradi.append(self.liste[a[i]][0])
                dosya1.write(self.liste[a[i]][2]+'\n')
            deneme['Öğrenci No']=ogrno
            deneme['Öğrenci Adı']=ogradi
            deneme.to_excel('./dersler/'+self.drs_adi.get()+'_Yoklama.xlsx', 'Sheet1', index=False)
            dosya1.close()
            dosya2=open('dersadlari.txt','a', encoding='utf-8')
            dosya2.write(self.drs_adi.get()+'\n')
            dosya2.close()

            messagebox.showinfo("Durum","OLUŞTURULDU")
    def ogrenciler(self):
        pencere=Tk()
        pencere.title("ÖĞRENCİ EKLE")
        pencere.geometry("250x170")

        self.label1=Label(pencere, text="")
        self.label1.grid(row=1,column=0)

        self.label3=Label(pencere, text="Öğrenci Adı Soyadı:")
        self.label3.grid(row=3,column=0)
 
        self.ogr_adi=Entry(pencere)
        self.ogr_adi.grid(row=3,column=1)        
        
        self.label4=Label(pencere, text="Öğrenci No:")
        self.label4.grid(row=4,column=0)
        
        self.ogr_no=Entry(pencere)
        self.ogr_no.grid(row=4,column=1)
        
        self.label5=Label(pencere, text="Öğrenci Resmi:")
        self.label5.grid(row=5,column=0)
        self.buton1=Button(pencere, text = 'resim seç', width = 6, command=self.browse_file)
        self.buton1.grid(row=5,column=1)
        self.buton2=Button(pencere, text = 'Kaydet', width = 6, command=self.kaydet)
        self.buton2.grid(row=6,column=1)
        pencere.mainloop()


    def browse_file(self):

        ftypes = [("Fotoğraf Dosyaları", "*.png; *.jpg; *.jpeg; *.bmp")]
        ttl  = "Title"
        dir1 = 'C:\\'
        self.ogrenci_foto_path=askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
        
    def kaydet(self):
        if(self.ogr_adi.get()==""):
            messagebox.showinfo("Hata","İsim Boş Olamaz")
        elif(self.ogr_no.get()==""):
            messagebox.showinfo("Hata","Numara Boş Olamaz")
        elif(self.ogrenci_foto_path==""):
            messagebox.showinfo("Hata","Fotoğraf Seçilmedi")
        else:    
            hedef_yukseklik = 480
            resim = Image.open(self.ogrenci_foto_path)
            yeniboyut_orani = (hedef_yukseklik / float(resim.size[1]))
            hedef_genislik = int((float(resim.size[0])*float(yeniboyut_orani)))
            resim=resim.resize((hedef_genislik,hedef_yukseklik),PIL.Image.ANTIALIAS)
            resim.save('./images/'+self.ogr_no.get()+'.jpg')
            path='./images/'+self.ogr_no.get()+'.jpg'

            image_of_ahmet=face_recognition.load_image_file(path)
            ahmet_face_locations=face_recognition.face_locations(image_of_ahmet)

            for face_locations in ahmet_face_locations:
                top,right,bottom,left =face_locations

                face_image=image_of_ahmet[top:bottom, left:right]
                pil_image=Image.fromarray(face_image)

                os.remove(path)
                pil_image.save('./images/'+self.ogr_no.get()+'-1.jpg')

            dosya=open("kayıtlar.txt","a", encoding='utf-8')
            path='./images/'+self.ogr_no.get()+'-1.jpg'
            ogrenciiadi=str(self.ogr_adi.get()).lower()
            aa=ogrenciiadi+","+path+","+self.ogr_no.get()+"\n"
            dosya.write(aa)
            dosya.close()
            messagebox.showinfo("Durum","EKLENDİ")

        

root = Tk()
root.geometry("600x450")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  