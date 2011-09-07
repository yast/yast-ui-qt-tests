def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("CheckBox2.ycp")
sleep(1)
assert exists("1314970727345.png")
shortcut("e")
shortcut("p")
shortcut("o")
assert exists("1314970772800.png")
shortcut("o")
waitVanish("1314970772800.png")