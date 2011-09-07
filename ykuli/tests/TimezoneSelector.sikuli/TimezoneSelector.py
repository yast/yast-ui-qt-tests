def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("TimezoneSelector.ycp")
sleep(3)
assert exists("1314886745438.png")
click("1314886835076.png")

assert exists("1314886858433.png")

shortcut("c")

waitVanish("1314886858433.png")