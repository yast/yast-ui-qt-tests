def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("ContextMenu.ycp")
sleep(3)

assert exists("1314957900044.png")
rightClick("1314957924246.png")
assert exists("1314957984801.png")
type (Key.ESC)
sleep(1)
shortcut("o")
waitVanish("1314958059304.png")


