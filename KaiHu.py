import json
import wx
import requests
import threading
import pyperclip

QQAPI = ""#在这里填你查QQ数据的API
PhoneAPI = ""#在这里填你反查手机数据的API
WeiBoAPI = ""#在这里填你查微博数据的API
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(590, 600))

        self.panel = wx.Panel(self)

        self.qq_label = wx.StaticText(self.panel,label="QQ查绑 ""请输入要查询的QQ:")
        self.qq_input = wx.TextCtrl(self.panel)
        self.qq_query_button = wx.Button(self.panel, label="查询QQ号码")
        self.qq_result = wx.StaticText(self.panel, label="", style=wx.ALIGN_LEFT)

        self.phone_label = wx.StaticText(self.panel, label="手机号反查 ""请输入手机号:")
        self.phone_input = wx.TextCtrl(self.panel)
        self.phone_query_button = wx.Button(self.panel, label="查询手机号")
        self.phone_result = wx.StaticText(self.panel, label="", style=wx.ALIGN_LEFT)
        self.weibo = wx.StaticText(self.panel, label="微博查绑 ""请输入微博ID")
        self.weibo_input = wx.TextCtrl(self.panel)
        self.weibo_button = wx.Button(self.panel, label="查询手机号")
        self.weibo_result = wx.StaticText(self.panel, label="", style=wx.ALIGN_LEFT)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.qq_label, 0, wx.ALL, 5)
        sizer.Add(self.qq_input, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.qq_query_button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.qq_result, 0, wx.ALL | wx.DOWN, 30)

        sizer.Add(self.phone_label, 0, wx.ALL, 5)
        sizer.Add(self.phone_input, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.phone_query_button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.phone_result, 0, wx.ALL | wx.DOWN, 30)

        sizer.Add(self.weibo, 0, wx.ALL, 5)
        sizer.Add(self.weibo_input, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.weibo_button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.weibo_result, 0, wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.qq_query_button.Bind(wx.EVT_BUTTON, self.on_qq_query)
        self.phone_query_button.Bind(wx.EVT_BUTTON, self.on_phone_query)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.weibo_button.Bind(wx.EVT_BUTTON,self.WeiboSearch)
        self.last_size = None
    def OnEraseBack(self, event):
        dc = event.GetDC()
        width, height = self.GetClientSize()
        bg_image = wx.Image("BG.png", wx.BITMAP_TYPE_ANY)
        bg_image = bg_image.Scale(width, height, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        dc.DrawBitmap(bg_image, 0, 0)
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
    def OnResize(self, event):
        new_size = self.GetClientSize()
        if new_size != self.last_size:
            self.last_size = new_size
            wx.CallLater(200,self.Refresh)
            event.Skip()

    def on_qq_query(self, event):
        threading.Thread(target=self.qq_query_thread).start()

    def qq_query_thread(self):
        QQ = self.qq_input.GetValue()
        if QQ == "":
            self.qq_result.SetLabel("未检测到用户输入")
        else:
            length = len(self.qq_input.GetValue())
            if length > 10:
                self.qq_result.SetLabel("你输入的数据太长了，不是QQ号")
            else:
                self.qq_result.SetLabel("查询中……")
                qq_data = requests.get(QQAPI + QQ).text
                if "查询成功" in qq_data:
                    qq_data = json.loads(qq_data)
                    qq_info = "qq: {}\n的电话号码: {} {}".format(QQ, qq_data["phone"], qq_data["phonediqu"]+"\n内容已复制")
                    pyperclip.copy(qq_info.replace("\n内容已复制", ""))
                    self.qq_result.SetLabel(qq_info)
                elif "没有找到" in qq_data:
                    self.qq_result.SetLabel("qq: {} 没有找到电话号码".format(QQ))

    def on_phone_query(self, event):
        threading.Thread(target=self.phone_query_thread).start()
    def phone_query_thread(self):
        phone = self.phone_input.GetValue()
        if phone == "":
            self.phone_result.SetLabel("未检测到用户输入")
        else:
            length = len(self.phone_input.GetValue())
            if length > 11:
                self.phone_result.SetLabel("你输入的数据太长了，不是手机号")
            else:
                self.phone_result.SetLabel("查询中……")
                phone_data = requests.get(PhoneAPI + phone).text
                if "查询成功" in phone_data:
                    phone_data = json.loads(phone_data)
                    qq_info = "电话: {}\n对应qq号码是: {}".format(phone, phone_data["qq"] +"\n内容已复制")
                    pyperclip.copy(qq_info.replace("\n内容已复制", ""))
                    self.phone_result.SetLabel(qq_info)
                elif "没有找到" in phone_data:
                    self.phone_result.SetLabel("电话: {} 没有找到qq号码".format(phone))
    def WeiboSearch(self, event):
        threading.Thread(target=self.weibo_query_thread).start()
    def weibo_query_thread(self):
        ID = self.weibo_input.GetValue()
        if ID == "":
            self.weibo_result.SetLabel("未检测到用户输入")
        else:
            self.weibo_result.SetLabel("查询中……")
            weibo_data = requests.get(WeiBoAPI+ID).text
            if "查询成功" in weibo_data:
                weibo_data = json.loads(weibo_data)
                self.weibo_result.SetLabel("微博ID: {} 的电话号码是：{} {} 内容已复制".format(ID,weibo_data["phone"],weibo_data["phonediqu"]))
                fuzhi = "微博ID: {} 的电话号码是：{} {}".format(ID,weibo_data["phone"],weibo_data["phonediqu"])
                pyperclip.copy(fuzhi)
            elif "没有找到" in weibo_data:
                self.weibo_result.SetLabel("微博ID: {} 没有找到电话号码".format(ID))

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "隐私查询软件界面模版 "+"本软件需要联网"+" 请勿用于非法用途！后果自负！")
    frame.Show()
    app.MainLoop()