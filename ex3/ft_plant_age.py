# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ydimitra <ydimitra@student.42.f>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 20:14:47 by ydimitra          #+#    #+#              #
#    Updated: 2025/12/08 20:19:30 by ydimitra         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = int( input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
       
