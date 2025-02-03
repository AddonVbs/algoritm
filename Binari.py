arr = [1,2,3,4,5]

def binari_serch(arr_user,user_serch):
    low = 0
    high = len(arr_user)
    
    for i in range(len(arr)):
        mid = (low+high)//2 #отсикаем половину чтоб получить средние число и угадывать
        gess = arr_user[mid]
        if gess==user_serch:
            return mid
        
        if gess > user_serch:
            high=mid-1
        if gess < user_serch:
            low = mid+1
        if user_serch > len(arr_user):
            return None
        
print(binari_serch(arr,5))