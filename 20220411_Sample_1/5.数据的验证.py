# coding:utf-8
print('所有字符都是数字(十进制的阿拉伯数字)')
print('123'.isdigit())
print('一二三'.isdigit())
# 罗马数字返回的也是False
print('ⅠⅡⅢ'.isdigit())
print('0b1001'.isdigit())

print('所有字符都是数字(包括阿拉伯数字,罗马数字等)')
print('123'.isnumeric())
print('一二三'.isnumeric())
print('ⅠⅡⅢ'.isnumeric())
print('壹贰叁'.isnumeric())
print('0b1001'.isnumeric())

print('所有字符都是字母(包括英文,中文等)')
print('hello你好'.isalpha())
print('hello你好123'.isalpha())
print('hello你好一二三'.isalpha())
print('hello你好ⅠⅡⅢ'.isalpha())

print('所有字符都是字母+数字')
print('hello你好123'.isalnum())
print('hello你好123...'.isalnum())
print('hello你好一二三'.isalnum())
print('hello你好壹贰叁'.isalnum())
print('hello你好ⅠⅡⅢ'.isalnum())

print('所有字符都是小写字母,中文不分大小写')
print('helloword'.islower())
print('Helloword'.islower())
print('helloword你好'.islower())

print('所有字符都是大写字母,中文不分大小写')
print('HELLOWORLD'.isupper())
print('hELLOWORLD'.isupper())
print('HELLOWORLD你好'.isupper())

print('单词字符是首字母大写')
print('Hello'.istitle())
print('HelloWorld'.istitle())
print('Hello World'.istitle())
print('Helloworld'.istitle())
print('Hello world'.istitle())

print('所有字符都是空白字符')
print('\t'.isspace())
print('  '.isspace())
print('\n'.isspace())
