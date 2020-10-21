print('請輸入您的名字')
yourName = input()
print('請輸入您的年齡')
yourAge = int(input())
if yourAge>22:
    print(yourName + ':')
    print('念研究所或在工作了')
else:
    if yourAge<12:
        print(yourName + ':')
        print('小學還沒畢業')
    elif yourAge<15:
        print(yourName + ':')
        print('國中還沒畢業')
    elif yourAge<18:
        print(yourName + ':')
        print('高中還沒畢業')
    else:
        print(yourName + ':')
        print('大學還沒畢業')