import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-pagamentos',
  templateUrl: './pagamentos.page.html',
  styleUrls: ['./pagamentos.page.scss'],
})
export class PagamentosPage implements OnInit {

  // Usando o operador ! para garantir que será atribuído um valor antes de usar
  nome_cliente!: string;
  cpf_cnpj!: string;
  endereco!: string;
  cidade!: string;
  estado!: string;
  cep!: string;
  telefone!: string;
  email!: string;
  servico!: string;

  constructor(private apiService: ApiService) {}

  alertButtons = ['Voltar'];

  ngOnInit() {
  }

  submitForm() {
    // Enviar os dados do formulário
    const formData = {
      nome_cliente: this.nome_cliente,
      cpf_cnpj: this.cpf_cnpj,
      endereco: this.endereco,
      cidade: this.cidade,
      estado: this.estado,
      cep: this.cep,
      telefone: this.telefone,
      email: this.email,
      servico: this.servico
    };

    this.apiService.postData(formData).subscribe(response => {
      console.log(response);
    });
  }
}
