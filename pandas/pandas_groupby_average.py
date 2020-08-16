import pandas as pd

data = {'transit_time': [1,1,2,2,3,3],
        'orig_state': ['UT', 'UT', 'UT', 'UT', 'UT', 'UT'],
        'dest_state': ['CA', 'CA', 'AZ', 'AZ', 'NY', 'NY'],
        'GEOID': ['01', '01', '02', '02', '03', '03'],
        'dest_state_fn': ['California', 'California', 'Arizona', 'Arizona', 'New York', 'New York'],
        'dest_county_name': ['county1', 'county1', 'county2', 'county2', 'county3', 'county3']
       }
df = pd.DataFrame(data,columns=['transit_time', 'orig_state', 'dest_state', 'GEOID', 'dest_state_fn', 'dest_county_name'])

print(df)

df2 = df.groupby(['GEOID', 'dest_county_name']).agg(ave_transit_time=('transit_time', 'mean'), count=('GEOID', 'count'))

print(df2)
