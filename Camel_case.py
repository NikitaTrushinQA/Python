#Нужно написать функцию, которая переделывает строку в camelCase,
#где все слова начиная со 2го идут без пробелов и других разделителей с большой буквы.
#Первое же слово будет с большой только если в изначальной строке оно было с большой.
#Строка на входе будет разделена дефисами и нижними подчеркиваниями. Примеры в задаче там сверху

#Python
def Camel_case(string):
    new_string =string.replace('-',' ')
    new_string=new_string.replace('_', ' ')
    result = new_string.title()
    result= result.replace(' ','')
    result=result.replace(result[0],string[0])
    return result

#print(Camel_case("The-stealth-warrior"))
#print(Camel_case("the-stealth_warrior"))

