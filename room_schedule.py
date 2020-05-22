import datetime

# reading txt file containing details of the conference rooms
with open("rooms.txt") as f:
    content = f.readlines()
rooms = [x.strip() for x in content]  # storing details of all conference rooms in a list

total_rooms = len(rooms)  # total number of conference rooms available

# creating a dictionary to store capacity of conference room as the value for each corresponding conference rooms
capacity_dict = {}
for room in rooms:
    capacity_dict[room.split(',')[0]] = int(room.split(',')[1])

# creating a dictionary to store the available timings for each corresponding conference room
timings_dict = {}
for room in rooms:
    time_iterator = iter([datetime.datetime.strptime(j, '%H:%M').time() for j in room.split(',')[2:]])
    timings_dict[room.split(',')[0]] = list(zip(*[iter(
        time_iterator)] * 2))  # available timings are stored as a list of tuples which consists (start_time, end_time)


def room_scheduler(size, floor, start, end):
    """
    Finds nearest available conference room/rooms for a team

    Parameters
    ----------
    :param size : int
        size of the team which needs a conference room
    :param floor : int
        the floor on which the team works
    :param start : datetime.time
        start time of the team meeting
    :param end : datetime.time
        end time of the team meeting

    Returns
    -------
    :return result : list
        List of best suitable conference room/rooms for the team. If no conference room is suitable for the team
        requirements, a string is returned which says 'no room available'
        - The result is a list and not a single room because there could be multiple rooms available for the team in
          the floor closest to the team
    """

    size_compatible_rooms = list(
        dict((x, y) for x, y in capacity_dict.items() if y >= size).keys())  # filtering out rooms based on team size

    # filtering out rooms based on the meeting timings and storing all the suitable rooms in a list
    compatible_rooms_list = []
    for i in size_compatible_rooms:
        for j in timings_dict[i]:
            if j[0] <= start and j[1] >= end:
                compatible_rooms_list.append(i)

    # if more than 1 rooms are available, the best room is selected
    if len(compatible_rooms_list) > 1:

        # creating a dictionary which stores the floor number of each corresponding conference room
        compatible_rooms_floor_dict = {}
        for i in compatible_rooms_list:
            compatible_rooms_floor_dict[i] = int(i.split('.')[0])

        # The floor nearest to the teams floor is considered the best_floor
        best_floor = min(list(compatible_rooms_floor_dict.values()), key=lambda x: abs(x - floor))

        # filtering out only the conference rooms present on the best floor
        compatible_rooms_list = list(dict((x, y) for x, y in
                                          compatible_rooms_floor_dict.items() if y == best_floor).keys())

    if len(compatible_rooms_list) > 0:
        return compatible_rooms_list  # all the suitable conference rooms are returned as a list
    else:
        return 'no room available'  # if no rooms are suitable, an error message is returned


if __name__ == '__main__':
    team_size = int(input("Please enter the team size : "))
    team_floor = int(input("Please enter the floor on which the team works : "))
    start_time = datetime.datetime.strptime(input("Please enter the start time of the meeting : "), '%H:%M').time()
    end_time = datetime.datetime.strptime(input("Please enter the end time of the meeting : "), '%H:%M').time()
    print(room_scheduler(team_size, team_floor, start_time, end_time))
