if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        dataframe

    This function converts column names from camel case to snake case.

    Example:
        If the input data has columns ['DOLocationID', 'PassengerCount'], this function will convert them to 
        ['do_location_id', 'passenger_count'].
    """

    column_names_old = data.columns.tolist()
    print(column_names_old)

    def camel_to_snake(camel_case_string):
        snake_case_string = ""
        for i, c in enumerate(camel_case_string):
            if i == 0:
                snake_case_string += c.lower()
            elif c.isupper():
                if i < len(camel_case_string) - 1 and camel_case_string[i + 1].islower():
                    snake_case_string += "_" + c.lower()
                else:
                    if camel_case_string[i - 1].islower():
                        snake_case_string += "_" + c.lower()
                    else:
                        snake_case_string += c.lower()
            else:
                snake_case_string += c.lower()
        return snake_case_string

    column_names_new = [camel_to_snake(x) for x in column_names_old]

    print([f"Old name: {x} - new name {y} \n"for x,y in zip(column_names_old, column_names_new)])
    data.columns = column_names_new

    return data


@test
def test_no_upper_cas_letters(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """

    s = " "
    assert s.join(output.columns.tolist()).islower() is True, 'There are uppercase letters in the columns'
