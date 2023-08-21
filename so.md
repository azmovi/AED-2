## Drivers
1. Explique como o Sistema Operacional interage com dispositivos.
- Atraves do gerenciador de dispositivos.

2. Descreva o design moderno de drivers de dispositivo e como ele difere da abordagem
histórica.

3. Qual ´e a importˆancia da Northbridge e Southbridge em rela¸c˜ao ao suporte 
de hardware para dispositivos?
- Northbridge responsavel por gerenciar a comunicação de alta velocidade entre a
CPU e a memoria.
- Southbridge responsavel pelo gerenciamento de entrada/saida de menor velocidade
como portas usb, interfaces de rede entre outros
- Sao vitais para o suporte de hardware, pois faz a comunicação entre os dispositivos
e o processador.

4. Explique a importˆancia de suportar diferentes velocidades de barramentos para
dispositivos em um sistema.
- permite acomodar diferentes dispositivos com diferentes desempenhos, aumentando 
a compatibilidade e adaptação de mudanças futuras.

5. Explique a abstra¸c˜ao no funcionamento interno de um dispositivo canˆonico.
- Ele apresenta uma interface de hardware que permite o software do sistema controle
esse hardware. E apresenta a Estrutra Interna que implementa a abstração do Sistema
Operacional 

6. Como o sistema operacional se comunica com o dispositivo canˆonico?
- Ele apresenta 3 registradores, o de status que permite a leitura do statual atual
do dispositivo, o de comando que permite que comandos sejam enviados para ao dispositivo
e o de data que permite leitura ou gravação no dispostivo.
- Alem disso ocorre o propocolo de comuniação. Iniciando com o polling o SO verifica o
status do dipositivo em um loop ate que ele esteja pronto. Depois é enviado dados
pelos registadors de dados. Após isso ele é capaz de registrar o comando atrave do 
registrador de commandos onde ele vai trabalhar para executar, enquanto isso ocorre
a etapa de polling ja esta ocorrendo para verificar o termino o inicio de uma nova 
tarefa.

7. Descreva o problema com a abordagem de ‘spin‘ no protocolo do dispositivo
- representa a tecnica usada para verificar repetidamente o estado de um despositivo
até que uma condição seja atendida ele é feito por um loop (spin) curtos e frequentes,
entretando ela nao é eficaz devidio o dispercidio de cpu e o constumo de energia, 
alem do bloqueio

8. Quais s˜ao os benef´ıcios da comunica¸c˜ao ass´ıncrona em rela¸c˜ao ao 
protocolo do dispositivo?
- Representa um modelo em que as tarefas sao tratadas de forma independente,
permitem uma maior eficiencia, escalabilidade.

9. Como as interrup¸c˜oes melhoram a eficiˆencia da comunica¸c˜ao entre o CPU e o dis-
positivo?
-  as interrupções indicam que a cpu deve ter uma atençao imediata ao dispositivo
que enviou a interrupção. Eles sao fundamentais pois melhoram o tempo de reposta
quando eles priorizam eventos, fazendo com a cpu arrume os problemas de forma
hierárquica 

10. Descreva a diferen¸ca entre PIO (Programmed IO) e DMA (Direct Memory Access)
na transferˆencia de dados.
- PIO: A CPU é responsavel pela transferencia de dados entre dispositios de entrada/saida
e a memoria. Dessa forma a CPU controla as etapas de leitura, escrita e a transferencia
entre dispositivos e memoria.
- DMA: Não tem a intervenção da CPU na transferencia de dados entre os dispositivos
e a memoria. Dessa forma a CPU fica fazendo outras tarefas enquanto o DMA se preocupa
com a transfeerencia
- A DMA é preferevel devidido sua efeciencia e desemepnho, a PIO é usada quando se 
quer ter um controle precioso na hora da transferencia ou tambem na compatibilidade
dos dispostiivos.

11. O que s˜ao drivers e por que s˜ao importantes?
- Sao programas de software que fazem o meio de campo entre o hardware e sistema
operacional, apresentam uma interface padronizada para concetar a placa de som, 
a placa de rede entre outros, ele é a peça principal para o funcionamento adequado
desses elementos 

