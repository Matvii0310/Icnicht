# my_list="1"
# iterator = iter(my_list)
# print(iterator)
#
# for elem in iterator:
#     print(elem)
# for elem in iterator:
#     print(elem)


# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
# count = Counter(7)
# # for elem in count:
# #      print(elem)
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(next(count))
# # print(iter(count))
# print(next(count))
# print(next(count))


# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
# res = raise_to_the_degrees(5, 50)
# # print(res)
# for _ in res:
#     print(_)
# print("new execution")
# for _ in res:
#     print(_)


# def raise_to_the_degrees(number):
#     i=0
#     while True:
#         yield number**i
#         i+=1
# res = raise_to_the_degrees(122345)
# print(res)
# for _ in res:
#     print(_)
#     print()


# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}." \
#                f" Afterwards I will help you with {work}"
# helper = Helper("homework")
# print(helper("cleaning"))
# print(helper("eating"))

# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. " \
#                f"Afterwards I will help you with {work}"
#     return helper
#
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

#
# def checker(function, *args, **kwargs):
#     try:
#         result = function(*args, **kwargs)
#     except Exception as exc:
#         print(f"We have problems {exc}")
#     else:
#         print(f"No problems. Result – {result}")
#     return checker
# def calculate(expression):
#     return eval(expression)
# calculate = checker(calculate)
# calculate("2+2")

# checker(calculate,"(2+2*2)/4")


# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(f"We have problems {exc}")
#         else:
#             print(f"No problems. Result – {result}")
#     return checker
#
# @checker
# def calculate(expression):
#     return eval(expression)
#
# calculate("2+2")


def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_types) as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result – {result}")
        return checker
    return checker
@checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
 return eval(expression)
expr=input("Введите ваш пример")
calculate(expr)