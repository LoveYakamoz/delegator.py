import delegator

if __name__ == '__main__':
    c = delegator.run(['dir'], block=False)
    #c = delegator.run(['sleep', '3'], block=False)
    #c.std_out.write("yagnpei")

    c.out
