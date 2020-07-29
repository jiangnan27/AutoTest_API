a = "{\"content-type\": \"application/json\",\"access-token\": \"${my_getattr(\"access-token\")}}"


b = a.split("${my_getattr(\"access-token\")}")


print(b)

bb = b[0][-1]
bbb = b[1][0]

if bb != "\"" and bbb != "\"":
    print(1111)


