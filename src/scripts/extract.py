import httplib
import urllib
import json

from bs4 import BeautifulSoup

'''
@author: anant bhardwaj
@date: Jun 30, 2014

Extract All Pune University Engineering College Details
''' 

def extract():
  f = open('out.txt', 'a')
  conn = httplib.HTTPConnection('www.dtemaharashtra.gov.in')
  conn.request(
      'GET',
      '/approvedinstitues/StaticPages/frmInstituteList.aspx?did=63')  
  list_page = conn.getresponse().read()
  body = BeautifulSoup(list_page)
  table = body.find('table', {'id': 'ctl00_rightContainer_ContentTable1_gvInstituteList'})
  for row in table.findAll('tr'):
    try:
      cells = row.findAll('td')
      sr_no = cells[0].find(text=True)
      institute_code = cells[1].find(text=True)
      college_name = cells[2].find(text=True)
      conn.request(
          'GET',
          '/approvedinstitues/StaticPages/frmInstituteSummary.aspx?InstituteCode=' + institute_code)
      info_page = conn.getresponse().read()
      info_body = BeautifulSoup(info_page)
      name = info_body.find(
          'span', {'id': 'ctl00_rightContainer_ContentBox1_lblPrincipalNameEnglish'}
        ).find(text=True)
      email = info_body.find(
          'span', {'id': 'ctl00_rightContainer_ContentBox1_lblEMailAddress'}
        ).find(text=True)
      item = [sr_no, institute_code, college_name, email, name]
      row_text = '\t'. join(item)
      f.write(row_text+'\n')
    except Exception, e:
      pass
  


def main(): 
  extract()



if __name__ == "__main__":
  main()

