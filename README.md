# Escalonador EDF - Earliest Deadline First

## Descrição
Este é um aplicativo simples de escalonamento usando o algoritmo Earliest Deadline First (EDF) implementado em Python com interface gráfica usando Tkinter e gráficos usando Matplotlib.

## Pré-requisitos
- Python 3.x instalado (recomenda-se a versão 3.6 ou superior)
- Pacotes listados em `requirements.txt` instalados.


## Instalação
1. Clone ou faça o download deste repositório.

2. Navegue até o diretório do projeto:
```
cd escalonador-edf
```
3. Instale as dependências listadas em `requirements.txt`:
```
pip install -r requirements.txt
```
ou
```
pip3 install -r requirements.txt
```

Este comando instala todas as bibliotecas Python necessárias para executar o projeto, conforme especificado no arquivo `requirements.txt`.


## Execução
Para iniciar o aplicativo do Escalonador EDF, execute o seguinte comando no terminal:
```
python main.py
```

Isso iniciará a aplicação de Escalonador EDF com uma interface gráfica.

Certifique-se de que o Python esteja corretamente instalado em seu sistema antes de executar os comandos acima.


## Utilização
- **Adicionar Tarefa:** Insira o Tempo de Execução (ET) e o Período da tarefa nos campos correspondentes e clique em "Adicionar Tarefa".
- **Agendar:** Depois de adicionar todas as tarefas desejadas, clique em "Agendar" para calcular e exibir o escalonamento EDF.
- **Gráfico:** O gráfico exibe visualmente o escalonamento das tarefas.
