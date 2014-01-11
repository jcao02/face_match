from subprocess import Popen


def main():
    """docstring for main"""
    f = open("out", "w")
    p = Popen(["./random","42"], stdout=f)
    code = p.wait()
    f.flush()
    with open('out') as f:
        for lines in f:
            x = int(lines)
            print x



if __name__ == "__main__":
    main()
