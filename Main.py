import Pyro4

Stream = Pyro4.Proxy("PYRONAME:servidor.Fala")

def main():
    texto = input("Digite seu texto aqui: ")
    Stream.textReceiver(texto)


if __name__ == "__main__":
    main()