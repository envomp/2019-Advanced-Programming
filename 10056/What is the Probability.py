inputid = int(input())
for i in range(inputid):
    mangijate_arv, toenaosus, mitmes_mangija = map(float, input().split())
    if toenaosus == 0:
        print("0.0000")
    else:
        vastand_toenaosus = 1 - toenaosus
        eelnevad_mangijad = mitmes_mangija - 1
        vahemalt_1_voidab = 1 - vastand_toenaosus ** mangijate_arv
        print("{:.4f}".format(toenaosus * (vastand_toenaosus ** eelnevad_mangijad) / vahemalt_1_voidab))
