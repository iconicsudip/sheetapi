from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
# Create your views here.
@api_view(['GET'])
def sheetdata(request,code):
    sheet_url = "https://docs.google.com/spreadsheets/d/"+code+"/edit#gid=0"
    url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    data = pd.read_csv(url)
    dic = dict()
    for index, row in data.iterrows():
        temp_dic = dict()
        for i in range(len(row)):
            temp_dic[row.keys()[i]] = row[i]
        dic[index] = temp_dic
    count = 0
    final_dic = dict()
    for i in dic:
        flag = False
        for j in dic[i]:
            try:
                img = float(dic[i][j])
                flag = True
            except:
                continue
        if(flag==False):
            print(dic[i])
            final_dic[count] = dic[i]  
            count+=1
    return Response(final_dic)
