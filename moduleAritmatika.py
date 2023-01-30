import Aritmatika

def main():
    a = int(input('Masukkan nilai a : '))
    b = int(input('Masukkan nilai b : '))

    print('a\t: %d' %a)
    print('b\t: %d' %b)

    print('a+b\t: %d' % Aritmatika.tambah(a, b))
    print('a-b\t: %d' % Aritmatika.kurang(a, b))
    print('axb\t: %d' % Aritmatika.kali(a, b))
    print('a/b\t: %d' % Aritmatika.bagi(a, b))

if __name__=="__main__":
    main()
