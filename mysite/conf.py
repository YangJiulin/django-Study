SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_TITLE = '百度一下你就知道'
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['报告列表', '静态测试', '动态测试'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{
        'name': '报告列表',
        'icon': 'fas fa-code',
        'url': 'https://gitee.com/tompeppa/simpleui'
    }, {
        # 自2021.02.01+ 支持多级菜单，models 为子菜单名
        'app':'pretreat',
        'name': '静态测试',
        'icon': 'fa fa-file',
      	# 二级菜单
        'models': [{
            'name': '文件上传反编译',
            'icon': 'far fa-surprise',
            'url': 'pretreat/appbaseinfo'
            # 第三级菜单 ，
        }, {
            'name': '词法分析',
            'icon': 'fab fa-git',
            'url': 'pretreat/appmoreinfo'
        },
        {
            'name': '污点分析',
            'url': 'https://www.wezoz.com',
            'icon': 'fab fa-git'
        }]
    }, {
        'name': '动态测试' ,
        'icon': 'fa fa-desktop',
        'models': [{
            'name': 'Http中间人',
            'url': 'http://baidu.com',
            'icon': 'far fa-surprise'
        }]
    }]
}