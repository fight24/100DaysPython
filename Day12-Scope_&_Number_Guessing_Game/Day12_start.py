# ################## Scope ####################

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# # Local Scope
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

# # Global Scope
# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion()

# # There is no Block Scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
#
#
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
