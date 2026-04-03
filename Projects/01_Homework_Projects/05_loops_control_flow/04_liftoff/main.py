import time 

def main ():
    # for i in range(10, 0, -1):
    #     print(i, end=' ')
    # print("Liftoff!")


    for i in range(10, 0, -1):
        print(f"\r{i}", end="", flush=True)
        time.sleep(1)
    print("\rLiftoff!")

if __name__ == "__main__":
    main()
