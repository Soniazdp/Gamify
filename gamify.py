'''
A simulator for an app that encourages students to exercise when taking online courses at home.
Specific mechanism of rewarding stars, health points and hedons are discussed in README.md

Authors: Bonnie & Sonia 
'''
import random

cur_hedons = cur_health = last_activity_duration = cur_time = last_finished = 0
cur_star = cur_star_activity = last_activity = None
bored_with_stars = False


def initialize():
    '''
    Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it
    '''

    global cur_hedons, cur_health
    global cur_star, cur_star_activity

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars

    cur_hedons = 0
    cur_health = 0

    cur_star = [-1000, -1000, -1000]
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = 1000  


def perform_activity(activity, duration):
    '''
    Simulate the user's performing activity for duration minutes.
    activity: str
    duration: +ve int
    '''
    global cur_time, cur_health, cur_hedons, last_finished, last_activity_duration, last_activity

    if activity in ["running", "textbooks", "resting"] and duration > 0 and type(duration) == int:

        # Health points gained from running
        if activity == "running":
            if (last_activity != activity and duration <= 180) or (last_activity == activity
                                                                   and duration + last_activity_duration <= 180):
                cur_health += 3 * duration
            elif last_activity != activity and duration > 180:  # not a continuation of the last activity
                cur_health += 3 * 180 + duration - 180
            elif last_activity == activity and duration + last_activity_duration > 180:  # a continuation
                cur_health += (180 - last_activity_duration) * 3 + (duration + last_activity_duration - 180)

        # Health points gained from carrying textbooks
        if activity == "textbooks":
            cur_health += 2 * duration
            
        # No points gained from resting
        if activity == "resting":
            cur_health += 0
            cur_hedons += 0


        # Rest time is over 120 minutes - user not tired
        if last_finished >= 120:  

            if activity == "running":

                if (last_activity != activity and duration <= 10) or (last_activity == activity
                                                                      and duration + last_activity_duration <= 10):
                    # Hedons gained from running
                    cur_hedons += 2 * duration
                elif last_activity != activity and duration > 10:  # not a continuation of the last activity
                    cur_hedons += 10 * 2 + (duration - 10) * (-2)
                elif last_activity == activity and duration + last_activity_duration > 10:  # a continuation
                    cur_hedons += (10 - last_activity_duration) * 2 + (-2) * (duration + last_activity_duration - 10)

            if activity == "textbooks":

                # Hedons gained from carrying textbooks
                if (last_activity != activity and duration <= 20) or (last_activity == activity
                                                                      and duration + last_activity_duration <= 20):
                    cur_hedons += duration
                elif last_activity != activity and duration > 20:
                    cur_hedons += 20 - (duration - 20)
                elif last_activity == activity and duration + last_activity_duration > 20:
                    cur_hedons += (20 - last_activity_duration) + (-1) * (duration + last_activity_duration - 20)

            ## added 0 <= and added elif
        elif 0 <= last_finished <= 120:  # Hedon deduction from tiredness
            if activity != "resting":
                cur_hedons -= 2 * duration


        if activity == "resting" and last_activity != "resting":  # Update resting time
            last_finished = duration
        elif activity == "resting" and last_activity == "resting":
            last_finished += duration
        elif activity != "resting":
            last_finished = 0
            
        if star_can_be_taken(activity) == True:
            if duration <= 10:
                cur_hedons += 3 * duration
            else:
                cur_hedons += 30

        if activity == last_activity:  # Update for next use
            last_activity_duration += duration
        else:
            last_activity_duration = duration
            last_activity = activity

        cur_time += duration


def get_cur_hedons():
    """Return the num of hedons
    return: int"""

    return cur_hedons


def get_cur_health():
    """Return the num of health points
    return: int"""

    return cur_health


def offer_star(activity):
    """
    Simulate a offering the user a star for doing the activity
    activity: str
    """
    global cur_time, cur_star_activity, cur_star, bored_with_stars

    if activity in ["running", "textbooks"]:

        cur_star_activity = activity
        if type(cur_time) == int:
            cur_star.pop(0)
            cur_star.append(cur_time)

        time_elapsed = cur_star[2] - cur_star[0]

        if time_elapsed < 120:
            bored_with_stars = True

        else:
            bored_with_stars = False


def star_can_be_taken(activity):
    """
    Return True iff a star can be used to get more hedons for activity
    activity: str
    return: boolean
    """

    global cur_star, cur_time, cur_star_activity, bored_with_stars

    if activity == "resting":
        return False

    elif activity in ["running", "textbooks"]:
        if cur_star_activity == activity and cur_star[2] == cur_time and bored_with_stars == False:
            return True
        else:
            return False


def most_fun_activity_minute():
    '''
    Return the activity that gives the most hedon if the user perform it at
    the current time
    return: str
    '''
    global cur_star_activity, last_finished, last_activity, last_activity_duration

    most_fun_activity = ""
    running_hedon = 0
    textbooks_hedon = 0
    resting_hedon = 0

    # If a star can be taken
    if star_can_be_taken("running") == True and cur_star_activity == "running":
        running_hedon += 3

    elif star_can_be_taken("textbooks") == True and cur_star_activity == "textbooks":
        textbooks_hedon += 3

    # User not tired
    if last_finished >= 120:
        if last_activity == "running":
            # Hedon gain for running ---- continuing last activity
            if last_activity_duration < 10:
                running_hedon += 2
            elif last_activity_duration >= 10:
                running_hedon += -2

            # Hedon gain for textbooks
            textbooks_hedon += 1


        elif last_activity == "testbooks":
            # Hedon gain for running
            running_hedon += 2

            # Hedon gain for textbooks ---- continuing last activity
            if last_activity_duration < 20:
                textbooks_hedon += 1
            elif last_activity_duration >= 20:
                textbooks_hedon += -1


    # User tired
    elif last_finished < 120:
        running_hedon += -2
        textbooks_hedon += -2

    # Deciding the "most_fun_activity"
    if textbooks_hedon > running_hedon and textbooks_hedon > resting_hedon:  # textbooks is the max
        most_fun_activity = "textbooks"

    elif running_hedon > textbooks_hedon and running_hedon > resting_hedon:  # running is the max
        most_fun_activity = "running"

    elif resting_hedon > running_hedon and resting_hedon > textbooks_hedon:  # resting is the max
        most_fun_activity = "resting"

    elif running_hedon == textbooks_hedon > resting_hedon:
        most_fun_activity = random.choice(["textbooks", "running"])
    elif running_hedon == resting_hedon > textbooks_hedon:
        most_fun_activity = random.choice(["running", "resting"])
    elif textbooks_hedon == resting_hedon > running_hedon:
        most_fun_activity = random.choice(["textbooks", "resting"])
    elif running_hedon == textbooks_hedon == resting_hedon:
        most_fun_activity = random.choice(["running", "resting", "textbooks"])

    return most_fun_activity


################################################################################

if __name__ == '__main__':
    initialize()
    
    # Sample Activities
    perform_activity("running", 30)
    print(get_cur_hedons())  # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health())  # 90 = 30 * 3
    print(most_fun_activity_minute())  # resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running
    perform_activity("textbooks", 30)
    print(get_cur_health())  # 150 = 90 + 30*2
    print(get_cur_hedons())  # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())  # 210 = 150 + 20 * 3
    print(get_cur_hedons())  # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())  # 700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())  # -430 = -90 + 170 * (-2)
    print("            ")