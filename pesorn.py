import os,sys
print()
print("\033[1;32m")
def sp(s):
    #####
    for c in s + '\n':
        ##*##
        sys.stdout.write(c)
        sys.stdout.flush()
        os.system ("sleep 0.00000000001")
def sh():
    os.system ("sleep 0.00000000000000000001")
def wait():
    os.system ("read upd")
#Tool Script By Cat Cyber
def key():
    ###
    try:
        #here
        os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        #here
        pass
    print(" [+] Try (mldir) check termux''s files")
    sh()
    shortcutkey = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    print("  preparing Keys...")
    script = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
    print(" [+] opening termux data ...")
    sh()
    script.write(shortcutkey)
    print(" [+] adding keys ")
    print(" \033[0;32m /data/data/com.termux/files/home/.termux/termux.properties")
    script.close()
    #os.system("termux-reload-settings")
    sh()
    print("  [+] Done")
    os.system("termux-reload-settings")
sp("      [+] สคริปนี้สร้างมาให้ เจ้านาย นะครับ ")
print
print(" [KEWY] : เจ้านายโปรดเลือกตัวเลือกการทำงการทำงานฮ้าบ")
print
print(""" 
    [1] แก้ใขแบนเนอะ , ชื่อแบนเนอร์
    [2] ออก 
    """)
txt = input(" [เลือกเลยค้าบ] => ")
if txt == '1':
    sp(" [KEWY] : เดี๋ยวผมจัดการทุจัดการทุกอย่างให้เองนะค้าบ ไว้ใจ KEWY ได้เลย")
    print
    print(" [KEWY] : \033[0mกำลังติดตั้งสิ่งต่างๆที่เจ้านายต้องใช้นะคับ")
    print
    os.system("pkg install nano")
    print
    print
    sp("[KEWY] : เพื่อความสดวกในการใช้งารใช้งานนะคับ ผมขอติดตั้ง ลูกศรให้นะคับ")
    key()
    print("รอเดี๋ยวนะคับ")
    os.system("sleep 1.5")
    os.system("cd && cd .. && cd usr/etc && ls && nano bash.bashrc")