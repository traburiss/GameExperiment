# GameExperiment
### 一个关于游戏策略的玩意，目前包括：
* 剪刀石头布策略:
    + 选手:
        1. 标准随机出手型的剪刀石头布选手 StandardJsbPlayer
        2. 有出手喜好，会随着自己的输赢修改自己出手喜好的剪刀石头布选手 SimpleJsbPlayer
    + 裁判:
        1. 严格判决，从不黑哨的裁判 StandardJsbJudgment
    + 场地:
        2. 想干嘛就干嘛的游戏场地文件 game.py
        

* 打井机器人(施工中):
    + 选手:
        1. 根据我对AI的理解弄出来的玩打井机器人,虽然我猜我的理解八成是错的 MyDjPlayer
            - 每次游戏结束后，保存对局的当前局面、下法，胜负次数到数据库
            - 游戏中每次面对某个局面提取数据库数据进行匹配，根据胜负概率进行选择下一步下法，找不到就乱下 
