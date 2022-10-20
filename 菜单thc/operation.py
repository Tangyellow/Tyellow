from menu import menu1
from menu import addMember

def printMenu():
    print("这是本店的菜单")
    for i in menu1:
        print(i,menu1[i])
    print("请问你要使用下列的哪个选项：1.添加 2.删除 3.退出")
def addMenu(addition):
    global addMember
    menu1[str(addMember)]=addition
    addMember+=1
def cutMenu(cutFood):
    global addMember
    if(cutFood in menu1 and addMember>=1):
        addMember -= 1
        for i in range(int(cutFood),addMember):
            menu1[str(i)]=menu1[str(i+1)]
        del menu1[str(addMember)]
    else:
        print("菜单里并没有您要删的菜的序号")
