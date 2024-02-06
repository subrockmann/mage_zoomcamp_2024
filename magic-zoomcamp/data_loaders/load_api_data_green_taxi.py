import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    urls = [
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz',
    ]


    taxi_dtypes = {
        'VendorID' : pd.Int64Dtype(),

        'passenger_count' : pd.Int64Dtype(),
        'trip_distance' : float,
        'RatecodeID' : pd.Int64Dtype(),
        'store_and_fwd_flag' : str,
        'PULocationID' : pd.Int64Dtype(),
        'DOLocationID' : pd.Int64Dtype(),
        'payment_type' : pd.Int64Dtype(),
        'fare_amount' : float,
        'extra' : float,
        'mta_tax' : float,
        'tip_amount' : float,
        'tolls_amount' : float,
        'improvement_surcharge' : float,
        'total_amount' : float,
        'congestion_surcharge' : float,
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    total_df = pd.DataFrame()

    for url in urls:

        df = pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        total_df = pd.concat([total_df, df], ignore_index=True, sort=False)

    #time_format = '%Y-%m-%d %H:%M:%S'

    #total_df.lpep_pickup_datetime = total_df.lpep_pickup_datetime.apply(lambda d: datetime.datetime.fromtimestamp(d.timestamp()).strftime('%Y-%m-%d %H:%M:%S'))
    #total_df['lpep_pickup_datetime'] = pd.to_datetime(total_df['lpep_pickup_datetime']).dt.strftime('%Y-%m-%d %H:%M:%S')
    #df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    #, unit = "ms") # , format=time_format)
    #print(type(total_df['lpep_pickup_datetime'][0]))
    #total_df['lpep_pickup_datetime'] = total_df['lpep_pickup_datetime'].dt.time# .apply(lambda x: dt.datetime.utcfromtimestamp(int(x)))#.strftime('%Y-%m-%dT%H:%M:%SZ'))
    #pd.to_datetime(total_df['lpep_pickup_datetime'].astype(int))#, unit ="s")
    print(total_df.info())

    return total_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

