from excel import Excellib
xl = Excellib()
# シートの設定
xl.setSheetName("yamatani6")
i = 1
while i <=100:
#    print('A' + str(i))
    xl.setCellValue('A' + str(i) , str(i))
#    print('B' + str(i))
    xl.setCellValue('B' + str(i) , str(i).encode('utf-8'))
    i += 1
# 保存
xl.save(r"d:\test6.xlsx")
