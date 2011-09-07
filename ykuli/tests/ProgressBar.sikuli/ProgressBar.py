def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("ProgressBar1.ycp")
sleep(1)
assert exists("1314968483781.png")
shortcut("n")
sleep(1)
shortcut("n")
sleep(1)
shortcut("n")
sleep(1)
shortcut("n")
sleep(1)
shortcut("n")
sleep(1)
assert exists("1314968536005.png")
shortcut("c")
waitVanish("1314968536005.png")