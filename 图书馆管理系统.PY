book={'计算机应用基础':10,'':15,'MySQL项目应用':30,'心理学':5,'大学英语':8,'Dreamweaver使用教程':2,
      'Photoshop实用基础':13,'网络安全':6,'人工智能':8}
flag = 1
while flag == 1:
    print('欢迎来到图书管理系统，可选择的功能有：\n1、查询\n2、外借\n3、补充\n4、下架\n5、退出')
    menu = input('请选择：')
    if menu == '1':
        print('查询功能：')
        bookname = input('请输入您要查询的书籍名：')
        if bookname in book:
            print('%s的库存为%s:'%(bookname,book[bookname]))
        else:
            print('图书库没有该书籍')

    elif menu == '2':
        print('外借功能：')
        bookname = input('请输入您要外借的书籍：')
        if bookname in book:
            num = int(input('请输入您要外借的数量：'))
            #判断库存是否足够外借
            if book[bookname] >= num:
                #外借
                book[bookname] = book[bookname] - num
                print('外借成功！%s的剩余库存为：%s本'%(bookname,book[bookname]))
            else:
                print('库存不够!%s仅有%s本'%(bookname,book[bookname]))
        else:
            print('图书库没有该书籍，无法外借！')

    elif menu == '3':
        print('补充功能：')
        bookname = input('请输入你要补充的书籍名：')
        num = int(input('请输入你要补充的书籍数量：'))
        if bookname in book:
            book[bookname] = book[bookname] + num
        else:
            book[bookname] = num
        print('补充成功，%s的现有库存为%s'%(bookname,book[bookname]))

    elif menu == '4':
        print('下架功能：')
        bookname = input('请输入您要下架的书籍名：')
        if bookname in book:
            del book[bookname]
            print('下架成功，图书库现有库存情况为：\n%s'%book)
        else:
            print('图书库没有该书籍！')

    elif menu == '5':
        print('已退出')
        flag=1
    else:
        print('选择功能错误，已退出系统')