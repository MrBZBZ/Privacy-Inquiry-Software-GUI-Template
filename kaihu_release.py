import json 
import wx 
import requests 
import threading 
import pyperclip 
class MyFrame (wx .Frame ):
    def __init__ (O0OO00O0O00O0OO0O ,O00OOOOO0O00O0000 ,O00OO00O00OO0OOO0 ):
        super (MyFrame ,O0OO00O0O00O0OO0O ).__init__ (O00OOOOO0O00O0000 ,title =O00OO00O00OO0OOO0 ,size =(590 ,600 ))
        O0OO00O0O00O0OO0O .panel =wx .Panel (O0OO00O0O00O0OO0O )
        O0OO00O0O00O0OO0O .qq_label =wx .StaticText (O0OO00O0O00O0OO0O .panel ,label ="QQ查绑 " "请输入要查询的QQ:")
        O0OO00O0O00O0OO0O .qq_input =wx .TextCtrl (O0OO00O0O00O0OO0O .panel )
        O0OO00O0O00O0OO0O .qq_query_button =wx .Button (O0OO00O0O00O0OO0O .panel ,label ="查询QQ号码")
        O0OO00O0O00O0OO0O .qq_result =wx .StaticText (O0OO00O0O00O0OO0O .panel ,label ="",style =wx .ALIGN_LEFT )
        O0OO00O0O00O0OO0O .phone_label =wx .StaticText (O0OO00O0O00O0OO0O .panel ,label ="手机号反查 " "请输入手机号:")
        O0OO00O0O00O0OO0O .phone_input =wx .TextCtrl (O0OO00O0O00O0OO0O .panel )
        O0OO00O0O00O0OO0O .phone_query_button =wx .Button (O0OO00O0O00O0OO0O .panel ,label ="查询手机号")
        O0OO00O0O00O0OO0O .phone_result =wx .StaticText (O0OO00O0O00O0OO0O .panel ,label ="",style =wx .ALIGN_LEFT )
        O0OO00O0O00O0OO0O .weibo =wx .StaticText (O0OO00O0O00O0OO0O .panel ,label ="微博查绑 " "请输入微博ID")
        O0OO00O0O00O0OO0O .weibo_input =wx .TextCtrl (O0OO00O0O00O0OO0O .panel )
        O0OO00O0O00O0OO0O .weibo_button =wx .Button (O0OO00O0O00O0OO0O .panel ,label ="查询手机号")
        O0OO00O0O00O0OO0O .weibo_result =wx .StaticText (O0OO00O0O00O0OO0O .panel ,label ="",style =wx .ALIGN_LEFT )
        OO0O000OOO0OOO0O0 =wx .BoxSizer (wx .VERTICAL )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .qq_label ,0 ,wx .ALL ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .qq_input ,0 ,wx .ALL |wx .EXPAND ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .qq_query_button ,0 ,wx .ALL |wx .CENTER ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .qq_result ,0 ,wx .ALL |wx .DOWN ,30 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .phone_label ,0 ,wx .ALL ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .phone_input ,0 ,wx .ALL |wx .EXPAND ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .phone_query_button ,0 ,wx .ALL |wx .CENTER ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .phone_result ,0 ,wx .ALL |wx .DOWN ,30 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .weibo ,0 ,wx .ALL ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .weibo_input ,0 ,wx .ALL |wx .EXPAND ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .weibo_button ,0 ,wx .ALL |wx .CENTER ,5 )
        OO0O000OOO0OOO0O0 .Add (O0OO00O0O00O0OO0O .weibo_result ,0 ,wx .ALL ,5 )
        O0OO00O0O00O0OO0O .panel .SetSizer (OO0O000OOO0OOO0O0 )
        O0OO00O0O00O0OO0O .qq_query_button .Bind (wx .EVT_BUTTON ,O0OO00O0O00O0OO0O .on_qq_query )
        O0OO00O0O00O0OO0O .phone_query_button .Bind (wx .EVT_BUTTON ,O0OO00O0O00O0OO0O .on_phone_query )
        O0OO00O0O00O0OO0O .panel .Bind (wx .EVT_ERASE_BACKGROUND ,O0OO00O0O00O0OO0O .OnEraseBack )
        O0OO00O0O00O0OO0O .Bind (wx .EVT_SIZE ,O0OO00O0O00O0OO0O .OnResize )
        O0OO00O0O00O0OO0O .weibo_button .Bind (wx .EVT_BUTTON ,O0OO00O0O00O0OO0O .WeiboSearch )
        O0OO00O0O00O0OO0O .last_size =None 
    def OnEraseBack (OO0O00O00O0OOOOOO ,OOO0O0O0000O00OO0 ):
        O0OO0OO00O0O00OO0 =OOO0O0O0000O00OO0 .GetDC ()
        O0O0O00O00O0O00O0 ,O0O00O000OO00OO0O =OO0O00O00O0OOOOOO .GetClientSize ()
        OOO0O0OOOOOOO0000 =wx .Image ("BG.png",wx .BITMAP_TYPE_ANY )
        OOO0O0OOOOOOO0000 =OOO0O0OOOOOOO0000 .Scale (O0O0O00O00O0O00O0 ,O0O00O000OO00OO0O ,wx .IMAGE_QUALITY_HIGH ).ConvertToBitmap ()
        O0OO0OO00O0O00OO0 .DrawBitmap (OOO0O0OOOOOOO0000 ,0 ,0 )
        O0O0OOO0000OOO000 =wx .Font (12 ,wx .FONTFAMILY_DEFAULT ,wx .FONTSTYLE_NORMAL ,wx .FONTWEIGHT_NORMAL )
    def OnResize (O0OO000000O00OOO0 ,OO0O0000OO000000O ):
        O0O00OOO0O00O0000 =O0OO000000O00OOO0 .GetClientSize ()
        if O0O00OOO0O00O0000 !=O0OO000000O00OOO0 .last_size :
            O0OO000000O00OOO0 .last_size =O0O00OOO0O00O0000 
            wx .CallLater (200 ,O0OO000000O00OOO0 .Refresh )
            OO0O0000OO000000O .Skip ()
    def on_qq_query (O000OO000OOO00000 ,OO0OO000000000O0O ):
        threading .Thread (target =O000OO000OOO00000 .qq_query_thread ).start ()
    def qq_query_thread (OO0000OO0OO00OOOO ):
        OO00OO0O00000O000 =OO0000OO0OO00OOOO .qq_input .GetValue ()
        if OO00OO0O00000O000 =="":
            OO0000OO0OO00OOOO .qq_result .SetLabel ("未检测到用户输入")
        else :
            O0O0O0O0OO0OOO00O =len (OO0000OO0OO00OOOO .qq_input .GetValue ())
            if O0O0O0O0OO0OOO00O >10 :
                OO0000OO0OO00OOOO .qq_result .SetLabel ("你输入的数据太长了，不是QQ号")
            else :
                OO0000OO0OO00OOOO .qq_result .SetLabel ("查询中……")
                OO0000OO0OO00OOOO .qq_result .SetLabel ("查询中……")
                O00OO00OO00O0OO0O =requests .get ('https://zy.xywlapi.cc/qqcx2023?qq='+OO00OO0O00000O000 ).text 
                if "查询成功"in O00OO00OO00O0OO0O :
                    O0O0O00O00O0O0O00 ="qq: {}\n电话号码: {} {}".format (OO00OO0O00000O000 ,O00OO00OO00O0OO0O [40 :51 ],O00OO00OO00O0OO0O [66 :73 ]+"\n内容已复制")
                    pyperclip .copy (O0O0O00O00O0O0O00 .replace ("\n内容已复制",""))
                    OO0000OO0OO00OOOO .qq_result .SetLabel (O0O0O00O00O0O0O00 )
                elif "没有找到"in O00OO00OO00O0OO0O :
                    OO0000OO0OO00OOOO .qq_result .SetLabel ("qq: {} 没有找到电话号码".format (OO00OO0O00000O000 ))
    def on_phone_query (OOO00O000O0O00OOO ,OOOOOO000OOOOOO0O ):
        threading .Thread (target =OOO00O000O0O00OOO .phone_query_thread ).start ()
    def phone_query_thread (O0OO000O0OO0OOO00 ):
        OO0OO0O00O0O0O0OO =O0OO000O0OO0OOO00 .phone_input .GetValue ()
        if OO0OO0O00O0O0O0OO =="":
            O0OO000O0OO0OOO00 .phone_result .SetLabel ("未检测到用户输入")
        else :
            O0O00OO000O0O0000 =len (O0OO000O0OO0OOO00 .phone_input .GetValue ())
            if O0O00OO000O0O0000 >11 :
                O0OO000O0OO0OOO00 .phone_result .SetLabel ("你输入的数据太长了，不是手机号")
            else :
                O0OO000O0OO0OOO00 .phone_result .SetLabel ("查询中……")
                O0OO000O0OO0OOO00 .phone_result .SetLabel ("查询中……")
                O0OO0OO00OOOOO0O0 =requests .get ("https://zy.xywlapi.cc/qqphone?phone="+OO0OO0O00O0O0O0OO ).text 
                if "查询成功"in O0OO0OO00OOOOO0O0 :
                    O00OOO000000O000O ="电话: {}\n对应qq号码是: {}".format (OO0OO0O00O0O0O0OO ,O0OO0OO00OOOOO0O0 [37 :47 ]+"\n内容已复制")
                    pyperclip .copy (O00OOO000000O000O .replace ("\n内容已复制",""))
                    O0OO000O0OO0OOO00 .phone_result .SetLabel (O00OOO000000O000O )
                elif "没有找到"in O0OO0OO00OOOOO0O0 :
                    O0OO000O0OO0OOO00 .phone_result .SetLabel ("电话: {} 没有找到qq号码".format (OO0OO0O00O0O0O0OO ))
    def WeiboSearch (O0O00000OO0OO0000 ,OOOO00O000000O000 ):
        threading .Thread (target =O0O00000OO0OO0000 .weibo_query_thread ).start ()
    def weibo_query_thread (OOO00OOOO0OOO0O00 ):
        OOOOOOO000O0OOOO0 =OOO00OOOO0OOO0O00 .weibo_input .GetValue ()
        if OOOOOOO000O0OOOO0 =="":
            OOO00OOOO0OOO0O00 .weibo_result .SetLabel ("未检测到用户输入")
        else :
            OOO00OOOO0OOO0O00 .weibo_result .SetLabel ("查询中……")
            OOO00OOOO0OOO0O00 .weibo_result .SetLabel ("查询中……")
            O0O000OOOOO00OO00 =requests .get ("https://zy.xywlapi.cc/wbapi?id="+OOOOOOO000O0OOOO0 ).text 
            if "查询成功"in O0O000OOOOO00OO00 :
                O00O0O0OO0O00000O =json .loads (O0O000OOOOO00OO00 )
                OOO00OOOO0OOO0O00 .weibo_result .SetLabel ("微博ID: {} 的电话号码是：{} {} 内容已复制".format (OOOOOOO000O0OOOO0 ,O00O0O0OO0O00000O ["phone"],O00O0O0OO0O00000O ["phonediqu"]))
                OO0O000OOO0000000 ="微博ID: {} 的电话号码是：{} {}".format (OOOOOOO000O0OOOO0 ,O00O0O0OO0O00000O ["phone"],O00O0O0OO0O00000O ["phonediqu"])
                pyperclip .copy (OO0O000OOO0000000 )
            elif "没有找到"in O0O000OOOOO00OO00 :
                OOO00OOOO0OOO0O00 .weibo_result .SetLabel ("微博ID: {} 没有找到电话号码".format (OOOOOOO000O0OOOO0 ))
if __name__ =="__main__":
    app =wx .App (False )
    frame =MyFrame (None ,"隐私查询软件 "+"本软件需要联网"+" 请勿用于非法用途！后果自负！")
    frame .Show ()
    app .MainLoop ()