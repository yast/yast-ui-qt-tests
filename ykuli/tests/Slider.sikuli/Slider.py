def waitnclick(img) :
        wait(img, 5)
        click(img)
        sleep(1) # time to let img go away

def shortcut(key) :
        type(key, KEY_ALT)

def ycptest(module) :
        type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")

ycptest("Slider1.ycp")
sleep(5)
assert exists("1314885065416.png")
shortcut("p")
type(Key.BACKSPACE)
type(Key.BACKSPACE)
type("0")
sleep(1)
assert exists("1314885179888.png")
type(Key.BACKSPACE)
type(Key.BACKSPACE)
type("100")
sleep(1)
assert exists("1314885208426.png")

shortcut("o")
waitVanish("1314885208426.png")