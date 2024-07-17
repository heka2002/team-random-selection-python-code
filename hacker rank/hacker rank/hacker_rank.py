from numpy import *
class_A=['Espain','England','portogal','germany']
class_B=['Crotia','Italy','Belguim','Poland']
class_C=['Wales','Denmark','Iceland','Slovakia']
class_D=['Sweeden','Greece','Lativia','Albania']
random.shuffle(class_A)
random.shuffle(class_B)
random.shuffle(class_C)
random.shuffle(class_D)

for i in range(4):
    print("1)", class_A[i])
    print("2)", class_B[i])
    print("3)", class_C[i])
    print("4)", class_D[i])
    print("***************************")
