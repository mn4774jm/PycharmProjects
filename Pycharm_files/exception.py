#Exception handling

while True:
    try:

        small, large = input1()
        countingList, totalCount = processing(small, large)
        output1(countingList, totalCount)

    except Exception as err:
        print(err)