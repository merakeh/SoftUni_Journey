decorations_bought_a_day = int(input())
days_until_christmas = int(input())
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_light_price = 15
# ornament_set_points = 5
# tree_skirt_points = 3
# tree_garland_points = 10
# tree_light_points = 17
#
# total_cost = 0
# total_spirit = 0
#
#
# for day in range(1, 1+days_until_christmas):
#     if day % 2 == 0:
#         total_cost += decorations_bought_a_day * ornament_set_price
#         total_spirit += decorations_bought_a_day * ornament_set_points
#     if day % 3 == 0:
#         total_cost += (tree_skirt_price + tree_garland_price) * decorations_bought_a_day
#         total_spirit += (tree_skirt_points + tree_garland_points) * decorations_bought_a_day
#     if day % 5 == 0:
#         total_cost += tree_light_price
#         total_spirit += 17
#
#     if day % 10 == 0:
#         total_spirit -= 20
#         total_cost += 23
#
#     if day == days_until_christmas and day % 10 == 0:
#         total_spirit -= 30
#
#
# print(total_cost, total_spirit)