# to create user you should use authintication import
from importlib import resources
from re import search
from urllib import request

import requests

from django.contrib.auth import login
# to run the project and route it/redirect for specific path
from django.shortcuts import render, redirect
# get back
from django.urls import reverse
from sqlalchemy import and_, create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func
from django.db import connection

from account.templates.users.form import CustomUserCreationForm
from . import models


def dashboard(request):
    if request.method == "GET":
        if request.GET.get('q') != None:
            return youtube_search(request)

        # youtube_search(request)
        return render(request, "users/dashboard.html")


def youtube_search(request):
    key = 'AIzaSyBbX4KyODgsZIWpKfPUnbMNEe6mbgeB9kk'
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'part': 'snippet',  # key in json file and fixed
        'q': request.GET.get('q'),  # search query
        'key': key,
        'maxResults': 3,
        'type': 'video',

    }
    video_id = []

    r = requests.get(search_url, params=params).json()
    #save_data(r,request)
    print(r)
    # request to get data from youtube

    for item in r['items']:
        video_id.append(item['id']['videoId'])
    # get video id from json file


    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    video_params = {
    'part': 'snippet',
    'key': key,
    'id': ','.join(video_id),
    }
    r=requests.get(video_url, params=video_params).json()
    video=[]
    for item in r['items']:
        vid={
            'description': item['snippet']['description'][:100] + '...',
             'id': item['id'],
            'title': item['snippet']['title'],
         'thumbnail': item['snippet']['thumbnails']['high']['url'],
        }
        video.append(vid)



    print(video)
    # get video data from json file

    # get video title from json file
    return render(request, 'users/dashboard.html', {'video' : video} )#all video data in video list so return it


# def save_data(res,req):
#
#     UID=req.user.id
#     models.User_History.objects.create(
#     #     user_ID=models.User.objects.create(
#     #         ID=5,
#     #         FirstName="John",
#     #         LastName="Doe"
#     #     ),
#
#         user_ID=models.User.objects.get(id=UID),
#     # Search_ID=res['items'][0]['id']['videoId'],
#         Search_query=req.GET.get('q'),
#         search_result=res
#
#
#     )










# search_url = 'https://www.googleapis.com/youtube/v3/search'
#
#
# serach_params = {
#     'part': 'snippet',
#
#     'q': 'python',
#     'key': key,
#     'maxResult': '10',
#     'type': 'video'
# }
#
# video_id = []
#
# r = requests.get(search_url, params=serach_params, ).json()
#
# for vid in r['items']:
#     if vid['id']['kind'] == 'youtube#video':
#         video_id.append(vid['id']['videoId'])
#         print(video_id)
#
# video_params = {
#     'part': 'snippet,contentDetails',
#     'key': key,
#     'id': ','.join(video_id)}
#
#
# r = requests.get(video_url, params=video_params).json()['items']
#
# # print(r.json()['items'][0]['snippet']['title'])  # print the title of the first video
# # print(r.json()['items'][0]['snippet']['description'])  # print the description of the first video
# # print(r.json()['items'][0]['snippet']['thumbnails']['high']['url'])  # print the url of the first video
# # print(r.json()['items'][0]['id']['videoId'])  # print the video id of the first video
#
#
# video1_list=[]
# for val in r:
#     val1={
#             'title': r.json()['items'][0]['snippet']['title'],
#             'description': r.json()['items'][0]['snippet']['description'],
#             'thumbnail': r.json()['items'][0]['snippet']['thumbnails']['high']['url'],
#             'video_id': val['id']
#
#
#     }
# video1_list.append(val1)
#
#
# return ({youtube_search: video1_list}),


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
            ]

    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM account_auth_user ")
    row = dictfetchall(cursor)
    print(row)

    contaxt = {
        "userData": row,
    }

    if request.method == "GET":
        valSearch = request.GET.get('searchVal')
    if valSearch != None:
        return search(request, valSearch, row)

    return render(request, "users/dashboard.html", contaxt)


def search(request, valSearch, con):
    def dictfetchall(cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()
                ]

    cursor = connection.cursor()
    filter = request.GET['filter']
    cursor.execute("SELECT * FROM account_auth_user WHERE " + filter + " LIKE '%" + valSearch + "%'")
    row = dictfetchall(cursor)
    print(row)
    context = {
        "names": row,
        "userData": con
    }
    return render(request, "users/dashboard.html", context)


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect(reverse("dashboard"))

    # def home_dashboard( request):
    #     data = {}
    #     with resources.path("project.data", "db.sqlite3") as sqlite_filepath:
    #         engine = create_engine(f"sqlite:///{sqlite_filepath}")
    #     Session = sessionmaker()
    #     Session.configure(bind=engine)
    #     session = Session()
    #     return render(request, 'users/dashboard.html', session)
