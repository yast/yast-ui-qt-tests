def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("MultiProgressMeter2.ycp")
sleep(2)

assert exists("1315230872758.png")
assert exists("1315230884913.png")
shortcut("c")
waitVanish("1315230872758.png")