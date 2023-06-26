# Virtualização

### Processo
#### Áreas da memória:
- **Text**: Código do programa e constantes.
- **Data**: Variáveis globais e estáticas.
- **Stack**: Parâmetros, endereço dos returns e variáveis locais.
- **Heap**: Área alocadas a pedido do processo (Ex: malloc).
#### Estado de um processo:
- **Executando**: Processo atual está executando.
- **Pronto**: Processo pronto para ser executado e sera chamado pelo _escalonador_.
- **Bloqueado**: Processo está suspenso, SO decide o que será feito com ele.
- **Nova**: Processo está sendo criado, estado para garantir que o _escalonador_ não o chame.
- **Morto**: Processo terminou.

### Escalonamento
#### Troca de Contexto:
- Armazena o estado atual do do processo e muda para algum processo armazenado anteriormente.
- Razões:
    - processo termina.
    - seu tempo de execução terminou e outro processo que esta pronto vai rodar.
    - hardware necessita de ajuda e interrompe o processo atual.
#### Política de Escalonamento
- Determina qual é processo deve ser executado.
- Principais pontos:
    - **Utilização**: qual fração do tempo a CPU está executando um processo.
    - **Tempo de retorno**: tempo desde da criação do processo até sua finalização.
    - **Tempo de resposta**: tempo desde de se tornar pronto até ser agendado.
    - **Equidade**: todos os processos recebem a mesma quantidade de CPU.
    - **Progresso**: permitir que os processos avancem.
#### Não Preemptivo:
- Processo **não** pode ser dividido e executado em tempos diferentes na CPU.
###### First In First Out (FIFO):
- Lista de processos sem prioridade.
- Simples e por ordem de chegada.
###### Shortest Job First (SJF):
- Tarefas com o menor tempo de execução tem prioridade.
- Sistema pouco justa. 
#### Preemptivo:
- Processo pode ser dividido e executado em tempos diferentes na CPU.
###### Shortest Time to Completion First (STCF):
- Parecido com o SJF, entretando um processo muito grande que chegou primeiro
pode ser dividido para que um processo de custo menor ocorra primeiro.
- Sistema menos justo ainda.
###### Round Robin (RR)
- Cada processo recebe um pequeno intervalo de tempo (**_quatum_**) para ser executado
- Compartilhamento justo.
###### Multi Level Feedback Queue (MLFQ)
- Baseado em múltiplas filas de prioridade
- Todo processo é mandado para uma fila de alta prioridade, se o **_quatum_** não 
for concluído nesse espaço de tempo ele é jogada para uma fila de menor prioridade.
- Níveis superiores tem **_quantum_** menores, e quando se vai descendo o nível esse
quatum aumenta.

###### Completely Fair Scheduler (CFS)
- Tempo de execução virtual: Seu tempo de execução real em relação ao número 
total de tarefas em execução
- São feito em todos os processos na fila de execução simultaneamente.
- Calcula a fração de todos os processos do seu tempo ideal pelo o tempo total 
ideal e os mantem em uma árvore rubro-negra.
- O processo com a maior fração é agendado para execução e assim por diante.

DUVIDA(como é feita a preempção desses processos depois.)


