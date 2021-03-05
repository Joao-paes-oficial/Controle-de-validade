from app import Principal

x = Principal()
x.inserir_produto('001', 'Leite', 'Vaca', '05/03/2021')
x.inserir_produto('002', 'Água', 'Rio', '05/03/2021')
x.inserir_produto('003', 'Chocolate', 'Doce', '05/05/2021')
x.exibir_produtos()
x.excluir_produto('001', '05/03/2021')
x.exibir_produtos()