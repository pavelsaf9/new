tool = 'Super-Puper MainTool /v2*'
tool_1 = tool[24]
tool_2 = tool[:5] + tool[16:20] + tool[21:24]
result = tool_1.center(20, '*')


print(result)
print(tool_2.center(20, '-').replace('2', '1').replace('/', ' '))
print(result)
