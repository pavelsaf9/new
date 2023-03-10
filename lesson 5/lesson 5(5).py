target_str = "38659296041780974788136902140185944280532444726389158259281259748" \
             "704707896928755068403238391628903785951500546"

print(sum([int(target_str[i:i+2]) for i in range(0, len(target_str), 2)]))



# total_sum = 0
#
# for i in range(0, len(target_str), 2):
#     total_sum += int(target_str[i:i+2])
#
# print(total_sum)
