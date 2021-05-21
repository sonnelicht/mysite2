import openpyxl
class Excellib :
    #コンストラクタ
    def __init__(self):
        self.workbook = openpyxl.Workbook()

    # シート名の設定（アクティブシートへの設定）
    def setSheetName(self, sheetname):
        self.worksheet = self.workbook.active
        self.worksheet.title = sheetname

    # セルの値を設定    
    def setCellValue(self, cellpos, value):
        self.worksheet[cellpos] = value

    # ブックの保存
    def save(self, path):
        self.workbook.save(path)
