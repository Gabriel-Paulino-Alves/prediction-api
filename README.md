# prediction-api
api feita em FLASK para realizar a predição de imagens via requisição POST

foi utilizada a base pré treinada da KAGGLE https://www.kaggle.com/datasets/gpiosenka/sports-classification -> possui 100 classes de sports diferentes

Modelo treinado no Google Colab: https://colab.research.google.com/drive/1u60lg2j21IgR1nh_OHJNomGugKVTS9gE?usp=sharing

Passo a passo de execução:
  COLAB:
- Executar os blocos de código um por um em ordem descendente
- Editar de acordo com suas preferencias (tamanho da img, batch, epochs, etc...)
- após o treinamento execute a função model.save() para salvar o modelo treinado
- Salve o modelo treinado em sua maquina utilizando :
  from google.colab import files
  files.download('my_model.h5')

  IDE de desenvolvimento:
- Crie a estrutura do seu projeto e faça upload do modelo treinado
- Execute a API com o comando flask run

  POSTMAN:
- Crie uma nova coleção
- Selecione o método POST
- vá em "body" e mude de "none" para "form-data"
- logo embaixo mude o campo "text" para "image" e o valor para file
- faça o upload do seu arquivo e clique em send
- e a magia irá acontecer
