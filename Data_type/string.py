from modulefinder import test


text = "help"
new_test = text.replace("e", "a") # we can also use same variable name to store the new value, but it is not recommended because it can cause confusion and make the code harder to read. It is better to use a different variable name to store the new value, so that it is clear what the variable represents and what it is used for.
print(new_test)
print(text[1:3])
var = "one"
vat2 = "two"
message = '{}+{} equals three'.format(var, vat2)
print(message)
message2 = f'{var.upper()} + {vat2.upper()} equals three'
print(message2)
print(dir(var))
print(var.__hash__())
print(var.zfill(10))
print(help(str.zfill))