def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("InputField1.ycp")
sleep(1)




assert exists("1314951895142.png")
type ("test")
assert exists("1314951933759.png")
shortcut("o")
waitVanish("1314951933759.png")