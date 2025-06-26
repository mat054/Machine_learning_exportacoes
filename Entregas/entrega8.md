# Finalização do trabalho

## Mini Trabalho 8 - Lançamento, monitoramento e manutenção do sistema

### Equipe
- Daniela Soares de Oliveira - 180015222
- Gabriel Freitas Balbino - 180075462
- Mateus de Castro Santos - 222015195
- Pablo Santos Costa - 180128817
- Pedro Lucas Dourado Santos - 211039680

## Descrição do Trabalho Realizado:
Este mini trabalho teve como objetivo entregar a solução final do nosso projeto de machine learning e fazer o deploy dela com um plano de monitoramento e manutenção.
Nosso plano é que seja um projeto Open Source e de contribuição voluntária, então foi realizado um [Guia de Contribuição](CONTRIBUTING.md), [Código de Conduta](CODE_OF_CONDUCT.md) e a adição de uma [Licença](LICENSE) com o intuito de orientar e facilitar as contribuições da comunidade.

Apesar dos artefatos gerados, para um melhor monitoramento e manutenção do nosso modelo treinado, o grupo optou por escolher a ferramenta [MLflow](https://mlflow.org/) por achar mais adequada e de fácil entendimento. Ela é uma ferramenta para gerenciar o ciclo de vida de projetos de Machine Learning, desde o começo até o monitoramento em produção.

Também foi iniciado o desenvolvimento de uma interface web utilizando a biblioteca do Python chamada **streamlit**. Por meio dessa interface, o usuário pode selecionar a especiaria, o país e o ano desejados, de forma prática e intuitiva, para que o sistema realize a previsão correspondente. Para executar basta:

```bash
streamlit run app.py
```

### Como o MLflow nos ajuda?

A seguir, destacamos como o MLflow contribui para as principais etapas do ciclo de vida do nosso projeto:

1.Desenvolvimento:

- Ele treina vários modelos e registra métricas com MLflow Tracking.
- Escolhe o melhor modelo com base nos resultados.

2.Deploy:

- Registra o modelo no Model Registry.
- Promove o modelo para o estágio Production.

3.Monitoramento:

- Coleta métricas reais de produção.
- Compara o desempenho atual com o esperado.

4.Manutenção:

Caso o desempenho venha a cair, é possivel:

- Treinar um novo modelo.
- Testar em ambiente de staging.
- Promover para produção via MLflow quando pronto.

Para informações detalhadas sobre a execução da solução e os procedimentos relacionados a esta entrega, consulte o arquivo: [README_MLflow.md](README_MLflow.md)


