### Quebra-Cabeça dos 8 - Solucionador com Interface Gráfica

Este repositório contém um programa que resolve o clássico **Quebra-Cabeça dos 8** (8-Puzzle) utilizando o algoritmo **A*** (A-star) com uma interface gráfica interativa desenvolvida em **Pygame**. O objetivo do jogo é reorganizar os números em um tabuleiro 3x3, movendo o espaço vazio (representado pelo número 0) até que os números estejam na ordem correta.

### Funcionalidades Principais

1. **Interface Gráfica Interativa**:
   - O usuário pode escolher entre **criar manualmente** um estado inicial ou **gerar um estado aleatório**.
   - O programa verifica se o estado inicial é solucionável antes de tentar resolver o quebra-cabeça.
   - Exibe a solução passo a passo, mostrando os movimentos necessários para chegar ao estado final.

2. **Algoritmo A***:
   - Utiliza a **heurística de Manhattan** para calcular a distância entre o estado atual e o estado final, garantindo uma solução eficiente.
   - Retorna o caminho mais curto para resolver o quebra-cabeça.

3. **Verificação de Solubilidade**:
   - O programa verifica se o estado inicial é solucionável antes de tentar resolver o quebra-cabeça. Caso contrário, informa ao usuário que o estado não tem solução.

4. **Visualização Dinâmica**:
   - O tabuleiro é renderizado com um estilo 3D e cores dinâmicas que mudam conforme o progresso da solução.
   - Botões interativos permitem ao usuário escolher entre criar um estado manualmente ou gerar um aleatório.

### Como Usar

1. **Executar o Programa**:
   - Execute o arquivo `main.py` para iniciar a interface gráfica.
   - Escolha entre **"Criar Estado"** para definir manualmente o estado inicial ou **"Gerar Estado"** para obter um estado aleatório.

2. **Criar Estado Manualmente**:
   - Clique nas células do tabuleiro para inserir os números de 0 a 8.
   - O programa verificará se o estado é solucionável antes de prosseguir.

3. **Gerar Estado Aleatório**:
   - O programa gera automaticamente um estado inicial válido e solucionável.

4. **Visualizar a Solução**:
   - O programa exibirá a solução passo a passo, mostrando os movimentos necessários para chegar ao estado final.

### Requisitos

- **Python 3.x**
- **Pygame** (para a interface gráfica)
- **Matplotlib** (para renderização de gradientes)

### Estrutura do Projeto

- **`main.py`**: Contém a lógica principal da interface gráfica e a interação com o usuário.
- **`puzzle_solver.py`**: Implementa o algoritmo A* para resolver o quebra-cabeça.
- **`state.py`**: Define o estado final (`GOAL_STATE`) e funções para gerar estados aleatórios e verificar a solubilidade.
- **`actions.py`**: Contém funções para movimentar as peças e verificar a validade dos movimentos.
- **`heuristics.py`**: Implementa a heurística de Manhattan usada pelo algoritmo A*.
- **`utils.py`**: Funções auxiliares para renderização gráfica, como desenho do tabuleiro e botões.
- **`config.py`**: Configurações visuais, como cores, tamanhos e fontes.

### Exemplo de Uso

```bash
python main.py
```

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar o código, adicionar novas funcionalidades ou corrigir bugs.
