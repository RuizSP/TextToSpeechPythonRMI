import Pyro4

Stream = Pyro4.Proxy("PYRONAME:servidor.Fala@172.25.5.216:9090")

def main():
    texto = input("Digite seu texto aqui: ")
    language = input("Digite pt-br")
    Stream.textReceiver(texto,language)


if __name__ == "__main__":
    main()