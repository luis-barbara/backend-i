a = 1
b = "a"
c = True
d = False

print(f"Hello world! {c}")

x = [1,2,3,4,5,6,"1",True, [1,2,3,4]]
print(x)

d = {1,2,3,4,5,1,1,1,1} # dicionario - neste caso é set, um set nao pode ter valores duplicados
print(d)

cenas = [1,2,3,4,5,1,1,1,1]
print(list(set(cenas)))

cenas = {1:2,2:2}
print(cenas)


arr = [100, 200, 300]
arr.sort(reverse=True)
print(arr)