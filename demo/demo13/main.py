# import mon_module

# print("mon programme principal")

# print(mon_module.VERSION)
# print(mon_module.saluer("tutu"))

from mon_module import addition , VERSION

print(addition(6,7))
print(VERSION)


from mon_module import saluer as s

saluer = "toto"
print(s("tata"))




