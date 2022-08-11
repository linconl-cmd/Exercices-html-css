programa
{
	
	funcao inicio()
	{
		cadeia funcionario
		inteiro janeiro,fevereiro,marco,abril,vendast,mvendas

		escreva("Digite o nome do funcionario: ")
		leia(funcionario)

		escreva("Digite a qntd. de venda em Janeiro: ")
		leia(janeiro)
		escreva("Digite a qntd. de venda no Fevereiro: ")
		leia(fevereiro)
		escreva("Digite a qntd. de venda no Março: ")
		leia(marco)
		escreva("Digite a qntd. de venda no Abril: ")
		leia(abril)

		vendast=(janeiro+fevereiro+marco+abril)

		mvendas=vendast/4
		
		escreva( funcionario +" o seu total de vendas de Janeiro á Abril é de: " + vendast + ", e a media ficou em: " + mvendas)
		
		
		
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 180; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */