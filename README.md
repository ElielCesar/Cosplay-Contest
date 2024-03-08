# Cosplay Contest

Um sistema desenvolvido em Python e Django, projetado para avaliação e pontuação em festivais regionais de cosplay.

## Características Principais:

### **Categorias de Cosplay**:
1. **Fantasy**:
    - Focado em cosplays profissionais ou semi-profissionais.
    - Quesitos de pontuação:
      - Criatividade
      - Estética
      - Performance de palco
      - Sustentabilidade
    OBS: Mais critérios podem ser adicionadas pelo desenvolvedor, caso necessário.

2. **Makeyourself (Faça você mesmo)**:
    - Voltado para cosplays mais amadores, criados com materiais comuns do dia a dia.
    - Quesitos de pontuação:
      - Criatividade
      - Estética
      - Performance de palco
      - Sustentabilidade
       OBS: Mais critérios podem ser adicionadas pelo desenvolvedor, caso necessário.

## Personalização:
O sistema apresenta um layout simples com interface web, permitindo uma fácil personalização. Cores, logos e imagens podem ser adaptadas conforme a necessidade do evento ou do organizador.

## **Funcionamento**:
    1 - Deve ser criado um usuário administrador do django.
    2 - Caso já não exista, deve ser criado 2 grupos com exatamente esses nomes: jurados, administradores.
    3 - Todos os participantes devem se inscrever pela página de cadastro, os jurados devem ser adicionados ao grupo jurados pelo admin do django.
    4 - Após se cadastrarem no sistema os cosplayers/participantes devem se cadastrar em uma das 2 categorias existentes.
    5 - Somente o admin do django pode cadastrar no sistema os apoiadores, jurados e organizadores, esse cadastro é meramente
    para fins informativos e não afetam em nada os usuários cadastrados no sistema, são apenas uma espécie de banner independente.
    6 - Somente jurados podem avaliar os participantes e dar as notas.
    7 - Cada usuário pode se inscrever e apagar sua inscricão como participante, caso tenha se inscrito em uma categoria errada ou com dados errados, o participante deve apagar a inscricão e faze-la novamente com os dados corretos.
    8 - A apuracão acontece em tempo real pelas abas ranking Fantasy e ranking Make Your Self.
    9 - Caso o usuário esqueca sua senha, ele deve entrar em contato com o administrador do sistema para que ela seja resetada.
---

Para mais informações ou dúvidas sobre o sistema, sinta-se à vontade para abrir uma issue ou enviar uma mensagem.
