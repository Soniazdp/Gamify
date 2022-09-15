'''
Test Cases for Gamification of Exercise, 
which should be copied and pasted to the gamify.py file for direct use.
'''
# ########

#     initialize()
#     perform_activity("running", 120)
#     perform_activity("running", 30)
#     perform_activity("running", 50)
#     print(get_cur_health())             # 560
#     print(get_cur_hedons())             # -360
#     print("            ")


# ########

#     initialize()
#     perform_activity("running", 150)
#     perform_activity("textbooks", 1)
#     perform_activity("running", 50)
#     print(get_cur_health())             # 602
#     print(get_cur_hedons())             # -362
#     print("            ")


# #######

#     initialize()
#     print("**************************************")
#     offer_star("textbooks")
#     perform_activity("running", 90)
#     print(get_cur_health())                     # 270
#     print(get_cur_hedons())                     # -140
#     print(cur_star)
#     print("        ")

#     offer_star("running")
#     perform_activity("resting", 29)
#     print(get_cur_health())             # 270
#     print(get_cur_hedons())             # -140
#     print(cur_star)
#     print("         ")

#     offer_star("running")
#     perform_activity("running", 10)
#     print(get_cur_health())             # 300
#     print(get_cur_hedons())             # -160
#     print(cur_star)
#     print(bored_with_stars)             # True
#     print("         ")

#     perform_activity("running", 5)
#     print(get_cur_health())             #315
#     print(get_cur_hedons())             #-170
#     print(cur_star)
#     print(bored_with_stars)             # True
#     print("   ")

#     offer_star("resting")
#     print(star_can_be_taken("resting")) # False

# ########

#     initialize()
#     perform_activity("textbooks", 200)
#     offer_star("running")
#     offer_star("running")
#     perform_activity("running", 10)
#     print(get_cur_health())             # 430
#     print(get_cur_hedons())             # -150
#     print("       ")

# #########

#     initialize()                       # Test Star behaviour
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks
#     offer_star("textbooks")
#     print(bored_with_stars)            # True
#     print(most_fun_activity_minute())  # running

#     initialize()
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks
#     offer_star("textbooks")
#     perform_activity("running", 30)
#     print(most_fun_activity_minute())  # resting

#     initialize()
#     offer_star("textbooks")
#     perform_activity("running", 101)
#     print(get_cur_health()) # 303
#     print(get_cur_hedons()) # -162
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks
#     perform_activity("textbooks", 20)
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks

#     initialize()
#     offer_star("resting")
#     offer_star("textbooks")
#     perform_activity("running", 101)
#     print(get_cur_health()) # 303
#     print(get_cur_hedons()) # -162
#     perform_activity("textbooks", 20)
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks
#     perform_activity("textbooks", 20)
#     offer_star("textbooks")
#     print(most_fun_activity_minute())  # textbooks