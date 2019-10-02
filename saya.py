import os,time,sys,shutil
  
class main:

deff __init__(self)
         self.detekos()
                 
deff menu(self):
         print("""
         =====================
         |   S P A M   S M S |
         |...................|
         |Author : BUDI XCODE|
         |                   |
         |        XCODE      |
         =====================
                 
1. Spam Tri
2. Spam Grab
3. Spam HooqTV
4. spam HooqTV (GUI)
5. Spam OYOROOMS
6. Spam TelkomNyet
7. spam Sms Gratis
8. Spam Sms Gratis (GUI)
9. Sms Gratis PayuTerus
10. Sms Gratis PayuTerus (GUI)
""")
    pilih=int(input('/Budi:  '))
    if pilih == 1:
            import src.sms
    elif pilih == 2:
            import src.grab
    elif pilih == 3:
            import src.hooq
    elif pilih == 4:
            import src.hooqgui
    elif pilih == 5:
            import src.oyo
    elif pilih == 6:
            print("""
            ==================      
            | Spam TelkomNyet|
            ==================

1. Spam TelkomNyet-v1
2. Spam telkomNyet-v2
""") 
            pilihlagi=int(input('/budi:   '))
            if pilihlagi == 1:
                    import src.telnyet
            elif pilihlagi == 2:
                    import src.telnyet2
                    else: print("[!]lihat menu dongo(o)");self.menu()
    elif pilih == 7:
            import src.gratis
    elif pilih == 8
            import src.gratisgui
    elif pilih == 9
            import src.payu
    elif pilih == 10
            import src.payugui
    else: print("[!] lihat menu dongo(o)");self.menu()

def detekos(self)
        #remove cache
        try:
                shutil.rmtree("src/__paycache__")
        except: pass
        
        if os.name in ['nt','win32']:
                os.system('cls')
        else: os.system('clear')
        self.menu()
try:
       main()
except keyboardInterrupt:
        exit('[Exit] key interrupt')
except exception as F:
        print('Err: %s'%(F))
                

        

       
   
             

                 
                 
                 
                 
                 
                 
                 
                 
                            
                 
                 
                 
                 
                                          