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
    msg=data['messages']
    a=0
    for i in msg:
        str1=i['date']
        if str1[5:7]==str(month):
            a+=1
    return a
x=fromJson('result.json')
print(get_post_month(x,10))

