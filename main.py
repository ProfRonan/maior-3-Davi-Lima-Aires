"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    x = float(input('Digite um número.'))
    y = float(input('Digite outro número.'))
    z = float(input('Digite mais um número.'))
    print(f'{max(x,y,z)}')



    
if __name__ == '__main__':
    main()
