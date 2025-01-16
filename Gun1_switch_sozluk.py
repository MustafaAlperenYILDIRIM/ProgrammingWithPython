def languages(x):
    switch={
        "Java":"you can become web developer",
        "Python":"you can become data scientist",
        "C":"you can become hardware programmer",
    }
    return switch.get(x)


x = input("Python||Java||C dillerinden hangisini öğrenmek istiyorsunuz: ")
print(languages(x))



