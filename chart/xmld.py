# import requests, bs4
# from lxml import html
# from urllib.parse import urlencode, quote_plus, unquote
# import chart
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chart.settings')
#
# import django
# django.setup()
#
# from graph.models import Covid19
#
#
# # 1. URL 파라미터 분리하기.
# # Service URL
# xmlUrl = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
#
# My_API_Key = unquote('WRvGBkn9UEtw%2BAsg0tYo210Etxvb1QEcAX%2BwfWvOxVGYJkh1CNZ%2FY4QFa0r7j4bhT4NjPu7z1i1ck8ZgsKMt2Q%3D%3D')
# queryParams = '?' + urlencode(  # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
#     {
#         quote_plus('ServiceKey'): My_API_Key,  # 필수 항목 1 : 서비스키 (본인의 서비스키)
#         quote_plus('startCreateDt'): '20200301',  # 필수 항목 2 : 지역코드 (법정코드목록조회에서 확인)
#         quote_plus('endCreateDt'): '20210407'  # 필수 항목 3 : 계약월
#     }
# )
#
# response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
# xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
#
# rows = xmlobj.findAll('item')
# columns = rows[0].find_all()
#
# rowList = []
# nameList = []
# columnList = []
#
# rowsLen = len(rows)
# for i in range(0, rowsLen):
#     columns = rows[i].find_all()
#
#     columnsLen = len(columns)
#     for j in range(0, columnsLen):
#         # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
#         if i == 0:
#             nameList.append(columns[j].name)
#
#         # 컬럼값은 모든 행의 값을 저장해야한다.
#         eachColumn = columns[j].text
#         columnList.append(eachColumn)
#     rowList.append(columnList)
#     columnList = []  # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)
#
# # for i in rowList:
# #     print(i)

