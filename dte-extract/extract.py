import codecs
import unicodecsv as csv
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
  f = open('out.csv', 'w+')
  writer = csv.writer(f, encoding='utf-8')
  conn = httplib.HTTPConnection('www.dtemaharashtra.gov.in')
  conn.request(
      'GET',
      '/approvedinstitues/StaticPages/frmInstituteList.aspx?did=63')  
  list_page = conn.getresponse().read()
  body = BeautifulSoup(list_page)
  table = body.find('table', {'id': 'ctl00_rightContainer_ContentTable1_gvInstituteList'})
  for row in table.findAll('tr'):
    try:
      conn = httplib.HTTPConnection('www.dtemaharashtra.gov.in')
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
      
      if not name:
        name = ''

      email = info_body.find(
          'span', {'id': 'ctl00_rightContainer_ContentBox1_lblEMailAddress'}
        ).find(text=True)
      
      if not email:
        email = ''

      status1 = info_body.find(
          'span', {'id': 'ctl00_rightContainer_ContentBox1_lblStatus1'}
        ).find(text=True)

      if not status1:
        status1 = ''

      status2 = info_body.find(
          'span', {'id': 'ctl00_rightContainer_ContentBox1_lblStatus2'}
        ).find(text=True)

      if not status2:
        status2 = ''

      status3 = info_body.find(
          'span', {'id': 'ctl00_rightContainer_ContentBox1_lblStatus3'}
        ).find(text=True)

      if not status3:
        status3 = ''

      row = [sr_no, institute_code, college_name, email, name, status1, status2, status3]
      writer.writerow(row)
      row_text = '\t'.join(row)
      print row_text
    except Exception, e:
      print e
      pass

def main(): 
  extract()


if __name__ == "__main__":
  main()

