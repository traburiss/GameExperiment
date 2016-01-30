# Created by Traburiss on 2016/1/27
from people.judgment.jsb_judgment.standard_jsb_judgment import StandardJsbJudgment
from people.player.jsb_player.simple_jsb_player import SimpleJsbPlayer


a = SimpleJsbPlayer(1, "a", [10, 1, 1])
b = SimpleJsbPlayer(2, "b", [1, 10, 1])
c = SimpleJsbPlayer(3, "c", [1, 1, 1])
d = SimpleJsbPlayer(4, "d", [1, 1, 1])

# a.actions()
# b.actions()
# c.actions()
# d.actions()
#
# print(a.get_action_result())
# print(b.get_action_result())
# print(c.get_action_result())
# print(d.get_action_result())
#
j = StandardJsbJudgment("j")
# j.ruling([a.get_action_result(), b.get_action_result(), c.get_action_result(), d.get_action_result()])
# print(j.get_result_name())
# print("winner:" + str(j.get_winner()))
# print("loser" + str(j.get_loser()))


point = dict()
total = 10000
for i in range(total):
    a.actions()
    b.actions()
    c.actions()
    d.actions()
    a.game_tactics([b.get_action_result(), c.get_action_result(), d.get_action_result()])
    b.game_tactics([a.get_action_result(), c.get_action_result(), d.get_action_result()])
    # c.game_tactics([a.get_action_result(), b.get_action_result(), d.get_action_result()])
    # d.game_tactics([a.get_action_result(), b.get_action_result(), c.get_action_result()])
    j.ruling([a.get_action_result(),
              b.get_action_result(),
              c.get_action_result(),
              d.get_action_result()])
    if j.get_result_code() == 2:
        for item in j.get_winner():
            if item[SimpleJsbPlayer.PLAYER_NAME] in point:
                point[item[SimpleJsbPlayer.PLAYER_NAME]] += 1
            else:
                point[item[SimpleJsbPlayer.PLAYER_NAME]] = 1
    else:
        if "P" in point:
            point["P"] += 1
        else:
            point["P"] = 1
print(point)
for item in point:
    print(item + "::" + str(point[item]/total*100)+"%")


# point = dict()
# total = 10000
# for i in range(total):
#     b.actions()
#     if b.get_action_result()[b.JSB_NAME] in point:
#         point[b.get_action_result()[b.JSB_NAME]] += 1
#     else:
#         point[b.get_action_result()[b.JSB_NAME]] = 1
#
# print(point)
