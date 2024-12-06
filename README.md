# Simulação de Campo Elétrico

Este aplicativo Python permite simular e visualizar o campo elétrico gerado por cargas pontuais em um plano bidimensional. O programa utiliza as bibliotecas `numpy` e `matplotlib` para realizar cálculos e renderizar gráficos interativos.

## Funcionalidades
- Inserção de cargas pontuais com suas coordenadas e magnitudes.
- Simulação do campo elétrico gerado pelas cargas.
- Visualização do vetor de campo elétrico como linhas de fluxo.
- Personalização do título da simulação.

## Requisitos
Certifique-se de ter o Python 3 instalado no sistema. Além disso, instale as bibliotecas necessárias:

```bash
pip install numpy matplotlib
```

## Como Usar
1. **Execute o script**:
   ```bash
   python simulacao_eletromagnetismo.py
   ```

2. **Insira as cargas manualmente**:
   - O programa solicitará as coordenadas `x`, `y` e a magnitude `q` (em Coulombs) de cada carga.
   - Digite "fim" para encerrar a entrada de cargas.

   Exemplo de entrada:
   ```
   Insira a coordenada x da carga (ou 'fim' para encerrar): 0
   Insira a coordenada y da carga: 0
   Insira a magnitude da carga (em Coulombs): 1e-9
   Insira a coordenada x da carga (ou 'fim' para encerrar): fim
   ```

3. **Simulação com valores padrão**:
   - Caso nenhuma carga seja inserida, o programa utilizará valores padrão:
     - Carga 1: `(0, 0, 1e-9)`
     - Carga 2: `(1, 1, -1e-9)`
     - Carga 3: `(-1, -1, 2e-9)`

4. **Visualização**:
   - O gráfico exibirá o campo elétrico como linhas de fluxo, com as cargas representadas como pontos coloridos.
   - Cargas positivas são marcadas em vermelho, e cargas negativas em azul.

## Personalização
- **Intervalo do gráfico**:
  Altere os parâmetros `x_range` e `y_range` na função `plot_electric_field` para ajustar o intervalo do plano de visualização.
  ```python
  plot_electric_field(user_charges, x_range=(-5, 5), y_range=(-5, 5))
  ```
- **Título da simulação**:
  Personalize o título passando o argumento `app_title`:
  ```python
  plot_electric_field(user_charges, x_range=(-2, 2), y_range=(-2, 2), app_title="Minha Simulação de Eletromagnetismo")
  ```

## Exemplo de Uso
Ao executar o programa com cargas padrão, o gráfico gerado será semelhante ao seguinte:

![Exemplo de Campo Elétrico](example_plot.png)

## Licença
Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.

