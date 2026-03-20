# 🎯 Guia Visual: Deploy no Render (Passo a Passo)

## 📊 Fluxo Completo

```
┌────────────────────────────────────────────────────────────────┐
│ 1. Criar PostgreSQL Database                                  │
├────────────────────────────────────────────────────────────────┤
│ 2. Criar Web Service (Conectar GitHub)                        │
├────────────────────────────────────────────────────────────────┤
│ 3. Configurar Environment Variables (DATABASE_URL)            │
├────────────────────────────────────────────────────────────────┤
│ 4. Deploy Automático + Testes                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## 🔷 PASSO 1: Criar Banco de Dados PostgreSQL

### 1.1 - Acesse o Render Dashboard
```
URL: https://dashboard.render.com
```

**O que você verá:**
```
┌─────────────────────────────────────────┐
│  🏠 Render Dashboard                    │
├─────────────────────────────────────────┤
│                                         │
│  [👤 Account]  [⚙️ Settings]  [➕ New] │
│                                         │
│  ❌ NO SERVICES YET                     │
│                                         │
└─────────────────────────────────────────┘
```

---

### 1.2 - Clique no botão "+ New"

**Procure por este botão no canto superior direito:**

```
┌─────────────────────────────┐
│          ➕ New +            │
└─────────────────────────────┘
        ↓ Clique aqui
```

**Um menu irá aparecer:**

```
┌─────────────────────────────────────────┐
│  ➕ NEW                                 │
├─────────────────────────────────────────┤
│  ✦ Web Service                          │
│  ✦ PostgreSQL                    👈 ISTO│
│  ✦ Redis                               │
│  ✦ Static Site                          │
│  ✦ Background Worker                    │
│  ✦ Cron Job                             │
└─────────────────────────────────────────┘
```

---

### 1.3 - Selecione "PostgreSQL"

**Você verá este formulário:**

```
┌─────────────────────────────────────────────┐
│  🐘 Create a New PostgreSQL                 │
├─────────────────────────────────────────────┤
│                                             │
│  Name:  ┌──────────────────────────────┐   │
│         │ bradesco-db                  │   │
│         └──────────────────────────────┘   │
│                                             │
│  Database:  ┌──────────────────────────┐   │
│             │ bradesco_db              │   │
│             └──────────────────────────┘   │
│                                             │
│  User:  ┌──────────────────────────────┐   │
│         │ bradesco_user                │   │
│         └──────────────────────────────┘   │
│                                             │
│  Region: ┌──────────────────────────────┐  │
│          │ 🌎 Escolha mais perto        │  │
│          └──────────────────────────────┘  │
│                                             │
│  [ Create Database ]                        │
│                                             │
└─────────────────────────────────────────────┘
```

---

### 1.4 - Copie a Database URL

**Após criar, você verá:**

```
┌────────────────────────────────────────────────────────┐
│  ✅ PostgreSQL Created!                                │
├────────────────────────────────────────────────────────┤
│                                                        │
│  📋 External Database URL:                             │
│  ┌──────────────────────────────────────────────────┐ │
│  │ postgresql://bradesco_user:PASSWORD@host:5432   │ │
│  │ /bradesco_db                                     │ │
│  └──────────────────────────────────────────────────┘ │
│                                  [📋 Copiar]          │
│                                                        │
│  ⚠️ Guarde esta URL com segurança!                    │
│                                                        │
└────────────────────────────────────────────────────────┘
```

✅ **Copie esta URL!** Você vai precisar dela em breve.

---

## 🟦 PASSO 2: Criar Web Service

### 2.1 - Clique em "+ New" novamente

```
┌─────────────────────────────┐
│          ➕ New +            │
└─────────────────────────────┘
        ↓ Clique aqui
```

---

### 2.2 - Selecione "Web Service"

```
┌─────────────────────────────────────────┐
│  ➕ NEW                                 │
├─────────────────────────────────────────┤
│  ✦ Web Service               👈 ISTO   │
│  ✦ PostgreSQL                          │
│  ✦ Redis                               │
│  ✦ Static Site                          │
│  ✦ Background Worker                    │
│  ✦ Cron Job                             │
└─────────────────────────────────────────┘
```

---

### 2.3 - Conecte seu Repositório GitHub

**Você verá suas opções:**

```
┌──────────────────────────────────────────────────┐
│  🔗 Connect a Repository                         │
├──────────────────────────────────────────────────┤
│                                                  │
│  🔍 Procure por seu repositório:                 │
│  ┌──────────────────────────────────────────┐   │
│  │ deploy                              [🔄] │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  📦 Repositórios disponíveis:                    │
│  ┌──────────────────────────────────────────┐   │
│  │ ✓ phdaserra171/deploy             👈 CLI│   │
│  │                                          │   │
│  │ [ Connect to this repo ]                │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
└──────────────────────────────────────────────────┘
```

**Clique em "Connect to this repo"**

---

### 2.4 - Configure o Web Service

**Você verá este formulário:**

```
┌────────────────────────────────────────────────────┐
│  ⚙️ Configure Web Service                          │
├────────────────────────────────────────────────────┤
│                                                    │
│  Name:  ┌──────────────────────────────────────┐  │
│         │ bradesco-livelo                      │  │
│         └──────────────────────────────────────┘  │
│                                                    │
│  Environment: ┌──────────────────────────────┐   │
│               │ Python 3                ▼    │   │
│               └──────────────────────────────┘   │
│                                                    │
│  Build Command:  ┌──────────────────────────┐   │
│                  │ pip install -r            │   │
│                  │ requirements.txt          │   │
│                  └──────────────────────────┘   │
│                                                    │
│  Start Command:  ┌──────────────────────────┐   │
│                  │ gunicorn server:app      │   │
│                  └──────────────────────────┘   │
│                                                    │
│  Instance Type: [ Free ] (Compatível)            │
│                                                    │
│  [ Continue ]                                     │
│                                                    │
└────────────────────────────────────────────────────┘
```

✅ **Clique em "Continue"**

---

## 🔐 PASSO 3: Adicionar Variáveis de Ambiente

### 3.1 - Na tela de Environment Variables

**Você verá:**

```
┌─────────────────────────────────────────────────────┐
│  🔐 Environment Variables                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [ ➕ Add Environment Variable ]                    │
│                                                     │
│  Nenhuma variável adicionada ainda                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### 3.2 - Clique em "Add Environment Variable"

