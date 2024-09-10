import requests
import time

def save():
    with open('data.txt','w',encoding='utf-8') as w:
        w.write(r.text)
    for i in range(3):
        print('...')
        time.sleep(1)
    print('set')

def rp():
    r = requests.post(getthing,headers=h,allow_redirects=False)
    return r
def rr():
    r = requests.get(getthing,headers=h,allow_redirects=False)
    return r
getthing = input('请输入URL：')
p = input('是否为图片或媒体数据\n1:yes\\默认 2:no\nPC:')
ess = input('1:post\\2:get\nPC:')
timeout = 0
h = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
if ess == '2':
    if p == '1':
        while True:
            try:
                r = rr()
            except:
                time.sleep(1)
                timeout += 1
                if timeout == 5:
                    print('URL已出错或连接不上')
                    quit(404)
            else:
                print(f"{r}\n状态码：{r.status_code}\n响应URL：{r.url}\n数据类型：{type(r.text)}\n----------------------\n")
                print(r.content)
                with open('data.png', 'wb') as f:
                    f.write(r.content)
                quit(200)
    while True:
        try:
            r = rr()
        except:
            print('错误URL！！！')
            print('正在重新尝试',f"已重新 {timeout}/5 此")
            time.sleep(1)
            timeout += 1
            if timeout == 5:
                print('URL已出错或连接不上')
                quit(404)
        else:
            print(f"{r}\n状态码：{r.status_code}\n响应URL：{r.url}\n数据类型：{type(r.text)}\n----------------------\n")
            print(r.text)
            save()
            break
elif ess == '1':
    if p == '1':
        while True:
            try:
                r = rp()
            except:
                print('错误URL！！！')
                print('正在重新尝试', f"已重新 {timeout}/5 此")
                time.sleep(1)
                timeout += 1
                if timeout == 5:
                    print('URL已出错或连接不上')
                    quit(404)
            else:
                print(f"{r}\n状态码：{r.status_code}\n响应URL：{r.url}\n数据类型：{type(r.text)}\n----------------------\n")
                print(r.content)
                with open('data.png', 'wb') as f:
                    f.write(r.content)
                quit(200)
    while True:
        try:
            r = rp()
        except:
            print('错误URL！！！')
            print('正在重新尝试',f"已重新 {timeout}/5 此")
            time.sleep(1)
            timeout += 1
            if timeout == 5:
                print('URL已出错或连接不上')
                quit(404)
        else:
            print(f"{r}\n状态码：{r.status_code}\n响应URL：{r.url}\n数据类型：{type(r.text)}\n----------------------\n")
            print(r.text)
            save()
            break
else:
    print('unknow word',ess)
quit()
