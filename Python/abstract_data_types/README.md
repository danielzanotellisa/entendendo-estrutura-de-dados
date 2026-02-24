# Tipos abstratos

- Como descrito no livro, os tipos abstratos são *interfaces* (contratos) que estabelecemos com o usuário para posteriormente usarmos uma DS e sua implementação
- Podemos ter 3 niveis de detalhamento quando falamos de ADT e DS:
    1. O nível ADT: apenas estabelecemos como o ADT funciona, quais as funções básicas e o seu comportamento
    2. O nível DS: aqui ja começamos a nos preocupar com a forma em que as coisas vão funcionar, qual DS iremos utilizar, etc.
    3. O nível de implementação: aqui nós iremos aplicar de fato a estrutura de dados em forma de código, assim conseguindo atingir o resultado final
- Uma ADT pode servir de abstração para vários tipos de DS, por exemplo, uma ADT `CONTÊINER` pode ser implemntada com um array, um array dinâmico, uma SLL ou DLL. Desde que seja possível inserir, percorrer e remover itens, nós temos um `CONTÊINER`
