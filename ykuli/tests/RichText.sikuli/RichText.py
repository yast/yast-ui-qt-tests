def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("RichText-hyperlinks.ycp")
sleep(10)
wait("1314884202346.png")
click("1314884403570.png")
wait("1314884423338.png")
shortcut("c")
waitVanish("1314884202346.png")
