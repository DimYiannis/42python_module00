# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ydimitra <ydimitra@student.42.f>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 20:33:39 by ydimitra          #+#    #+#              #
#    Updated: 2025/12/08 20:52:33 by ydimitra         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(day = 1, total_days=None):
    if total_days is None: 
        total_days = int(input("Days until harvest: "))
    if day > total_days:
        print("Harvest time!")
        return
    print(f"Day {day}") 
    ft_count_harvest_recursive(day + 1, total_days)
   

ft_count_harvest_recursive()
