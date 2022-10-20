import menu
import operation
def main():
    global menu1
    while True:
        operation.printMenu()
        try:
            answer1 = input()
        except:
            print("error!,请重新输入")
            continue
        finally:
            if (answer1 == "添加" or answer1 == "1"):
                operation.addMenu(input('请输入你要添加的菜'))
            elif (answer1 == "删除" or answer1 == "2"):
                 operation.cutMenu(input('输入你要删除的菜的序号'))
            elif (answer1 == "退出" or answer1 == "3"):
                print("已退出")
                break
            else:
                print("请输入已有的功能")
if __name__ == '__main__':
    main()
else:
    print("您正在用菜单模块")
    main()
