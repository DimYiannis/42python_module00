# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ydimitra <ydimitra@student.42.f>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 20:20:29 by ydimitra          #+#    #+#              #
#    Updated: 2025/12/08 20:23:56 by ydimitra         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


