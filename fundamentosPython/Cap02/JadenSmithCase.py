def JScase(texto:str) -> str:
    """
    Docstring for JScase
    
    :param texto: String
    :type texto: str
    :return: String Com primeira letra maiúscula, exemplo: "oi blz" ->"Oi Blz"
    :rtype: str
    """

    palavras = texto.split() #
    JSCpalavras = [palavra.capitalize() for palavra in palavras]
    
    return ' '.join(JSCpalavras)


entrada_teste = "oi tudo bem essa é a entrada de Teste"
saida_teste = JScase(entrada_teste)
print (saida_teste )


 
 