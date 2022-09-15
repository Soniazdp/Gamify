# Gamification of Exercise

In this project, a simulator for an app is designed to reward students with "health points" and "fun points (AKA. hedons)" for exercising while attending the Zoom University. It can model how users behave and test various strategies to help students gain maximal points.

## Details of Activities

### Rewards

The basic mechanism of the game works as the following. Every user starts with 0 health points and 0 hedons. When students perform an activity, including running, resting, and carrying textbooks, they will receive a certain number of hedons given the duration of the activity. More specifically, 

- Running worths 3 health points/min, for up to 180 min. When it exceeds the limit, running then depreciates to 1 health point/min for the extra duration.
- Carrying textbooks always worths 2 health points/min.
- Resting worths no hedons.

### Consumption 

Furthermore, users are tired when they finish running or carrying books less than 2 hours before another activity is initiated. If the user is tired, running and carrying textbooks **consume** 2 hedons/min. If they are not tired,
- running worths 2 hedons/min before the first 10 mins limit, but it starts to **consume** 2 hedons/min after the limit;
- carrying textbooks worths 1 hedon/min before the first 20 mins limit, but it starts to **consume** 1 hedon/min after the limit.

## Offering of Stars
There is also a system of rewarding and using stars. When an activity is offered with a star, the user can use the star immediately to gain extra 3 hedons/min for the first 10 mins, if this is their first time to conduct an activity. 

However, if there are 3 stars offered within 2 hours, the user will not get additional 3 hedons/hour for the activities until the end of the game.

## Credits

The project is originally designed by Michael Guerzhoy for his class ESC180, which is implemented by Bonnie Luo and Sonia Zeng in the Fall of 2020.

