import pandas as pd
import datetime as dt

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # EDA
    #print(data.describe())

    # Convert columns to 
    #data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S' )#.dt.strftime('%Y-%m-%d %H:%M:%S')
    #data['lpep_dropoff_datetime'] = pd.to_datetime(data['lpep_dropoff_datetime']).dt.strftime('%Y-%m-%d %H:%M:%S')

    print(data.info())

    print(f"Preprocessing: rows with zero passengers {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero trip distance {data['trip_distance'].isin([0]).sum()}")
    data = data[(data['passenger_count'] != 0) & (data['trip_distance'] != 0)]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print(f"Total days of data: {len(data['lpep_pickup_date'].unique().tolist())}")
    #print(data.info())
    #print(data['VendorID'].unique().tolist())

    # Clean up column names
    print(data.columns.tolist())

    return data





@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'

@test
def test_vendorid(output, *args) -> None:
    assert len(output[~output['VendorID'].isin([1, 2])]) == 0, 'There are invalid vendor IDs'