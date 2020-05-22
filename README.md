# Delta Dental
This repo contains the code for a programming exercise conducted by Delta Dental
## Conference Room Scheduling
Finds the nearest open conference room for a team depending on their requirements
* rooms.txt file contains details about all the conference rooms there are in the building
* room_schedule.py finds the nearest conference room


Steps Followed to solve the problem.

Program starts as: 

1. Getting the size of the team.

2. Entering the floor on which team works.

3. Start and end time of the meeting.

4. All the parameters are passed to room_scheduler fun which schedules the metting as per the availability.

5. Reading txt file containing details of the conference rooms as a input to the program
6. Then storing details of all conference rooms in a list
7. Will get total number of conference rooms available
8. Creating a dictionary to store capacity of conference room as the value for each corresponding conference rooms
9. Creating a dictionary to store the available timings for each corresponding conference room
10. Available timings are stored as a list of tuples which consists (start_time, end_time)

11. Created a fun room_scheduler the funtionality as follows:  
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
    
  12. filtering out rooms based on the meeting timings and storing all the suitable rooms in a list
  
  13. more than 1 rooms are available, the best room is selected
  
  14. eating a dictionary which stores the floor number of each corresponding conference room
  
  15. The floor nearest to the teams floor is considered the best_floor
  
  16. Filtering out only the conference rooms present on the best floor
  
  17. All the suitable conference rooms are returned as a list
  
  18. If no rooms are suitable, an error message is returned
