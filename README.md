# PythonSuperMario

## 架构
main.py作为游戏主入口 

Resource文件夹放置资源文件

Source

> constants.py 存放一些常量  
> sound.py 音乐相关  
> setup.py 游戏启动时加载的代码  
> tools.py 游戏主控工具  

> data 放置数据  
>> maps文件放关卡  
>> player放角色


>  components 放置游戏部件 放置游戏 人物 相关的一些代码
>> box.py 可以顶的方格  
>>  brick.py 砖块  
>> coin.py 金币  
>> enemy.py 敌人  
>> player.py 主角  
>> powerup.py 蘑菇等增强道具  


> states 游戏状态
> > main_menu.py 游戏开始的主菜单  
> > load_screen.py 载入画面  
> > level.py 游戏的关卡



## 1. 问题:
我将
> pygame.init()  
> pygame.display.set_mode(C.SCREEN_W, C.SCREEN_H)

放在setup文件中, 他是怎么执行到的呢?

GRAPHICS?

VScode如何设置在任何界面下运行都是从main.py开始运行?