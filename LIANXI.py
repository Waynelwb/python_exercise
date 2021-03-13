def make_album(sing,cd,number = ''):

    data = {'歌手名字':sing,'唱片名字':cd}
    if number:
        data['number'] = number
    return data
sing_name = '请输入歌手名：（输入‘quit’退出）'
cd_name = '请输入专辑名：（输入‘quit’退出）'
while True:
    a = input(sing_name)
    b = input(cd_name )
    if a == 'quit' or b == 'quit':
        break
    else:
        c = make_album(a,b)
        print(c)