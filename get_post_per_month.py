from read_data import fromJson


def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    count = {
        12:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
        6:0,
    }
    messages = data['messages']
    for msg in messages:
        if msg['type']=='message':
            date=msg['date']
            count[int(date[5:7])]+=1
    return count
file_path = "data/result.json"
data = fromJson(file_path)
count = get_post_per_month(data)
print(count)
