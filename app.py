from modelos.restaurante import Restaurante

restaurante_gopala = Restaurante('Gopala', 'Indiano')
restaurante_gopala.receber_avaliacao('Carlos', 5)
restaurante_gopala.receber_avaliacao('Ana', 4)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
   