```
┌───────────────────────────────────────┐
│  [ ➕ Add Environment Variable ]       │
│           ↓ Clique aqui
```

---

### 3.3 - Preencha a Variável

**Você verá este campo:**

```
┌────────────────────────────────────────┐
│  Key:   ┌──────────────────────────┐   │
│         │ DATABASE_URL             │   │
│         └──────────────────────────┘   │
│                                        │
│  Value:                                │
│  ┌────────────────────────────────┐   │
│  │ postgresql://bradesco_user:... │   │
│  │ @xxxxx.onrender.com:5432/      │   │
│  │ bradesco_db                     │   │
│  └────────────────────────────────┘   │
│         👆 Cole a URL copiada!        │
│                                        │
│  [ Save Variable ]                     │
│                                        │
└────────────────────────────────────────┘
```

✅ **Cole a URL do PostgreSQL aqui!**

---

## 🚀 PASSO 4: Deploy!

### 4.1 - Clique em "Create Web Service"

```
┌──────────────────────────────────────┐
│  [ Create Web Service ]              │
│       ↓ Clique para fazer deploy
```

---

### 4.2 - Aguarde o Build (2-5 minutos)

**Você verá a tela de logs:**

```
┌─────────────────────────────────────────────┐
│  📊 Build Logs                              │
├─────────────────────────────────────────────┤
│                                             │
│  ⏳ Building...                              │
│  └─ Cloning repository...                  │
│  └─ Installing dependencies...              │
│  └─ Running build command...                │
│  └─ Starting application...                 │
│                                             │
│  💡 Isto pode levar 2-5 minutos            │
│                                             │
└─────────────────────────────────────────────┘
```

**Quando terminar:**

```
┌─────────────────────────────────────────────┐
│  ✅ Deploy Successful!                      │
├─────────────────────────────────────────────┤
│                                             │
│  🌐 Your app is live!                       │
│                                             │
│  📍 URL:                                    │
│  https://bradesco-livelo.onrender.com      │
│                                             │
│  [ Open Site ]                              │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ✅ PASSO 5: Teste seu App

### 5.1 - Acesse o Frontend

```
https://bradesco-livelo.onrender.com
```

**Você deve ver:**
```
┌─────────────────────────────────────────┐
│  🏦 Bradesco - Livelo                   │
├─────────────────────────────────────────┤
│                                         │
│  CPF: ┌─────────────────────────────┐  │
│       │ 000.000.000-00              │  │
│       └─────────────────────────────┘  │
│                                         │
│  Telefone: ┌──────────────────────┐   │
│            │ (00) 00000-0000      │   │
│            └──────────────────────┘   │
│                                         │
│  [ 🔄 Resgatar ]                        │
│                                         │
└─────────────────────────────────────────┘
```

✅ Preencha e clique em "Resgatar"

---

### 5.2 - Verifique se os dados foram salvos

```
https://bradesco-livelo.onrender.com/admin
```

**Você deve ver:**
```
┌────────────────────────────────────────────┐
│  📊 Dados Registrados                      │
├────────────────────────────────────────────┤
│                                            │
│ ID │ Timestamp │ CPF │ Telefone │ Agência │
├────┼───────────┼─────┼──────────┼─────────┤
│ 1  │ 2026-03.. │ *** │ (11)... │ 1234    │
│                                            │
│ [ Apagar todos os dados ]                  │
│                                            │
└────────────────────────────────────────────┘
```

✅ **Perfeito! Está funcionando!**

---

## 📋 Checklist Final

- [ ] ✅ PostgreSQL criado no Render
- [ ] ✅ Web Service criado no Render
- [ ] ✅ `DATABASE_URL` configurada
- [ ] ✅ Deploy concluído (status: ✅ Live)
- [ ] ✅ Frontend carrega em `https://bradesco-livelo.onrender.com`
- [ ] ✅ Admin mostra dados em `/admin`
- [ ] ✅ Dados são salvos no banco PostgreSQL

---

## ⚠️ Se der erro...

| Erro | Solução |
|------|---------|
| **502 Bad Gateway** | Aguarde 2-3 minutos. O servidor pode estar iniciando. |
| **Conexão recusada** | Verifique se `DATABASE_URL` está configurada corretamente. |
| **Dados não salvam** | Acesse `/admin` para ver logs de erro. |
| **Aplicação dorme** | Normal no plano Free. Primeira requisição pode demorar 30-60s. |

---

## 🎉 Parabéns! Seu app está no ar!

**URL do seu app:** https://bradesco-livelo.onrender.com

**Gerencie aqui:** https://dashboard.render.com
