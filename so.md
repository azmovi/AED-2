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
- apresentam uma int

6. Como o sistema operacional se comunica com o dispositivo canˆonico?
- 

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
