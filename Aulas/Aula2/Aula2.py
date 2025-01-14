"""
Módulo 2 Codecademy

1. Creating an Instance
Iremos utilizar python shell para criar instâncias dos models. The Python Shell é um CLI que inicia um interpretador
python que utilizaremos para executar CRUD's Functionalities

Utilizamos rodando o seguinte: pyhon3 manage.py shell

Para trabalharmos com nossos modelos no python shell devemos importá-los da mesma maneira que em um arquivo python

>>> from app_name.models import ModelName

Com nosso Model importado, podemos começar a criar instâncias. Vamos supor que estamos criando um website como twitter
que tem um Post model com os fields title e description. Para criar uma instância disso devemos chamar nosso modelo
e preencher os campos:

post_instance = Post(title = "New", description="My Post")

Criamos nossa instância, agora precisamos salvá-la na nossa database chamando:
>>> post_instance.save()

Com nossa instância feita, podemos sair com o comando exit()
"""

owner_instance = Owner(first_name = "Vint", last_name = "Kahn", phone = "951-262-3062")

"""
2. Reading Instances

Poder ler Instâncias de um Model pode nos dar mais informações sobre o que está sendo armazenado na database e o formato
dos nossos dados. Quando queremos ver todas as instâncias de um modelo, podemos rodar o comando .all() method
eX:
>>> every_instance = ModelName.objects.all()
Isso irá retornar toda instância do model, vai parecer com isso:
>>> every_instance
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>

Nosso código nos retorna um QuerySet, uma coleção de objetos do nosso banco de dados. Nessas duas instâncias,
cada instância é associada com um ID. Devemos também saber que uma QuerySet é indexável, ou seja, podemos selecionar
as instâncias por index

ex:
>>> every_instance[0]
<ModelName: object (1)>

"""

"""
3. Updating an Instance

Para ver o valor de um campo de uma instância, podemos utilizar dot notation

ex:

>>> first_instance.name
'Asiqur'


Se quisermos mudar:
>>> first_name.name = "Ruqisa"

>>> first_instance.name
'Ruqisa'


E devemos salvar:
>>> first_instance.save()
"""

"""
4. Deleting an Instance

>>> first.instance.delete() 
Esse método excluirá a instância guardada em first_instance, mas se quisermos deletar tudo que está relacionado com
essa instância? Aqui é onde o .CASCADE vem, e nos salva muito tempo!

Podemos pensar no .CASCADE, como um efeito-dominó, quando usamos o .CASCADE para deletar um objeto, qualquer outro objeto 
que se referencie a ele também é deletado. Imagine que temos uma conta no Twitter, se excluirmos nossa conta, queremos também
que os posts sejam excluidos, certo? esse é um exemplo do efeito .CASCADE

.CASCADE Tem que ser implementado no nosso model e devemos prover o argumento. Vamos dizer que temos um Post Model

"""
class Post(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)


"""
5. The get() and get_or_create() method

o .get() method retorna um objeto que dá match com os argumentos que damos. Esse método deve ser estritamente 
utilizado se estivermos procurando valores únicos que retornam apenas uma instância. Se nossa Query retornar
múltiplos objetos, vamos receber um erro. E se não existir, também vamos receber um erro.

Ex:
>>> unique_instance = ModelName.objects.get(name="Ruqisa")
>>> unique_instance
<ModelName: ModelName object (10)>


o get_or_create() busca no banco de dados, mas caso não exista, ele cria o objeto com os argumentos providos
>>> wanted_object = ModelName.objects.get_or_create(title="example", content="jango")
>>> wanted_object
(<ModelName: ModelName object (15)>, True)


True se o objeto acabou de ser criado, False se não foi criado agora!


"""

"""
6. Additional Useful Querying Methods
o método .exclude() faz o exato contrário do .get(). Ao invés de retornar o objeto com o match de argumentos, ele retorna os que não
dão match.

ex:
>>> not_trucks = ModelName.objects.exclude(title="truck")
>>> not_trucks
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>


Outro método útil é .order.by(), que podemos ordenar nossa busca pelo ID, data de criação, etc.

ex:
>>> ordered_by_id = modelName.objects.order_by("-pk")
>>> ordered_by_id
<QuerySet [<ModelName: object (2)>, <ModelName: object (1)>]>


Podemos até retornar os objetos aleatoriamente:
>>> random_ordering = ModelName.objects.order_by("?")q

"""


"""
7. Querying Two Tables

As vezes vamos precisar mexer com duas tabelas ao mesmo tempo pois elas se conectam

Lembre-se, Foreign Keys podem conectar duas tables juntas através de uma relação one-to-many. Exemplo, imagine que tivessemos um model
Answer e um model Question. Uma Question Pode ter múltiplas Answers. Então, o Model Answer guarda uma foreign key do Question Model na sua
própria tabela

Vamos dizer que queremos retornar toda Answer que pertence a uma Question.
Podemos utilizar o .filter() method para olhar toda instância de Answer relacionada com essa Question

Primeiro precisamos é guardar a instância de Question em alguma variável, depois utilizarmos essa variável como argumento em um filter
na tabela Answer

Ex:
>>> question_instance = Question.objects.get(question="Is blue a color?") 
>>> Answer.objects.filter(question=question_instance)
<QuerySet [<Answer: No>, <Answer: Yes>, <Answer: It is a number>]>

"""

"""
8. Reverse Relationships

Se quisessemos fazer o contrário, achar todas as respostas relacioandas com uma Question? essa query é chamada de 
reverse relation, já que o relacionamento agora está o contrário, a table que esta fazendo a querying não contém a FK

para isso, devemos utilizar o set:

>>> question_instance.answer_set.all()

Por convenção, a propriedade _set é procedida por um lowercase do nome do Model.


"""
    