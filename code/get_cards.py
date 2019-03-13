import requests

for series in range(0,20):
    print("series" , str(series))
    for i in range(0,5):

        url = "https://www.iyingdi.com/hearthstone/card/search/vertical"
        cnt = i
        datas = "ignoreHero=1&series=" + str(series) + "&statistic=total&order=-series%2C%2Bmana&token=&page=" + str(cnt) + "&size=99"
        headers = {
            "Referer": "https://www.iyingdi.com/web/tools/hearthstone/cards?pagetype=inquire&series=" + str(series) ,
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie" : "pgv_pvid=325323865; tj_system=web; tj_version=100; tj_channel=iyingdi; tj_uuid=AFDV10JBDUP2EB4L; Hm_lvt_d8df04a6febf13b5f9ff26531fece72c=1552031286,1552439690,1552456485; acw_tc=7b39758315520313008185449e08042b04abe5efea5c42bb60ec7db911baba; BAIDU_SSP_lcr=https://www.iyingdi.cn/; __qc_wId=218; Hm_lpvt_d8df04a6febf13b5f9ff26531fece72c=1552456516; tj_userid=-1; tj_sign=d1d4d7f76cbfaa9027fa6fe2685a804c"
        }
        r = requests.post(url,data=datas,headers=headers)
        with open("series" + str(series) + str(cnt) + ".txt",'w',encoding="utf-8") as f1:
            print(r.content.decode("utf-8"))
            f1.write(r.content.decode("utf-8"))