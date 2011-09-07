
def waitnclick(img) :
	wait(img, 5)
	click(img)
	sleep(1) # time to let img go away

def shortcut(key) :
	type(key, KEY_ALT)		

def ycptest(module) :
	type(" /usr/lib/YaST2/bin/y2base /usr/share/doc/packages/yast2-ycp-ui-bindings/examples/"+ module + " qt\n")	

ycptest("PushButton1.ycp")
wait("1314085065432.png")
shortcut("o")
waitVanish("1314083924798.png")

ycptest("PushButton1.ycp")
waitnclick("1314085065432.png")
waitVanish("1314083924798.png")


