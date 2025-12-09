# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ydimitra <ydimitra@student.42.f>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 20:25:08 by ydimitra          #+#    #+#              #
#    Updated: 2025/12/08 20:36:27 by ydimitra         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")

ft_count_harvest_iterative()
