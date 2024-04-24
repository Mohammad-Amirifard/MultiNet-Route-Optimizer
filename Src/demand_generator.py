import random
import pandas as pd


def demand_generator(nodes):

    data_rate = [100, 400]
    random_demands_list = []

    while len(random_demands_list) < 20000:
        random_source = random.choices(nodes, k=1)
        random_destination = random.choices(nodes, k=1)
        random_data_rate = random.choices(data_rate, k=1)

        # check if source is different form destination
        if random_source != random_destination:
            # add random parameters to the list
            random_demands_list.append([1, random_data_rate[0], random_source[0], random_destination[0]])

    random_demands_df = pd.DataFrame(random_demands_list, columns=['no_demands', 'data_rate', 'source', 'destination'])
    random_demands_df.to_csv('random_demands.csv', index=False, header=True)


demand_generator([0,1,2,3,4,5,6,7])