12. Por que ´e importante ter uma API bem projetada para os drivers?
- A API é importante porque ela influencia diretamente na usabilidade dos componetes,
eficiencia e na qualidade em geral do software, como escabilidade ou resolver problemas
que possam ocorrer no futuro.

13. Explique a diferen¸ca entre drivers de modo usu´ario e drivers de modo kernel.
- Drivers de modo usuario sao programas que iteragem com o hardware mas sao operadas
no espaço de usuario, dessa forma estao em um espaço mais isolado, ja que nao
apresetam prviligios que os drivers de modo kernel.
- Esses por sua vez são mais sensiveis a mudança pois apresetam mais privilegio,
pois tem acesso direito a recursos e podem executar operaçoes em nivel de sistema
tendo uma maior complexidade e risco.

14. Quais s˜ao os riscos associados `a instala¸c˜ao de drivers incompat´ıveis ou mal projeta-
dos?
- Ela pode acarredar em diversos problemas, dando instabilidade a todo o sistema
pois commandos nao conhecidos darao sobrecarga a CPU, alem de aumentar a disputa
com compontes que antes funcionavam normal, agora a CPU vai passar grande parte
do tempo tentar resolver poissivel interrupções do drive mal implementado

15. Como o agendamento de E/S difere do agendamento da CPU?
- A diferença está o agendamento de E/S se concentra na alocação eficiente dos
recursos de E/S afim de minimizar o tempo de espera do sistema, enquanto o agendamento
da CPU visa otimizar a alocação de processos em execução para garantir a eficiencia 
de multitarefas e o tempo de resposta deles.

16. Qual ´e a fun¸c˜ao do buffering na otimiza¸c˜ao de E/S?
- Ele ajuda na redução de sobrecarga do E/S, pois essa memoria adicional ajudar 
na transferecia de dados mais organizada. Alem disso ocorre um controle de fluxo
de dados logo sua banda larga pode ser utilizada com mais eficiencia 

17. Qual ´e a ideia principal por tr´as do RAID?
- Ele ajuda a melhorar a confiabilidade, desempenho e capacidade de armazenamento
, ele combina multiplos discos rigidos, aonde utiliza tecnicas de agrupamento dos
dados entre os discos, servindo na recuperação dados, melhoria no desempenho juntamente
com o aumento da capacidade.

18. Entre RAID 01 e RAID 10, qual ´e considerado mais confi´avel?
- o RAID 10 é considerado mais confiavel pois falhas individuais sao toleradas
devido o espelhamento mas mesmo que ocorram falhas simultaneas em um dos pares
espelhados o outro espelhamento ainda pode estar intacto garantindo a confiabilidade.

## Sistema de Arquivos.
1. Explique o principal objetivo de um sistema de arquivos e como ele gerencia os
blocos persistentes de um dispositivo de armazenamento
- O principal objetivo é fornecer uma estrutura organizada para armanezar, gerenciar
e recuperar dados de maneira eficiente. Para o gerenciamento ele divide os blocos 
de persistencia em blocos de tamanho fixo, cada bloco passa a ser uma unidade de
alocação e os dados sao armazeandos nesses blocos. Apos isso ele passa a um mapa
de rastreamente desses blocos, para saber quais estao livres e quais estao sendo 
utlizados.

2. Qual ´e a principal diferen¸ca entre arquivos tipados e n˜ao tipados?
- Arquivos tipados: sao armazenados de acordo com o seu formato, e o acesso a esses
arquivos ocrre de maneira mais segura e rigida.
- Arquivos nao tipados: sao armazneados de acordo com sua sequencia de bits e os 
dados sao interpredados de acordo com o que o programa lê, sendo assim mais dificil
interpretar o que esse arquivo realmente contem ou deseja mostrar.

3. Qual ´e a fun¸c˜ao de um inode em um sistema de arquivos?
- Ele é uma estrutura de dados que é responsavel por armazenar informaçoes e metadados
sobre o arquivo ou diretorio que ele está associado. Ele é responsavel por ajudar 
o sistema operacional a identificar arquivos sem a necessidade de pecorrer todo 
o sistema de arquivos. Eles ajudama organizar, identificar e gerenciar arquivos, 
contribuindo na eficiencia.

4. Descreva a hierarquia de I/O apresentada nos slides.
- hardware de disco: Os componentes como HD ou SSD, onde os dados sao fisicamente
armazenados.
- driver de dispositiov de disco: Um software de sistema que atual como interface 
entre o hardaware de disco e o sistema operacional. Onde gerencia as operações de
leitura e escrita das midias fisicas.
- acesso a arquivos: Lida com as operações de leitura e escrita de arquivos individuais
usando funçoes fornecidas pelo driver de disitivos para fazer as tarefas nos arquivos.
- acesso a diretorios: Envolve o gerenciamento de diretorios que contem os arquivos
onde o sistema operacional consulta os inodes dos arquivos presentes nesses diretorios,
ele apresenta funçoes de navgação criação exclsao e privilegios.
- nomeação: A atribuição de nomes exclusivos a diretorios e arquivos principal
metodo de refernciamento para o armzenamento.

5. Quais s˜ao as trˆes vis˜oes diferentes de um arquivo?
- Visao de nomeação: Responsalve na forma de como os arquivos sao identificaodos
e acessando por meio do seu nome 
- Visao conteudo: Responsavel nos dados armezados dentro dos arquivos, aborda 
como os dados sao organizdos e interpretados dentro de uma arquivo.
- Visao de Armazenamento: Resposavel pela representação fisica do arquivo dentro
dos dispositivos de armazenamento. Ela aborda como os dados esntao divididos nos
blocos.

6. Descreva a finalidade da tabela de inodes no contexto de sistemas de arquivos e
como ela relaciona-se com o armazenamento de dados
- ela é responsavel pelo gerenciamento dos arquivos armazenados no sistema de arquivos,
pois é responsavel por rastrearar informaçoes sobre os arquivos, a partir dos 
metadados que tem as identificações princiapais do arquivo, como o tipo permissões
tamanho, ponteiro para o bloco de dados. Dessa forma encontrando a localizaã no 
bloco de dados, dessa forma é mais rapido acessar onde o dado esta armazenado fisicamente
tendo conhecimento do seu ponteiro.
- Quando um arquivo é criado seu inode é alocado na tabela de inodes. Quando esse arquivo
é acessado ou modificado o sistema operacional consulta a tabela de inodes para 
acessar  onde encontrar esse arquivo fisicamente. Quando o arquivo é excluido o 
inode é marcado como livre para ser reutilizado.

7. Como ´e feito o mapeamento do nome de um arquivo at´e o seu respectivo inode?
- Arquivo criado o sistema operacional aloca o inode na tabela de inodes, esse arquivo
é registrado no direitorio corrente da sua criação. Quando ocorre um pedido de 
acesso ou manipulção desse arquivo, o sistema operacional consulta o direitorio 
e acha seu inode, com isso ele encontra os blocos de dados presente na memoria fisica
e assim atualiza o arquivo que foi modificado ou acessado.

8. Explique a utilidade das entradas especiais de diret´orio ’.’ e ’..’
- o ponto é usado para referenciar o direitorio atual, ja o dois pontos é para 
refrenciar o pai do direitorio atual, ou seja um nivel a cima do direitorio corrente.

9. Qual ´e a fun¸c˜ao de um descritor de arquivo e como ele se relaciona com a 
tabela de inodes?
- ele é usado para gerenciar o controlar a manipulação de arquivos ele é uma abstração
que pemrite os progamas acessem e iterajam com os arquvos e dispositiovs de entrada/saida
- A sua relaçao com a tabela de inodes ocorrendo quando um processo abre um arquivo
e ele é associado a um descritor de arquivos. Entao o sistema operacional consulta 
a tabela de inodes para saber encontrar esse inode e conseguir seus metadados.
Com isso o o descritor de arquivos contem o inode do arquivo que esta senod utlizado
pelo programa e tem a funçao de admisntrar esse uso do programa para com o arquivo.
como a posição atual dos ponteirose as permissões presentes. Quando o arquivo é 
fehcado o descritor  é liberado.

10. Descreva a fun¸c˜ao da chamada de sistema open e o que ela retorna.
- È uma operação fundamentl que permite com que programas possam abrir arquivos.
Ela estabelece uma relação entre um descritor de arquivos e o arquivo presnte no sistema 
de arquivos. Tornando possivel assim a leitura, esrita e manipulação do mesmo. O 
valor retornado de quando se usa a funçao open sera a posição na tabela de descritor d
de arquivo.

11. Explique a ausˆencia de uma chamada de sistema para exclus˜ao de arquivos e como
a exclus˜ao ´e tratada.
- È a forma como foi projeada o sistema UNIX, uma filosfia que nao existe a necessidade
de fazer uma exclusao propriamente dita. Para tratar esse problema é usada o sistema 
de unlink. Portanto para remover um dado deve-se retirar todos os links que fazem 
referencia a esse especificando que esse espaço esta livre para armazenar o dado
ou seja ocorre uma sobreescirta do dado.

12.O que acontece quando se altera as permiss˜oes de um arquivo ap´os ele ser aberto?
- Podem ser afetados em operações subsequentes do processo, devido a mudança de 
permissão, em muitos casos ele continuara a rodar podendo enfretar possiveis erros
de permissão

13.Como os sistemas de arquivos do Windows e Unix lidam com m´ultiplos sistemas de
arquivos?
- Unix: Aprensetam uma hierarqui de diretorios unicos e padronizados. Iniciandos
pelo diretorio barra onde todos os diretorios restantes sao montados com referncia
nesse diretorio inicial e os multiplos dretores sao montados com refrencia direita
ou indireta ao diretorio /.
- Windows: Apresenta sisteam de discos, onde eles nao apresentam relação entre si
e o sistema de arquivos subsequentes podem estar onde desejarem

14. Explique a diferen¸ca entre links r´ıgidos e links suaves.
- Links rigidios: contem o mesmo inode do arquivo que foi referenciado, é basicamente
o mesmo arquivo apenas com outro nome e nao podem apontar para diretorios. Mudança
no conteudo a partir de um link vai fazer a mudança do arquivo orginal.
- Lins suaves: O link aponta para o caminho do arquivo de destino, e nao mais o 
inode, quando voce fizer o acesso voce vai entrar no arquivo atrasves do path presente
nesse link simbolico

15. Como um sistema de arquivos identifica um arquivo internamente e externamente?
- Arquivo interno: a identificão intera ocorre atrasves dos inodes que sao as estruturas
de dados criadas para guardar as princiapis infoações do arquivo sem tteer seu conteudo
propriamente dito.
- Arquivos externos: A sua indenficação é feita atasves dos nomes dos arquivos,
dessa forma o usario procura de forma mais simplificada e abstrata

16. Diferencie entre sistemas de arquivos baseados em FAT, NTFS e ext4
- FAT: Usado principalmente em usb e carao de memoria

17. Como a fragmenta¸c˜ao afeta a performance de um sistema de arquivos e como pode
ser mitigada?
- Fragmentação e quando os dados nao estao armazeados de maneira contigua, dessa forma
o acesso a infomação sera mais lento, alem de um despedicio de espaço, deivido 
o fato deles serem alocados em tamanho fixo, e pode ter blocos que nao foram complemtanete 
preechidos, e por ultimo um desgaste no disco fisico pois tera que fazer mais acessos
para encontrar todos os dados presentes em um determiado arquivo.
- Existe formas de mitigar isso, sendo elas a desgramenação que é o procesos de reoganizar
os dados presentes, presença de arquivos jornaldos.


## Otimização
1. xplique o desafio associado `a atualiza¸c˜ao atˆomica de arquivos. Por que a vers˜ao
antiga deve permanecer se o aplicativo ou sistema falhar?


