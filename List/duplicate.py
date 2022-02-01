
tu = tuple(input("Enter tuple separated by a space : ").split())
no_dul = list(tu)
t_l = no_dul.copy()
for i in range(len(tu)):
    if t_l.count(no_dul[i]) > 1:
        t_l.remove(no_dul[i])
tu = tuple(t_l)
print(tu)
