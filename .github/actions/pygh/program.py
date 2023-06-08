import os

def run():
    with open('Main.java') as f:
        lines = f.readlines()

    print('arquivo lido: ${lines}')


if __name__ == '__main__':
      run()