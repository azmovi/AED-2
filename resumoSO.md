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
