def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("LogView1.ycp")
sleep(3)

assert exists("1314950095045.png")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
sleep(1)
shortcut("o")
assert exists("1314950116383.png")
shortcut("o")
waitVanish("1314950116383.png")