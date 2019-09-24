#this code is not working
from urllib import request

goog = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1537747952&period2=1569283952&interval=1d&events=history&crumb=FVWgGX36lrv"

def download_file(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    file = r'goog.csv'
    fw = open(file,'w')
    for line in lines:
        fw.write(line + '\n')
        
    fw.close()
    
    
download_file(goog)
