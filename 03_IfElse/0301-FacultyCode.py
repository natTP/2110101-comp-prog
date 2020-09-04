n = input()
ok = ["01","02","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","53","55","58"]
isOK = False
for i in ok:
    if n == i:
        isOK = True
if isOK:
    print("OK")
else:
    print("Error")

#actually, you could
#if n in ok: print OK
# else: print Error