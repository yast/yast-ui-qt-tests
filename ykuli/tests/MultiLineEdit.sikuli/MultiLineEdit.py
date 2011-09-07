def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("MultiLineEdit1.ycp")
sleep(2)

assert exists("1315230677587.png")
type("line1")
type(Key.ENTER)
type("line2")
assert exists("1315230722027.png")
shortcut("o")
waitVanish("1315230722027.png")