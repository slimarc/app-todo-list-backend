<h1 align="center">Backend To-Do List 📑</h1>

## Sobre 🔎:

<p align="justify">Um aplicativo to-do list faz o gerencimento de tarefas, nele você pode inserir, editar ou excluir uma tarefa, além de poder marcá-la como completada. O backend desta api foi desenvolvido com Django Rest que é um framework web Phyton.</p>

## Requisitos :blue_book::

- Exibir a lista de TODOs;
- Adicionar novos TODOs;
- Remover TODOs;
- Editar TODOs;
- Marcar TODO como completo;
- A aplicação deveria conversar com o backend via JSONs.

## GET 

Executa a lista de tarefas.

```
http://localhost:8000/api-auth
``` 

## POST

Executa a criação de novas tarefas.

```
http://localhost:8000/api-auth/create
``` 

### BODY raw

```
{
   "Titulo": "Testando",
   "Descricao": "",
   "Data": "2022-08-26",
   "Completado": false
}
```

## PUT

Executa a leitura de uma tarefa já existente e insere as alterações. Perceba que é necessário incluir o id correspondente a tarefa à URL.

```
http://localhost:8000/api-auth/id_tarefa/
```

### BODY raw
 
```
{
   "id": 6,
   "Titulo": "Testando",
   "Descricao": "Adicionando informações",
   "Data": "2022-08-26",
   "Completado": false
}
```

## DEL

Executa a exclusão da tarefa.

```
http://localhost:8000/api-auth/delete/id_tarefa
```

## O que me ajudou:

Além dos links disponibilizados, utilizei algumas outras fontes que me ajudaram a desenvolver este backend e integrar ao frontend. 

- <p><a href="https://www.youtube.com/watch?v=evihDSZuO70" target="_blank"></p>
- <p><a href="https://jacksongomesbr.gitbooks.io/desenvolvimento-web-front-end-com-angular/content/servicos.html" target="_blank"></p>
- <p><a href="https://pypi.org/project/django-cors-headers/" target="_blank"></p>
- <p><a href="https://www.youtube.com/watch?v=G_IyMUm7Za0&t=1095s" target="_blank"></p>
- <p><a href="https://onebitcode.com/documentar-api-postman/" target="_blank"></p>

## Autor 👨‍🎨:
Ricardo Lima | Estudante de desenvolvimento
<div>
    <a href="mailto:sricardolimaa@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"target="_blank"></a> 
    <a href="https://www.linkedin.com/in/slimarc/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
</div>
