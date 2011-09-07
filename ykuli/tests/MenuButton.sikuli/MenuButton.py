def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("MenuButton1.ycp")
sleep(1)
assert exists("1314968065050.png")
click("1314968065050.png")
assert exists("1314968183484.png")
shortcut("t")
waitVanish("1314968183484.png")
