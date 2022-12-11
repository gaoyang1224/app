class Login:
    success_test = [
        {'title':'登录成功', 'user':'15195989321', 'pwd':'989321', 'expected':True}
    ]

    fail_test = [
        {'title': '账号为空', 'user': '', 'pwd': '989321', 'expected': '手机号码或密码不能为空'},
        {'title': '密码为空', 'user': '', 'pwd': '989321', 'expected': '手机号码或密码不能为空'},
        {'title': '密码错误', 'user': '15195989321', 'pwd': '123456', 'expected': '错误的账号信息'},
    ]