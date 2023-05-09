#In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

#For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

#Your function will be tested with pre-made examples as well as random ones.




def my_function(list_a, list_b):
    #
    volumeA = 1
    volumeB = 2
    for num in list_a:
        print(num)
        volumeA*=num
    print(volumeA)

print(my_function([2, 2, 3], [5, 4, 1]))



#################################################




def my_function(list_a, list_b):
    volumeA = 1
    volumeB = 2
    for num in list_a:
        print(num)
        volumeA*=num
    print(volumeA)
    for num in list_b:
        volumeB*=num
    print(volumeB)
    return abs(volumeB - volumeA)
    

print(my_function([2, 2, 3], [5, 4, 1]))







