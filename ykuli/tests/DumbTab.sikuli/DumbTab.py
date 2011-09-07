def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("DumbTab1.ycp")


assert exists("1314971515969.png")
shortcut("a")
exists("1314971573752.png")
shortcut("c")
waitVanish("1314971573752.png")
