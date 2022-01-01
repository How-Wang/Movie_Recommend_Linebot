import message_template
import requests as rs
from transitions.extensions import GraphMachine

import os
import sys
import json

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import FlexSendMessage
import random

from utils import send_text_message

load_dotenv()


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def is_going_to_choose_type(self, event):
        text = event.message.text
        return text == "電影分類推薦"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text == "詳細使用規則"

    def is_going_to_type1(self, event):
        text = event.message.text
        return text == "科幻"

    def is_going_to_type2(self, event):
        text = event.message.text
        return text == "愛情"

    def is_going_to_type3(self, event):
        text = event.message.text
        return text == "劇情"

    def is_going_to_type4(self, event):
        text = event.message.text
        return text == "歷史"

    def is_going_to_cancel(self, event):
        text = event.message.text
        return text == "取消操作"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = message_template.menu
        message_to_reply = FlexSendMessage("主選單", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_choose_type(self, event):
        reply_token = event.reply_token
        message = message_template.choose_type_menu
        message_to_reply = FlexSendMessage("開啟分類選擇選單", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        message = message_template.introduction_message
        message_to_reply = FlexSendMessage("詳細使用規則", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_type1(self, event):
        reply_token = event.reply_token
        message = message_template.show_movie
        with open('movie_dataset.json', newline='', encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        index = random.randint(0, len(data['科幻'])-1)
        message['contents'][0]['hero']['url'] = data['科幻'][index]['picture']
        message['contents'][0]['body']['contents'][0]['text'] = data['科幻'][index]['Chinese_name']
        message['contents'][0]['body']['contents'][1]['text'] = data['科幻'][index]['year']
        message_to_reply = FlexSendMessage("電影資訊", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_type2(self, event):
        reply_token = event.reply_token
        message = message_template.show_movie
        with open('movie_dataset.json', newline='',encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        index = random.randint(0,len(data['愛情'])-1)
        message['contents'][0]['hero']['url'] = data['愛情'][index]['picture']
        message['contents'][0]['body']['contents'][0]['text'] = data['愛情'][index]['Chinese_name']
        message['contents'][0]['body']['contents'][1]['text'] = data['愛情'][index]['year']
        message_to_reply = FlexSendMessage("電影資訊", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_type3(self, event):
        reply_token = event.reply_token
        message = message_template.show_movie
        with open('movie_dataset.json', newline='', encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        index = random.randint(0, len(data['劇情'])-1)
        message['contents'][0]['hero']['url'] = data['劇情'][index]['picture']
        message['contents'][0]['body']['contents'][0]['text'] = data['劇情'][index]['Chinese_name']
        message['contents'][0]['body']['contents'][1]['text'] = data['劇情'][index]['year']
        message_to_reply = FlexSendMessage("電影資訊", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_type4(self, event):
        reply_token = event.reply_token
        message = message_template.show_movie
        with open('movie_dataset.json', newline='',encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        index = random.randint(0,len(data['歷史'])-1)
        message['contents'][0]['hero']['url'] = data['歷史'][index]['picture']
        message['contents'][0]['body']['contents'][0]['text'] = data['歷史'][index]['Chinese_name']
        message['contents'][0]['body']['contents'][1]['text'] = data['歷史'][index]['year']
        message_to_reply = FlexSendMessage("電影資訊", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_cancel(self, event):
        reply_token = event.reply_token
        message = message_template.cancel_menu
        message_to_reply = FlexSendMessage("返回主選單", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
