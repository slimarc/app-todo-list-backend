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

##### BODY raw

```
{
   "Titulo": "Testando",
   "Completado": false
}
```

## PUT

Executa a leitura de uma tarefa já existente e insere as alterações. Perceba que é necessário incluir o id correspondente a tarefa à URL.

```
http://localhost:8000/api-auth/id_tarefa/
```

##### BODY raw
 
```
{
   "id": 6,
   "Titulo": "Testando",
   "Completado": false
}
```

## DEL

Executa a exclusão da tarefa.

```
http://localhost:8000/api-auth/delete/id_tarefa
```

## O que me ajudou :link::

Além dos links disponibilizados, utilizei algumas outras fontes que me ajudaram a desenvolver este backend e integrar ao frontend. 

-  [Integrate Django Rest API to Angular](https://www.youtube.com/watch?v=evihDSZuO70)
-  [Services](https://jacksongomesbr.gitbooks.io/desenvolvimento-web-front-end-com-angular/content/servicos.html)
-  [Django Cors Headers](https://pypi.org/project/django-cors-headers/)
-  [To-Do List API using Django Rest Framework](https://www.youtube.com/watch?v=G_IyMUm7Za0&t=1095s)
-  [Como documentar API usando o Postman](https://onebitcode.com/documentar-api-postman/)


## Postman :triangular_flag_on_post::

-  [Documentação postman](https://documenter.getpostman.com/view/23048135/VUxKSUdQ#intro)

## Tecnologias :rocket::

<div>
    <img height="60" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"/>
    <img height="70" width="90" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg"/>     
</div>

## Autor :wave::
Ricardo Lima | Estudante de desenvolvimento
<div>
    <a href="mailto:sricardolimaa@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"target="_blank"></a> 
    <a href="https://www.linkedin.com/in/slimarc/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
</div>
