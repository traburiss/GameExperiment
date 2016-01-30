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