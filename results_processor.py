# This module processes the winner

def process_results(master_state_map, rigged_party):
    """
    This function processes the election results
    :return:
    """
    party = ""
    reps_electorate_points = 0
    dems_electorate_points = 0
    total_num_votes = 0
    rigged_electoral_points = 0

    if rigged_party is None:




        for state_num, state_data in master_state_map.items():
            print(f"state_num: {state_num}, this represents the item number in the dictionary.")
            print(f"state_data: {state_data}, this contains all the state data")
            # print(state_data)
            for key, value in state_data.items():
                if key == 'state':
                    print(f"state: {value}")
                elif key == 'num_voters':
                    print(f"num_voters: {value}")
                elif key == 'party':
                    print(f"party: {value}")
                    party = value
                elif key == 'votes':
                    print(f"votes: {value}")
                    total_num_votes += value
                elif key == 'electorate':
                    print(f"electorate: {value}")
                    if party == "republican":
                        reps_electorate_points += value
                    elif party == "democrat":
                        dems_electorate_points += value

    print(f"reps: {reps_electorate_points}")
    print(f"dems: {dems_electorate_points}")
    print(f"the total amount of votes is : {total_num_votes}")
    # if republican electorate points are greater than the democrat electorate points, then republics win
    # else, democrats win
    if reps_electorate_points > dems_electorate_points:
            print(f"The Republicans win with {reps_electorate_points} electoral points!")
    elif dems_electorate_points > reps_electorate_points:
            print(f"The Democrats win with {dems_electorate_points} electoral points!")
    else:
            print('wow')

    if rigged_party:
        for state_num, state_data in master_state_map.items():
            print(f"state_num: {state_num}, this represents the item number in the dictionary.")
            print(f"state_data: {state_data}, this contains all the state data")
            # print(state_data)
            for key, value in state_data.items():
                if key == 'state':
                    print(f"state: {value}")
                elif key == 'num_voters':
                    print(f"num_voters: {value}")
                elif key == 'party':
                    print(f"party: {rigged_party}")
                    party = value
                elif key == 'votes':
                    print(f"votes: {value}")
                    total_num_votes += value
                elif key == 'electorate':
                    print(f"electorate: {value}")
                    if party == rigged_party:
                        rigged_electoral_points += value
                    elif party == "democrat":
                        rigged_electoral_points += value
                    elif party == "republican":
                        rigged_electoral_points += value
                    elif party == "libertarian":
                        rigged_electoral_points += value
                    elif party == "independent":
                        rigged_electoral_points += value


        print(f"The {rigged_party} party won with {rigged_electoral_points}!")

