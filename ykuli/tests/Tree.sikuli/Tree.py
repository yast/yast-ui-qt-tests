def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("Tree1.ycp")
sleep(3)
type(Key.RIGHT)
type(Key.RIGHT)
assert exists("1314094685564.png")
shortcut("u")
sleep(1)
type(Key.RIGHT)
assert exists("1314094786802.png")
shortcut("l")
shortcut("o")
assert exists("1314094841547.png")
shortcut("o")
waitVanish("1314094841547.png")
 
