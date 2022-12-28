import openpyxl
import requests
from bs4 import BeautifulSoup


book = openpyxl.load_workbook('Ryutarou01.xlsx')
sheet = book.active

url = "https://atinn.jp/area/tokai-tokai"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

start_row = 1



for prohis_box in soup.find_all(class_="prohis_box"):

	sel1 = "A"+str(start_row)
	sel2 = "B"+str(start_row)
	sel3 = "C"+str(start_row)
	sel4 = "D"+str(start_row)
	

	titles = prohis_box.find(class_="prohis_boxttl").get_text()
	sheet[sel1].value = titles

	prices = prohis_box.find(class_="current_price price_day2").get_text()
	sheet[sel2].value = prices

	flames = prohis_box.find(class_="prohis_boxintb2_td2a").get_text()
	sheet[sel3].value = flames

	station = prohis_box.find(class_="prohis_boxtopright pro_tbl").get_text()
	sheet[sel4].value = station
	start_row += 1
# for start_row in range(1,10):
	

book.save('Ryutarou01.xlsx')
book.close

#----------------------------------------------------------------------------------------ここまでは正常

#for 変数 in soup.find_all(取得したいデータが入っている全範囲):
#find_all / find の違い⇒find()メソッドは最初の要素のみを取り出し、find_all()メソッドは全ての要素を取り出す。


#Q1.取得したデータをExcelに繰り返して反映する手段
#An.

#sel1～sel4の定義をfor文の外にあると+1しても更新されない。for文の中に入れる事で解決。
#----------------------------------------------------------------------------------------





	
