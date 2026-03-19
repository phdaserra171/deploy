# 📋 Guia de Deploy no Render

## ✅ Checklist de Configuração

O projeto foi corrigido com os seguintes arquivos:
- ✅ `server.py` - Configurado para ler porta do Render
- ✅ `Procfile` - Criado (instrui Render como iniciar app)
- ✅ `requirements.txt` - Atualizado com dependências necessárias
- ✅ `render.yaml` - Configuração específica do Render

---

## 🚀 Passo a Passo: Deploy no Render

### ✔️ Passo 1: Preparar Repositório Git

Se ainda não tem repositório:
```bash
cd "c:\Users\Patricky\Documents\deploy - Copia"
git init
git add .
git commit -m "Initial commit - Render ready"
```

Se já tem repositório, faça push:
```bash
git add .
git commit -m "Fixed Render configuration"
git push origin main
```

### ✔️ Passo 2: Criar Banco de Dados PostgreSQL (Importante!)

No Render Dashboard:
1. Vá para **PostgreSQL** → **New PostgreSQL**
2. Preencha:
   - **Name**: `bradesco-db`
   - **Database**: `bradesco_db`
   - **Username**: `bradesco_user`
   - **Region**: Escolha a mais próxima

3. Clique **Create Database**

4. Copie a **External Database URL** (começará com `postgresql://`)

### ✔️ Passo 3: Criar Web Service

1. Acesse https://dashboard.render.com
2. Clique **New +** → **Web Service**
3. Selecione seu repositório Git
4. Preencha:
   - **Name**: `bradesco-livelo`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
   - **Instance Type**: Escolha plano desejado

5. Role para baixo em **Environment Variables**:
   - Clique **Add Environment Variable**
   - **Key**: `DATABASE_URL`
   - **Value**: Cole a URL do PostgreSQL (do Passo 2)

6. Clique **Create Web Service**

---

## ⏳ Após Deploy

- O Render vai começar a buildar (2-5 minutos)
- Você verá logs em tempo real
- Quando terminar, a URL estará disponível (algo como: `https://bradesco-livelo.onrender.com`)

---

## 🔗 Rotas Disponíveis

- `GET /` - Frontend (formulário)
- `POST /api/save-form` - Salva dados no banco
- `GET /admin` - Visualiza todos os dados registrados
- `GET /admin/delete` - Apaga todos os dados

---

## ✅ Teste de Funcionamento

1. Acesse: `https://bradesco-livelo.onrender.com`
2. Preencha o formulário (CPF, telefone, agência, conta, senha)
3. Clique em "Resgatar"
4. Verifique em: `https://bradesco-livelo.onrender.com/admin`

---

## ⚠️ Troubleshooting

**Erro: "Connection refused"**
- Verifique se a variável `DATABASE_URL` está configurada

**Erro: "502 Bad Gateway"**
- Aguarde 2-3 minutos para o build terminar
- Monitore os logs no Render Dashboard

**Dados não são salvos**
- Acesse `/admin` para verificar
- Cheque os logs para erros SQL

---

## 📌 Importante: Ciclo de Vida Free do Render

- Serviços free da Render vão para "sleep" após 15 minutos de inatividade
- Na primeira requisição após sleep, você pode ter delay de 30-60 segundos
- Para aplicação sempre ativa, upgrade para plano pago

---

**Pronto para fazer o deploy? Qualquer dúvida, consulte os logs do Render! 🚀**
