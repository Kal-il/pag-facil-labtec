<h1 align="center"> Pag-Fácil LABTEC </h1>
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

## Índice 

* [Descrição do projeto](#descrição)
* [Funcionalidades](#hammer-requisitos-funcionais)
# **PagFacil LABTEC-UFT**

## :clipboard: **Descrição**
O **PagFacil LABTEC-UFT** é uma plataforma web desenvolvida para simplificar o processo de pagamento de encomendas realizadas no Laboratório de Tecnologias 3D da Universidade Federal do Tocantins (**LABTEC-UFT**).  
Através da plataforma, clientes podem preencher formulários com as informações necessárias, permitindo que o laboratório envie os dados ao órgão responsável pela emissão de boletos.

---

## :hammer: **Requisitos Funcionais**

### **Usuário (Cliente):**
- **`RF01: Tela Home`:**  
  Página inicial com informações sobre os serviços oferecidos pelo LABTEC-UFT, além de acesso fácil ao formulário de pagamento.

- **`RF02: Formulário para pagamento`:**  
  Os usuários podem preencher um formulário com seus dados pessoais e informações relacionadas ao serviço contratado.

---

### **Administrador (LABTEC):**
- **`RF03: Tela de gerenciamento`:**  
  Permite que o administrador visualize e gerencie as solicitações recebidas, incluindo informações do cliente e status da solicitação.

- **`RF04: Aprovação ou recusa de solicitações`:**  
  Com base nas informações fornecidas pelos clientes, o administrador pode aprovar ou recusar as solicitações.

- **`RF05: Download de formulários`:**  
  O administrador pode fazer o download de formulários preenchidos em formato PDF para manter registros.

- **`RF06: Envio de formulário por e-mail`:**  
  Funcionalidade para enviar o formulário preenchido por e-mail ao órgão responsável pela emissão de boletos.

- **`RF07: Tela de login`:**  
  Um único administrador tem acesso ao sistema, sendo necessário login para gerenciar as solicitações.

---

## :gear: **Tecnologias Utilizadas**
- **Backend:** Django + Django REST Framework.
- **Frontend:** Bootstrap 5.
- **Banco de Dados:** SQLite (ou PostgreSQL, conforme necessidade futura).
- **Estilo Visual:** Alinhado à identidade do LABTEC-UFT.

---

