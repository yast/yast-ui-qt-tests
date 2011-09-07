def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("ComboBox1.ycp")

assert exists("1314971020794.png")

click("1314971036515.png")
type (Key.DOWN)
type (Key.DOWN)
type (Key.ENTER)
assert exists("1314971105935.png")
shortcut("o")
waitVanish("1314971105935.png")

