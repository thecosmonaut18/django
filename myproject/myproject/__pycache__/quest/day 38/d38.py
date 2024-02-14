                    # DOLLAR SYMBOL
# import re
# txt="hello world"
# a=re.findall("[$d]",txt)
# print(a) 

# import re
# txt="Hell0o w0orld 1to Ame8rica"
# # a=re.findall("[a-z]",txt)
# # a=re.findall("[A-Z]",txt)
# # a=re.findall("[0-9]",txt)
# a=re.findall("[a-zA-Z0-9\s]",txt)

# print(a) 

                #SPECIAL SEQUENCE

# import re
# txt="He11llo @wO0RL1D"
# # a=re.findall("\s",txt)
# # a=re.findall("\S",txt)
# # a=re.findall("\d",txt)
# # a=re.findall("\D",txt)
# # a=re.findall("\w",txt)
# # a=re.findall("\W",txt)
# # a=re.findall("\AH",txt)
# # a=re.findall("D\Z",txt)
# print(a)


                #span group string

# import re
# txt="The rain in spain"
# x=re.search("spain",txt)
# print(x)
# print(x.span())
# print(x.string)
# print(x.group())



# import re
# txt="The rainb in spain"
# x=re.findall(r"\b",txt)
# # x=re.findall(r"\bs",txt)
# # x=re.findall(r"\bs\w+",txt)
# print(x)

# import re
# txt="The rain in spain"
# txt2="The rain in spain spn hai hellya spaaaaaaaaaaiiiiiiiiiiiiin spnn spainnn spin"
# # x=re.findall("sp..n",txt)
# # x=re.findall("sp.*n",txt2)
# # x=re.findall("sp.+n",txt2)
# x=re.findall("sp.{2}n",txt2)
# print(x)