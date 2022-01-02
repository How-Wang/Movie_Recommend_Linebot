menu = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "歡迎來到 尋影｜電影推薦",
                        "weight": "bold",
                        "align": "center",
                        "size": "xl",
                        "wrap": True,
                    }
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "快點擊以下的功能，\n看看有什麼驚奇的新發現吧！",
                        "wrap": True,
                        "size": "lg",
                        "align": "center",
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "電影分類推薦",
                          "text": "電影分類推薦"
                        },
                        "size": "lg",
                        "height": "md",
                        "color": "#FFBF48",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "詳細使用規則",
                            "text": "詳細使用規則"
                        },
                        "size": "lg",
                        "height": "md",
                        "color": "#BF8F36",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "取消操作",
                            "text": "取消操作"
                        },
                        "size": "lg",
                        "height": "md",
                        "color": "#805F24",
                        "style": "primary"
                    }
                ],
                "spacing": "md"
            }
        }
    ]
}

introduction_message = {
    "type": "bubble",
    "size": "giga",
    "header": {
        "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "功能介紹",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "lg",
                        "align": "center"
                    },
                ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "📽　幫助您挑選好電影的工具",
                "wrap": True,
                "align": "center"
            },
            {
                "type": "text",
                "text": "　經典電影　類型推薦",
                "wrap": True,
                "align": "center"
            },
            {
                "type": "text",
                "text": "▶　告訴我你想看「哪種」",
                "wrap": True,
                "align": "center"
            },
            {
                "type": "text",
                "text": "▶　推薦您應該看「哪部」",
                "wrap": True,
                "align": "center"
            },
            {
                "type": "text",
                "text": "🔠　輸入「主選單」開始挑選你想要做什麼",
            },
            {
                "type": "text",
                "text": "🔠　根據選擇，我們告訴你推薦的電影",
            },
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "style": "primary",
                "action": {
                    "type": "message",
                    "label": "點我返回主選單",
                    "text": "主選單"
                }
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}


choose_type_menu = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/YaRH7lS.png",
                "size": "xxl",
                "aspectMode": "fit",
                "aspectRatio": "1:1"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "「科幻電影，\n不只是突破空間與時間的幻想，\n更是一場關於人類自我的探究之旅。」",
                        "wrap": True,
                        "align": "center",
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我想看科幻片！",
                          "text": "科幻"
                        },
                        "height": "md",
                        "color": "#B0A3D4",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/PPPTefX.png",
                "size": "xxl",
                "aspectMode": "fit",
                "aspectRatio": "1:1"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "「因為愛，\n使我們彼此更加完整。」",
                        "wrap": True,
                        "align": "center",
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我想看愛情片！",
                          "text": "愛情"
                        },
                        "height": "md",
                        "color": "#BFACAA",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/NaB9gnp.png",
                "size": "xxl",
                "aspectMode": "fit",
                "aspectRatio": "1:1"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "「生命就是短暫的一回邂逅。」",
                        "wrap": True,
                        "align": "center",
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我想看劇情片！",
                          "text": "劇情"
                        },
                        "height": "md",
                        "color": "#62B6CB",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/FfXhbv9.png",
                "size": "xxl",
                "aspectMode": "fit",
                "aspectRatio": "1:1"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "「歷史的長河流經蕭索歲月，\n唯有靈魂不死。」",
                        "wrap": True,
                        "align": "center",
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "我想看歷史片！",
                          "text": "歷史"
                        },
                        "height": "md",
                        "color": "#3B5249",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        }
    ]
}

show_movie = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "backgroundColor": "#D1D9D9",
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "🎞尋影 向您推薦的電影為",
                        "adjustMode" : "shrink-to-fit"
                    }
                ]
            },
            "hero": {
                "backgroundColor": "#D1D9D9",
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "aspectMode": "fit",
                "size": "full"
            },
            "body": {
                "wrap": True,
                "backgroundColor": "#D1D9D9",
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "電影中文名稱",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "xxl",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "上映年分",
                        "margin": "md",
                        "align": "center",
                        "wrap": True
                    }
                ]
            },
            "footer": {
                "backgroundColor": "#D1D9D9",
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                          "type": "message",
                          "label": "再找找看其他電影",
                          "text": "電影分類推薦"
                        },
                        "height": "md",
                        "color": "#5cd65c",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "好欸！我要去看這部電影了❤︎",
                            "text": "取消操作"
                        },
                        "height": "md",
                        "color": "#00cc66",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },

    ]
}

cancel_menu = {
    "type": "bubble",
    "size": "giga",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "祝你觀影愉快😎",
                "weight": "bold",
                "size": "xl",
                "margin": "xl",
                "align": "center"
            },
            {
                "type": "text",
                "text": "散場後，我們更忙，因為大銀幕投射在心靈的光，才正要開始釋放我們的需索…",
                "size": "md",
                "wrap": True,
                "margin": "lg",
                "align": "center"
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "style": "primary",
                "action": {
                    "type": "message",
                    "label": "返回主選單",
                    "text": "主選單"
                }
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
