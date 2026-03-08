# 🚀 INSTRUÇÕES DE DEPLOYMENT

Seu repositório Git está **pronto** com todos os arquivos!

---

## OPÇÃO 1: Deploy Automático com GitHub Pages (Recomendado)

### Passo 1: Criar Repositório no GitHub
1. Acesse: https://github.com/new
2. Crie um repositório com o nome: `bradesco-livelo`
3. **Não** inicialize com README (já temos)
4. Clique em "Create repository"

### Passo 2: Fazer Push do Repositório Local

Execute estes comandos no PowerShell (estar na pasta `deploy`):

```powershell
git remote add origin https://github.com/SEU_USERNAME/bradesco-livelo.git
git branch -M main
git push -u origin main
```

**Substitua `SEU_USERNAME` pelo seu username do GitHub**

### Passo 3: Ativar GitHub Pages

1. Vá para: https://github.com/SEU_USERNAME/bradesco-livelo
2. Clique em "Settings" (Configurações)
3. Vá em "Pages" (no menu esquerdo)
4. Em "Source", selecione:
   - Branch: `main`
   - Folder: `/ (root)`
5. Clique em "Save"

### Passo 4: Acessar Seu Site

Seu site estará disponível em:
```
https://SEU_USERNAME.github.io/bradesco-livelo/
```

**O deploy pode levar 1-2 minutos para ativar.**

---

## OPÇÃO 2: Deploy Rápido com Surge.sh

Se o PowerShell como Admin não funcionar, tente Windows Terminal:

1. Abra **Windows Terminal** como Administrador
2. Navegue até a pasta deploy:
   ```powershell
   cd c:\Users\PC\Desktop\brada\deploy
   ```
3. Execute:
   ```powershell
   surge .
   ```
4. Siga os prompts (email, senha, domínio)

---

## 📋 Estrutura do Repositório

```
.
├── index.html          (página principal)
├── favicon.ico         (ícone)
├── README.md           (informações)
├── DEPLOY_INSTRUCTIONS.md (este arquivo)
└── assets/
    ├── CSS
    ├── JavaScript
    ├── Imagens
    └── Fontes
```

---

## ✅ Verificação

Depois de fazer push ou deploy, você pode:
- Acessar a URL do seu site
- Verificar se todas as imagens carregam
- Testar o formulário

---

**Pronto para fazer push? Avise quando conseguir!** 🎉