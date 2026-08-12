# Gungo Agência & Marketing — Guia de Contribuição

Este ficheiro define o padrão de trabalho para **qualquer agente de IA** (Claude, GPT, Gemini, etc.) ou pessoa que edite este repositório. O objetivo é manter um histórico organizado de tudo o que é feito no site, e nunca alterar o site publicado (produção) diretamente sem revisão.

## Stack do projeto
- `index.html` — site público (Firebase Firestore + Cloudinary para conteúdo dinâmico)
- `admin.html` — área da equipa (login Firebase Auth)
- `firebase-config.js` — configuração do Firebase e Cloudinary (não conter segredos sensíveis; as chaves aqui são públicas por natureza do Firebase client SDK)
- Hospedagem: Netlify, com deploy automático a partir do ramo `main` deste repositório
- Base de dados: Firebase Firestore (coleções: `portfolio`, `partners`, `testimonials`, `content`, `avaliacoes`, `sugestoes`, `atividades`)
- Imagens: Cloudinary (upload não assinado via `upload_preset`)

## Regra principal: Issue → Branch → Pull Request

**Nenhuma alteração é feita diretamente no ramo `main`.** Todo o trabalho segue este ciclo:

### 1. Criar uma Issue
Antes de qualquer trabalho (correção de bug, melhoria, ou nova funcionalidade), criar uma Issue no GitHub que descreva:
- **Título curto** e claro (ex: "Corrigir botão do WhatsApp no rodapé")
- **Tipo**: usar um label — `bug` (correção), `enhancement` (melhoria), ou `feature` (nova função)
- **Descrição**: o que está errado ou o que se pretende adicionar, e porquê
- **Critério de aceitação**: como saber que está resolvido

### 2. Criar um branch a partir da Issue
Nome do branch deve referenciar o número da issue, ex: `issue-12-corrigir-whatsapp-rodape`.

### 3. Fazer as alterações nesse branch
Nunca commitar diretamente em `main`.

### 4. Abrir um Pull Request
- O título do PR deve ser claro sobre o que muda
- **A descrição do PR TEM de mencionar a Issue correspondente**, usando a sintaxe do GitHub que fecha a issue automaticamente ao fazer merge:
  ```
  Closes #12
  ```
  ou `Fixes #12` / `Resolves #12`
- Descrever brevemente o que foi alterado e como foi testado

### 5. Rever e fazer merge
- Idealmente, pedir revisão antes do merge (mesmo que seja o próprio Faustino a rever)
- Só depois do merge em `main` é que o Netlify publica automaticamente as alterações no site ao vivo

## Convenções de commits
Mensagens de commit curtas, em português, no imperativo:
- `Corrige link do WhatsApp no rodapé`
- `Adiciona secção de bastidores`
- `Melhora contraste do texto no hero`

## Notas importantes para qualquer agente
- Faustino (dono do projeto) **não é programador** — as instruções e explicações devem ser sempre simples, em português, passo a passo, assumindo zero conhecimento técnico
- Nunca sugerir uso de terminal/linha de comandos como primeira opção — preferir sempre a interface web do GitHub quando possível
- As regras de segurança do Firestore ficam documentadas separadamente; qualquer nova coleção Firestore criada precisa de uma regra de segurança correspondente, e isso deve ser referido explicitamente na Issue e no PR
- O ficheiro `firebase-config.js` contém identificadores públicos do Firebase (não é uma chave secreta de servidor) — mas ainda assim não deve ser exposto desnecessariamente fora do necessário
