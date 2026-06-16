# Relatório do Teste de Mutação

## Objetivo

Verificar se o teste E2E consegue detectar um erro inserido propositalmente na aplicação.

---

# Bug inserido

O teste altera temporariamente o arquivo:

```python
app/graphql_schema.py
```

Originalmente, o GraphQL busca todos os posts cadastrados no banco de dados utilizando:

```python
posts = db.query(PostModel).all()
```

Durante o teste de mutação, essa linha é substituída por:

```python
posts = []
```

Com essa alteração, o GraphQL deixa de consultar o banco de dados e passa a retornar sempre uma lista vazia, como se não existisse nenhum post cadastrado.

Na prática, esse bug faz com que a API GraphQL informe que não existem posts, mesmo que eles tenham sido criados corretamente pela API REST.

O objetivo é verificar se o teste E2E consegue identificar esse comportamento incorreto.

---

# 1. Localiza o arquivo

```python
arquivo = Path("app/graphql_schema.py")
```

Localiza o arquivo onde será aplicada a mutação.

---

# 2. Guarda o código original

```python
codigo_original = arquivo.read_text(...)
```

Lê e salva o conteúdo original do arquivo.

Isso permite restaurar o código ao final do teste.

---

# 3. Aplica a mutação

```python
codigo_mutado = codigo_original.replace(...)
```

Substitui a consulta ao banco pela lista vazia.

É nesse momento que o bug é inserido.

---

# 4. Salva o código alterado

```python
arquivo.write_text(codigo_mutado)
```

Grava o arquivo contendo a mutação.

A partir desse momento, o GraphQL passa a apresentar o comportamento incorreto.

---

# 5. Executa o teste E2E

```python
resultado = subprocess.run(...)
```

Executa automaticamente o teste E2E.

Esse teste realiza todo o fluxo da aplicação:

* Cria um post pela API REST.
* Consulta o post pelo GraphQL.
* Atualiza o post.
* Consulta novamente.
* Exclui o post.
* Confirma a exclusão pelo GraphQL.

---

# 6. Analisa o resultado

```python
if resultado.returncode != 0:
```

Se o E2E falhar:

```
Resultado do E2E: FAILED (esperado)
Conclusão: O E2E detectou o bug.
```

Isso significa que o teste percebeu que o GraphQL não retornou os dados corretamente.

Caso contrário:

```
Resultado do E2E: PASSED (não esperado)
Conclusão: O E2E NÃO detectou o bug.
```

Isso indicaria que o teste E2E não está validando corretamente o comportamento da aplicação.

---

# 7. Restaura o código original

```python
arquivo.write_text(codigo_original)
```

Após finalizar o teste, o código original é restaurado automaticamente.

Assim, a aplicação volta ao seu funcionamento normal.

---

# Conclusão

O bug simulado faz o GraphQL retornar uma lista vazia, mesmo existindo dados no banco de dados.

Como o teste E2E cria um post e depois tenta encontrá-lo pelo GraphQL, ele falha ao perceber que o post não foi retornado.

Isso demonstra que o teste E2E conseguiu detectar a mutação inserida e validar corretamente o fluxo completo da aplicação.
