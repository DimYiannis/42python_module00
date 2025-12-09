# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ydimitra <ydimitra@student.42.f>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 20:08:45 by ydimitra          #+#    #+#              #
#    Updated: 2025/12/08 20:13:56 by ydimitra         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print(f"Total harvest: {total}");

