def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("SelectionBox2.ycp")
sleep(1)
assert exists("1314970376647.png")
click("1314970572369.png")

shortcut("o")
assert exists("1314970416579.png")
shortcut("o")
waitVanish("1314970416579.png")
