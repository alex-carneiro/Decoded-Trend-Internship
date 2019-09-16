# Decoded-Trends-Internship

Testes práticos para candidatos a estagiário na Decoded Trends.

Os testes consistem de 5 problemas, os quais correspondem a 5 funções escritas em Python com as respectivas soluções.

As funções devem ser implementadas no arquivo **decoded_intern.py**, caso considere útil, novas funções podem ser implementadas.

As soluções entregues serão avaliadas quanto à clareza do código, coerência da lógica e qualidade dos comentários.

Utilize o framework de teste PyTest e o arquivo *teste.py* para verificar seu andamento. Mesmo que alguma função não passe nos testes, não significa que esteja errada.

### 1. Primeiro problema

A função **decoded_numbers(x)** tem o parâmetro *x* (int) como entrada, o qual pode ser qualquer valor inteiro. Para um dado valor de *x*, esta função deve retornar o resultado corresponde na sequência:

decoded_numbers(1) = 1, decoded_numbers(2) = 2/3, decoded_numbers(3) = 3/5, decoded_numbers(4) = 4/7, ...

Caso o número fornecido não seja inteiro ou seja menor que 1, a função deve retornar *None*.

Exemplo:

```python
>>> x0 = 1
>>> valor = decoded_numbers(x0)
>>> print(valor)
1.0
>>> x1 = 2
>>> valor = decoded_numbers(x2)
>>> print(valor)
0.6666666666666666
>>> x_invalido = -2
>>> teste = decoded_numbers(x_invalido)
>>> print(teste)
None
```

### 2. Segundo problema

A função **decoded_strings(s)** tem o parâmetro *s* (string) como entrada, o qual corresponde ao nome de um produto em um site de e-commerce. A string *s* pode conter quaisquer caracteres e esta função deve retornar uma string correspondente à entrada, porém apenas com letras minúsculas, números e underlines.

Exemplo:

```python
>>> s1 = "Decoded Trends!"
>>> resultado1 = decoded_strings(s1)
>>> print(resultado1)
decoded_trends
>>> s2 = "Mais não é melhor # 100"
>>> resultado2 = decoded_strings(s2)
>>> print(resultado2)
mais_nao_e_melhor_100
>>> s3 = "Bem-te-vi 123/4"
>>> resultado3 = decoded_strings(s3)
>>> print(resultado3)
bem_te_vi_123_4
>>> s4 = "Caçador lá (008)"
>>> resultado4 = decoded_strings(s4)
>>> print(resultado4)
cacador_la_008
>>> s5 = "(@#%#)"
>>> resultado5 = decoded_strings(s5)
>>> print(resultado5)

```

### 3. Terceiro problema

A função **decoded_file(filename)** tem o parâmetro *filename* (string) como entrada, o qual consiste em um dos arquivos *file1.txt* ou *file2.txt*. Esta função deve retornar quatro listas com as strings que estão no arquivo especificado. As listas devem ser tais que a primeira contém as strings que começam com vogais, a segunda contém as strings que começam com consoante, a terceira contém as strings que começam com número e a quarta contém as strings que começam com quaisquer outros caracteres.

Exemplo:

```python
>>> lista1, lista2, lista3, lista4 = decoded_file('files/file.txt')
>>> print(lista1)
['abc', 'abrttrd', 'e3242']
>>> print(lista2)
['GGG;', 'pHGCY56156', 'q++']
>>> print(lista3)
['77?17', '0,nnbi']
>>> print(lista4)
['@!11', '=,pqjdpd', '-32121']
```

### 4. Quarto problema

A função **decoded_json(jsonfile)** tem o parâmetro *jsonfile* (string) como entrada, o qual consiste em um dos arquivos *file1.json* ou *file2.json*. Esta função deve retornar um dicionário tal que as chaves sejam strings "n0", "n1", "n2", ... e os valores sejam os números contidos no arquivo JSON especificado.

Exemplo:

```python
>>> dicionario = decoded_json('files/file.json')
>>> print(dicionario)
{'n0': -8, 'n1': -1, 'n2': 4, 'n3': 17, 'n2': 56, 'n3': 90}
```

### 5. Quinto problema

A função **decoded_web(url, pattern)** tem os parâmetros *url* (string)  e *pattern* (string) como entrada, os quais correspondem à URL de um site na Internet e um padrão de busca, respectivamente. Esta função deve retornar um número inteiro que corresponde à quantidade de ocorrências da string *pattern* no site especificado.

Exemplo:

```python
>>> n_vezes = decoded_web('http://http://35.247.220.8/', 'ubuntu')
>>> print(n_vezes)
10
```

