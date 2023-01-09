from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    msg = 0
    for msg in messages:

        if msg['type']=='message':
            date=msg['date']
            # Get month from date

            if int(date[5:7])==month:
                count+=1


    return count

